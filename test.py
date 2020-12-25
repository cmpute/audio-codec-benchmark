import json
import os
import os.path as osp
import time
from itertools import product

import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

from testlib import *

# some global configs
x64 = False
files = [
    "Bass_tek 2 - PLight.wav"
] # TODO: support hires files

# encoder paths
flac_path = './codecs/flac_x64.exe' if x64 else './codecs/flac.exe'
mac_path = "./codecs/MAC_x64.exe" if x64 else './codecs/MAC.exe'
wavpack_path = "./codecs/wavpack_x64.exe" if x64 else './codecs/wavpack.exe'
lame_path = './codecs/lame_x64.exe' if x64 else './codecs/lame.exe'
takc_path = './codecs/Takc.exe' if not x64 else None
tta_path = './codecs/tta_sse4_x64.exe' if x64 else './codecs/tta_sse4.exe'
wma_path = './codecs/WMAEncode_x64.exe' if x64 else './codecs/WMAEncode.exe'
lossywav_path = './codecs/lossyWAV_x64.exe' if x64 else './codecs/lossyWAV.exe'
refalac_path = './codecs/refalac_x64.exe' if x64 else './codecs/refalac.exe'
ofr_path = "./codecs/ofr_x64.exe" if x64 else './codecs/ofr.exe'
ofs_path = "./codecs/ofs_x64.exe" if x64 else './codecs/ofs.exe'

# lossless codes
flac_codecs = [flac(flac_path, '-' + str(c)) for c in range(8)]
ape_codecs = [mac(mac_path, '-c%d000' % c) for c in range(1, 6)]
wavpack_lossless_codecs = [wavpack(wavpack_path, a) for a in ['-f',None,'-h','-hh',['-h', '-x1'],['-hh', '-x3']]]
wavpack_lossless_hybrid_codecs = [wavpack(wavpack_path, ['-c', '-b192'] + a) for a in [['-f'],[],['-h'],['-hh']]]
tak_codecs = [takc(takc_path, ['-p'+str(p)+e, '-tn'+str(t)]) for p, e, t in product(range(5), ['', 'e', 'm'], [1, 4])] if not x64 else []
tta_codecs = [tta(tta_path, None)]
wma_lossless_codecs = [wmaencode(wma_path, ['-c', 'lsl'])]
lossyflac_codecs = [lossyflac(lossywav_path, flac_path, ['-q', q, '-C'], '-' + str(c)) for q, c in product(['I','H','S','X'], [1,4,7])]
lossytak_codecs = [lossytak(lossywav_path, takc_path, ['-q', q, '-C'], '-p' + str(p)) for q, p in product(['I','H','S','X'], ['2m'])]
lossywv_codecs = [lossywv(lossywav_path, wavpack_path, ['-q', q, '-C'], a) for q, a in product(['I','H','S','X'], ['-f',None,'-h'])]
alac_codecs = [refalac(refalac_path, None), refalac(refalac_path, "--fast")]
optimfrog_codecs = [ofr(ofr_path, ["--preset", str(p)]) for p in [0, 5, 10]]
# optimfrog_hybrid_codecs = [ofs(ofs_path, ["--quality", str(q), "--correction"]) for q in [0,2,6]] # always crashes and audio is not preserved

lossless_codecs = {
    # "optimFrog": optimfrog_codecs,
    # "flac": flac_codecs,
    # "ape": ape_codecs,
    # "wavpack": wavpack_lossless_codecs,
    # "wavpack(hybrid)": wavpack_lossless_hybrid_codecs,
    # "tak": tak_codecs,
    # "tta": tta_codecs,
    # "wma": wma_lossless_codecs,
    # "lossyflac(hybrid)": lossyflac_codecs,
    # "lossytak(hybrid)": lossytak_codecs,
    # "lossywv(hybrid)": lossywv_codecs,
    # "alac": alac_codecs,
}

# lossy codes
birates = [128, 160, 192, 256, 320]
wavpack_lossy_codecs = [wavpack(wavpack_path, ['-b' + str(b)]) for b in birates]
wavpack_lossless_hybrid_codecs = [wavpack(wavpack_path, ['-c', '-b' + str(b)]) for b in birates]
lame_cbr_codecs = [lame(lame_path, ['-b' + str(b), '-q' + str(q)]) for b, q in product(birates, [2, 7])] # note: CBR <= 96kbps leads to downsampling
lame_vbr_codecs = [lame(lame_path, ['-V' + str(v), '-q' + str(q)]) for v, q in product(range(7), [2, 7])] # note: VBR <= V7 leads to downsampling
wma_lossy_cbr_codecs = [wmaencode(wma_path, ['-c', 'pro', '-m', m, '-b', str(b)]) for m, b in product(['cbr', 'cbr2pass'], [128,160,192,256,384,440])]
wma_lossy_vbr_codecs = [wmaencode(wma_path, ['-c', 'pro', '-m', m, '-q', str(q)]) for m, q in product(['vbr', 'vbr2pass'], [10,25,50,75,90,98])]
optimfrog_hybrid_codecs = [ofs(ofs_path, ["--quality", str(q)]) for q in [0,2,6]]

lossy_codecs = {
    "optimFrog": optimfrog_hybrid_codecs,
    # "mp3(CBR)": lame_cbr_codecs,
    # "mp3(VBR)": lame_vbr_codecs,
    # "wavpack": wavpack_lossy_codecs + wavpack_lossless_hybrid_codecs,
    # "wma(CBR)": wma_lossy_cbr_codecs,
    # "wma(VBR)": wma_lossy_vbr_codecs
}

def run_benchmark(save_spectrogram=True):
    results = {}
    for audio_file in files:
        print("> ----- Testing with", audio_file, "-----")
        asize = osp.getsize(audio_file)

        # load audio and calculate spectrogram
        audio, sr = librosa.load(audio_file, sr=None)
        ahash = array_hash(audio)
        sdb, spower = spectro(audio)
        psdb, pspower = weighted_spectro(audio, sr)

        if save_spectrogram:
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

                if "hybrid" in series: # for hybrid mode
                    if "wavpack" in series:
                        result_size = osp.getsize(fresult) + osp.getsize(fresult.replace(".wv", ".wvc"))
                    elif "lossy" in series:
                        result_size = osp.getsize(fresult) + osp.getsize(fresult.replace(".lossy", ".lwcdf"))
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

                tstart = time.time()
                fback = codec.decode(fresult)
                decode_time = time.time() - tstart

                raudio, sr = librosa.load(fback, sr=None)
                if 'wma' in series: # pad files generated by ffmpeg
                    raudio = pad_to(raudio, audio)
                rsdb, rspower = spectro(raudio)
                rpsdb, rpspower = weighted_spectro(raudio, sr)
                sdb_error = np.abs(rsdb - sdb)
                psdb_error = np.abs(rpsdb - psdb)
                sdb_snr = signal_to_noise(spower, rspower)
                psdb_snr = signal_to_noise(pspower, rpspower)
                print(", analyzed")

                series_results.append(dict(
                    codec=str(codec),
                    encode_time=encode_time,
                    decode_time=decode_time,
                    compression_ratio=result_size / asize,
                    spectrogram_error=float(np.mean(sdb_error)),
                    weighted_spectro_error=float(np.mean(psdb_error)),
                    snr=float(sdb_snr),
                    weighted_snr=float(psdb_snr)
                ))
            lossy_results[series] = series_results

        results[osp.basename(audio_file)] = {"lossless": lossless_results, "lossy": lossy_results}

    with open("result.json", "w") as jout:
        json.dump(results, jout)

markers = [".","o","v","^","<",">","1","2","3","4","8","s","p","P","*","h","H","+","x","X","D","d","|","_"]

def plot_results(result_path="result.json", tag_points=True):
    # TODO: only plot contour points for a series
    with open("result.json", "r") as jin:
        results = json.load(jin)

    for fname, fresults in results.items():
        # plot lossless results
        lossless_results = fresults["lossless"]
        fig, ax = plt.subplots(ncols=2, figsize=(16, 8))
        for sidx, (series, slist) in enumerate(lossless_results.items()):
            slist.sort(key=lambda item: item['compression_ratio'])
            codec_names = [item['codec'] for item in slist]
            encode_times = np.array([item['encode_time'] for item in slist])
            decode_times = np.array([item['decode_time'] for item in slist])
            cratio = np.array([item['compression_ratio'] for item in slist])

            contour = contour_points(cratio, encode_times, "sw")
            ax[0].plot(cratio[contour], encode_times[contour], label=series, marker=markers[sidx])
            if tag_points:
                for idx in contour:
                    ax[0].text(cratio[idx], encode_times[idx], codec_names[idx], fontsize=10)

            contour = contour_points(cratio, decode_times, "sw")
            ax[1].plot(cratio[contour], decode_times[contour], label=series, marker=markers[sidx])
            if tag_points:
                for idx in contour:
                    ax[1].text(cratio[idx], decode_times[idx], codec_names[idx], fontsize=10)

        # plot lossy results
        ax[0].set(ylabel="encoding time (s)", xlabel="compressed size ratio", yscale='log')
        ax[0].grid(True)
        ax[0].legend()
        ax[1].set(ylabel="decoding time (s)", xlabel="compressed size ratio", yscale='log')
        ax[1].grid(True)
        ax[1].legend()
        fig.tight_layout()
        fig.savefig("figs/" + osp.basename(fname) + (".lossless_x64.jpg" if x64 else ".lossless.jpg"))

        lossy_results = fresults["lossy"]
        fig, ax = plt.subplots(ncols=2, figsize=(16, 8))
        fig_err, ax_err = plt.subplots(ncols=2, nrows=2, figsize=(16, 12))
        for sidx, (series, slist) in enumerate(lossy_results.items()):
            slist.sort(key=lambda item: item['compression_ratio'])
            codec_names = [item['codec'] for item in slist]
            encode_times = np.array([item['encode_time'] for item in slist])
            decode_times = np.array([item['decode_time'] for item in slist])
            sdb_err = np.array([item['spectrogram_error'] for item in slist])
            psdb_err = np.array([item['weighted_spectro_error'] for item in slist])
            sdb_snr = np.array([item['snr'] for item in slist])
            psdb_snr = np.array([item['weighted_snr'] for item in slist])
            cratio = np.array([item['compression_ratio'] for item in slist])

            # TODO: encoding times vs cratio seems to be linear with lossy codecs
            contour = contour_points(cratio, encode_times, "sw")
            ax[0].plot(cratio[contour], encode_times[contour], label=series, marker=markers[sidx])
            if tag_points:
                for idx in contour:
                    ax[0].text(cratio[idx], encode_times[idx], codec_names[idx], fontsize=10)

            contour = contour_points(cratio, decode_times, "sw")
            ax[1].plot(cratio[contour], decode_times[contour], label=series, marker=markers[sidx])
            if tag_points:
                for idx in contour:
                    ax[1].text(cratio[idx], decode_times[idx], codec_names[idx], fontsize=10)

            contour = contour_points(cratio, sdb_err, "sw")
            ax_err[0, 0].plot(cratio[contour], sdb_err[contour], label=series, marker=markers[sidx])
            if tag_points:
                for idx in contour:
                    ax_err[0, 0].text(cratio[idx], sdb_err[idx], codec_names[idx], fontsize=10)

            contour = contour_points(cratio, psdb_err, "sw")
            ax_err[0, 1].plot(cratio[contour], psdb_err[contour], label=series, marker=markers[sidx])
            if tag_points:
                for idx in contour:
                    ax_err[0, 1].text(cratio[idx], psdb_err[idx], codec_names[idx], fontsize=10)

            contour = contour_points(cratio, sdb_snr, "nw")
            ax_err[1, 0].plot(cratio[contour], sdb_snr[contour], label=series, marker=markers[sidx])
            if tag_points:
                for idx in contour:
                    ax_err[1, 0].text(cratio[idx], sdb_snr[idx], codec_names[idx], fontsize=10)

            contour = contour_points(cratio, psdb_snr, "nw")
            ax_err[1, 1].plot(cratio[contour], psdb_snr[contour], label=series, marker=markers[sidx])
            if tag_points:
                for idx in contour:
                    ax_err[1, 1].text(cratio[idx], psdb_snr[idx], codec_names[idx], fontsize=10)

        ax[0].set(ylabel="encoding time (s)", xlabel="compressed size ratio")
        ax[0].grid(True)
        ax[0].legend()
        ax[1].set(ylabel="decoding time (s)", xlabel="compressed size ratio")
        ax[1].grid(True)
        ax[1].legend()
        ax_err[0, 0].set(ylabel="spectrogram error (dB)", xlabel="compressed size ratio")
        ax_err[0, 0].grid(True)
        ax_err[0, 0].legend()
        ax_err[0, 1].set(ylabel="weighted spectrogram error (dB)", xlabel="compressed size ratio")
        ax_err[0, 1].grid(True)
        ax_err[0, 1].legend()
        ax_err[1, 0].set(ylabel="signal-to-noise ratio (db)", xlabel="compressed size ratio")
        ax_err[1, 0].grid(True)
        ax_err[1, 0].legend()
        ax_err[1, 1].set(ylabel="weighted signal-to-noise ratio (dB)", xlabel="compressed size ratio")
        ax_err[1, 1].grid(True)
        ax_err[1, 1].legend()
        fig.tight_layout()
        fig_err.tight_layout()
        fig.savefig("figs/" + osp.basename(fname) + (".lossy_x64.jpg" if x64 else ".lossy.jpg"))
        fig_err.savefig("figs/" + osp.basename(fname) + (".lossy_err_x64.jpg" if x64 else ".lossy_err.jpg"))

        plt.show()

    # TODO: also output the markdown file table using HTML

if __name__ == "__main__":
    run_benchmark()
    plot_results()
