import os
import os.path as osp
import time
from itertools import product
from hashlib import sha1
from subprocess import check_call, DEVNULL

import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import json


# some global configs
x64 = False
cqt_fmin = librosa.note_to_hz('A1')
files = [
    "Hands Up - Hommarju.wav"
]


class Codec:
    def __init__(self, path, cmd_args):
        '''
        path: path to the codec binary
        cmd_args: (extr) command line args for encoding, used for adjusting compression level
        '''
        self.path = osp.abspath(path)
        if isinstance(cmd_args, (list, tuple)):
            self.cmd_args = list(cmd_args)
        else:
            self.cmd_args = [cmd_args]

    def encode(self, fin):
        pass

    def decode(self, fin):
        pass

    def __str__(self):
        return f"{self.__class__.__name__} ({' '.join(self.cmd_args)})"

class flac(Codec):
    def __init__(self, path, cmd_args):
        super().__init__(path, cmd_args)

    def encode(self, fin):
        fout = fin + ".flac"
        check_call([self.path, fin, "-sf", "-o", fout] + self.cmd_args)
        return fout

    def decode(self, fin):
        fout = fin + ".wav"
        check_call([self.path, fin, "-sfd", "-o", fout])
        return fout

class mac(Codec):
    def __init__(self, path, cmd_args):
        super().__init__(path, cmd_args)

    def encode(self, fin):
        fout = fin + ".ape"
        check_call([self.path, fin, fout] + self.cmd_args, stdout=DEVNULL, stderr=DEVNULL)
        return fout

    def decode(self, fin):
        fout = fin + ".wav"
        check_call([self.path, fin, fout, "-d"], stdout=DEVNULL, stderr=DEVNULL)
        return fout
        
class wavpack(Codec):
    def __init__(self, path, cmd_args):
        super().__init__(path, cmd_args)

    def encode(self, fin):
        fout = fin + ".wv"
        check_call([self.path, '-y'] + self.cmd_args + [fin, fout], stdout=DEVNULL, stderr=DEVNULL)
        return fout

    def decode(self, fin):
        fout = fin + ".wav"
        wvunpack = self.path.replace("wavpack.exe", "wvunpack.exe")
        check_call([wvunpack, '-y', fin, fout], stdout=DEVNULL, stderr=DEVNULL)
        return fout

class lame(Codec):
    def __init__(self, path, cmd_args):
        super().__init__(path, cmd_args)

    def encode(self, fin):
        fout = fin + ".mp3"
        check_call([self.path, "--quiet"] + self.cmd_args + [fin, fout])
        return fout

    def decode(self, fin):
        fout = fin + ".wav"
        check_call([self.path, "--quiet", "--decode", fin, fout])
        return fout

# encoder paths
flac_path = './codecs/flac_x64.exe' if x64 else './codecs/flac.exe'
mac_path = "./codecs/MAC_x64.exe" if x64 else './codecs/MAC.exe'
wavpack_path = "./codecs/wavpack_x64.exe" if x64 else './codecs/wavpack.exe'
lame_path = './codecs/lame_x64.exe' if x64 else './codecs/lame.exe'

# lossless codes
flac_codecs = [flac(flac_path, '-' + str(c)) for c in range(8)]
ape_codecs = [mac(mac_path, '-c%d000' % c) for c in range(1, 6)]
wavpack_lossless_codecs = [wavpack(wavpack_path, a) for a in ['-f',[],'-h','-hh']]
wavpack_lossless_hybrid_codecs = [wavpack(wavpack_path, ['-c', '-b192'] + a) for a in [['-f'],[],['-h'],['-hh']]]

lossless_codecs = {
    "flac": flac_codecs,
    "ape": ape_codecs,
    "wavpack": wavpack_lossless_codecs,
    "wavpack(hybrid)": wavpack_lossless_hybrid_codecs
}

# lossy codes
birates = [128, 160, 192, 256, 320]
wavpack_lossy_codecs = [wavpack(wavpack_path, ['-b' + str(b)]) for b in birates]
wavpack_lossless_hybrid_codecs = [wavpack(wavpack_path, ['-c', '-b' + str(b)]) for b in birates]
lame_cbr_codecs = [lame(lame_path, ['-b' + str(b), '-q' + str(q)]) for b, q in product(birates, [2, 7])] # note: CBR <= 96kbps leads to downsampling
lame_vbr_codecs = [lame(lame_path, ['-V' + str(v), '-q' + str(q)]) for v, q in product(range(7), [2, 7])] # note: VBR <= V7 leads to downsampling

lossy_codecs = {
    "mp3(CBR)": lame_cbr_codecs,
    "mp3(VBR)": lame_vbr_codecs,
    "wavpack": wavpack_lossy_codecs + wavpack_lossless_hybrid_codecs
}

def spectro(audio):
    spectro = librosa.stft(audio, n_fft=4096)
    sdb = librosa.amplitude_to_db(np.abs(spectro), ref=np.max)
    return sdb

def weighted_spectro(audio, sr):
    C = np.abs(librosa.cqt(audio, sr=sr, fmin=cqt_fmin))
    freqs = librosa.cqt_frequencies(C.shape[0], fmin=cqt_fmin)
    perceptual_sdb = librosa.perceptual_weighting(C**2, freqs, ref=np.max)
    return perceptual_sdb

def array_hash(audio):
    return sha1(audio).digest()

def run_benchmark():
    results = {}
    for audio_file in files:
        print("> ----- Testing with", audio_file, "-----")
        asize = osp.getsize(audio_file)

        # load audio and calculate spectrogram
        audio, sr = librosa.load(audio_file, sr=None)
        ahash = array_hash(audio)
        sdb = spectro(audio)
        psdb = weighted_spectro(audio, sr)

        print("Saving spectrograms")
        fig, ax = plt.subplots(figsize=(16, 5), nrows=2)
        img = librosa.display.specshow(sdb, x_axis='time', y_axis='log', ax=ax[0], sr=sr, hop_length=1024)
        fig.colorbar(img, ax=ax[0], format="%+2.f dB")
        ax[0].set(title="spectrogram", xlabel="")
        img = librosa.display.specshow(psdb, x_axis='time', y_axis='cqt_hz', ax=ax[1], sr=sr, fmin=cqt_fmin)
        fig.colorbar(img, ax=ax[1], format="%+2.f dB")
        ax[1].set(title="weighted spectrogram")
        plt.tight_layout()
        if not osp.exists("./figs"):
            os.mkdir("./figs")
        fig.savefig("figs/" + osp.basename(audio_file) + ".jpg")

        lossless_results = {}
        print("Benchmarking lossless codecs...")
        for series, codecs in lossless_codecs.items():
            series_results = []
            for codec in codecs:
                print("Testing", codec, end="")
                
                tstart = time.time()
                fresult = codec.encode(audio_file)
                encode_time = time.time() - tstart

                if "hybrid" in series: # for wavpack hybrid mode
                    result_size = osp.getsize(fresult) + osp.getsize(fresult.replace(".wv", ".wvc"))
                else:
                    result_size = osp.getsize(fresult)

                tstart = time.time()
                fback = codec.decode(fresult)
                decode_time = time.time() - tstart

                raudio, _ = librosa.load(fback, sr=None)
                hash_consistent = array_hash(raudio) == ahash
                print(", hash check:", hash_consistent)

                series_results.append(dict(
                    codec=str(codec),
                    encode_time=encode_time,
                    decode_time=decode_time,
                    hash_consistent=hash_consistent,
                    compression_ratio=result_size / asize
                ))
            lossless_results[series] = series_results

        print("Benchmarking lossy codecs...")
        lossy_results = {}
        for series, codecs in lossy_codecs.items():
            series_results = []
            for codec in codecs:
                print("Testing", codec, end="")
                
                tstart = time.time()
                fresult = codec.encode(audio_file)
                encode_time = time.time() - tstart

                result_size = osp.getsize(fresult)
                if osp.exists(audio_file + ".wvc"): # prevent wavpack decoding 
                    os.remove(audio_file + ".wvc")

                tstart = time.time()
                fback = codec.decode(fresult)
                decode_time = time.time() - tstart

                raudio, sr = librosa.load(fback, sr=None)
                rsdb = spectro(raudio)
                rpsdb = weighted_spectro(raudio, sr)
                sdb_error = np.mean(np.abs(rsdb - sdb))
                psdb_error = np.mean(np.abs(rpsdb - psdb))
                print(", analyzed")

                series_results.append(dict(
                    codec=str(codec),
                    encode_time=encode_time,
                    decode_time=decode_time,
                    compression_ratio=result_size / asize,
                    spectrogram_error=float(sdb_error),
                    weighted_spectro_error=float(psdb_error)
                ))
            lossy_results[series] = series_results

        results[osp.basename(audio_file)] = {"lossless": lossless_results, "lossy": lossy_results}

    with open("result.json", "w") as jout:
        json.dump(results, jout)

def plot_results(result_path="result.json"):
    with open("result.json", "r") as jin:
        results = json.load(jin)

    for fname, fresults in results.items():
        # plot lossless results
        lossless_results = fresults["lossless"]
        fig, ax = plt.subplots(ncols=2, figsize=(16, 8))
        for series, slist in lossless_results.items():
            slist.sort(key=lambda item: item['compression_ratio'])
            codec_names = [item['codec'] for item in slist]
            encode_times = np.array([item['encode_time'] for item in slist])
            decode_times = np.array([item['decode_time'] for item in slist])
            cratio = np.array([item['compression_ratio'] for item in slist])

            # TODO: use different symbols for different series
            ax[0].plot(cratio, encode_times, label=series)
            ax[1].plot(cratio, decode_times, label=series)

            for idx, name in enumerate(codec_names):
                ax[0].text(cratio[idx], encode_times[idx], name, fontsize=10)
                ax[1].text(cratio[idx], decode_times[idx], name, fontsize=10)

        # plot lossy results
        ax[0].set(ylabel="encoding time (s)", xlabel="compression ratio", yscale='log',
            title="Encoding comparison for " + fname + " (x64)" if x64 else "")
        ax[0].grid(True)
        ax[0].legend()
        ax[1].set(ylabel="decoding time (s)", xlabel="compression ratio", yscale='log',
            title="Decoding comparison for " + fname + " (x64)" if x64 else "")
        ax[1].grid(True)
        ax[1].legend()
        fig.tight_layout()
        fig.savefig("figs/" + osp.basename(fname) + ".lossless.jpg")

        lossy_results = fresults["lossy"]
        fig, ax = plt.subplots(ncols=2, nrows=2, figsize=(16, 12))
        for series, slist in lossy_results.items():
            slist.sort(key=lambda item: item['compression_ratio'])
            codec_names = [item['codec'] for item in slist]
            encode_times = np.array([item['encode_time'] for item in slist])
            decode_times = np.array([item['decode_time'] for item in slist])
            sdb_err = np.array([item['spectrogram_error'] for item in slist])
            psdb_err = np.array([item['weighted_spectro_error'] for item in slist])
            cratio = np.array([item['compression_ratio'] for item in slist])

            # TODO: use different symbols for different series
            ax[0, 0].scatter(cratio, encode_times, label=series)
            ax[0, 1].scatter(cratio, decode_times, label=series)
            ax[1, 0].scatter(cratio, sdb_err, label=series)
            ax[1, 1].scatter(cratio, psdb_err, label=series)

            for idx, name in enumerate(codec_names):
                ax[0, 0].text(cratio[idx], encode_times[idx], name, fontsize=10)
                ax[0, 1].text(cratio[idx], decode_times[idx], name, fontsize=10)
                ax[1, 0].text(cratio[idx], sdb_err[idx], name, fontsize=10)
                ax[1, 1].text(cratio[idx], psdb_err[idx], name, fontsize=10)

        ax[0, 0].set(ylabel="encoding time (s)", xlabel="compression ratio")
        ax[0, 0].grid(True)
        ax[0, 0].legend()
        ax[0, 1].set(ylabel="decoding time (s)", xlabel="compression ratio")
        ax[0, 1].grid(True)
        ax[0, 1].legend()
        ax[1, 0].set(ylabel="spectrogram error (dB)", xlabel="compression ratio")
        ax[1, 0].grid(True)
        ax[1, 0].legend()
        ax[1, 1].set(ylabel="weighted spectrogram error (dB)", xlabel="compression ratio")
        ax[1, 1].grid(True)
        ax[1, 1].legend()
        fig.tight_layout()
        fig.savefig("figs/" + osp.basename(fname) + ".lossy.jpg")

        plt.show()

    # TODO: also output the markdown file table using HTML

if __name__ == "__main__":
    run_benchmark()
    plot_results()
