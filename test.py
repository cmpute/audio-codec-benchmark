import json
import os
import os.path as osp
import time
import wave
from itertools import product

import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

from testlib import *

# some global configs
x64 = False # <---- Change to x64 codec implementations
files = [ # <---- Put your audio files in here (need .wav format)
    "PLight - Bass_tek 2.wav",
    "久石让 - あの夏へ.wav",
    "Aimer - Ref_rain.wav",
    "John Powell & Hans Zimmer - Hero.wav",
]

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
opus_path = "./codecs/opusenc.exe" if not x64 else None
ogg_path = "./codecs/oggenc2_x64.exe" if x64 else "./codecs/oggenc2.exe"
neroaac_path = "./codecs/neroAacEnc.exe" if not x64 else None
qaac_path = "./codecs/qaac_x64/qaac64.exe" if x64 else "./codecs/qaac/qaac.exe"
mpc_path = "./codecs/mpcenc_x64.exe" if x64 else "./codecs/mpcenc.exe"

# lossless codes
flac_codecs = [flac(flac_path, '-' + str(c)) for c in range(8)]
ape_codecs = [mac(mac_path, '-c%d000' % c) for c in range(1, 6)]
wavpack_lossless_codecs = [wavpack(wavpack_path, a) for a in ['-f',None,'-h','-hh',['-h', '-x1'],['-hh', '-x3']]]
wavpack_lossless_hybrid_codecs = [wavpack(wavpack_path, ['-c', '-b192'] + a) for a in [['-f'],[],['-h'],['-hh']]]
tak_codecs = [takc(takc_path, ['-p'+str(p)+e, '-tn'+str(t)]) for p, e, t in product(range(5), ['', 'e', 'm'], [1, 4])] if not x64 else []
tta_codecs = [tta(tta_path, None)]
wma_lossless_codecs = [wmaencode(wma_path, ['-c', 'lsl'])]
lossyflac_codecs = [lossyflac(lossywav_path, flac_path, ['-q', q, '-C'], '-' + str(c)) for q, c in product(['I','H','S','X'], [1,4,7])]
lossytak_codecs = [lossytak(lossywav_path, takc_path, ['-q', q, '-C'], '-p' + str(p)) for q, p in product(['I','H','S','X'], ['2m'])] if not x64 else []
lossywv_codecs = [lossywv(lossywav_path, wavpack_path, ['-q', q, '-C'], a) for q, a in product(['I','H','S','X'], ['-f',None,'-h'])]
alac_codecs = [refalac(refalac_path, None), refalac(refalac_path, "--fast")]
optimfrog_codecs = [ofr(ofr_path, ["--preset", str(p)]) for p in [0, 5, 10]]
# optimfrog_hybrid_codecs = [ofs(ofs_path, ["--quality", str(q), "--correction"]) for q in [0,2,6]] # always crashes and audio is not preserved

lossless_codecs = {
    "optimFrog": optimfrog_codecs,

    "flac": flac_codecs,
    "ape": ape_codecs,
    "wavpack": wavpack_lossless_codecs,
    "wavpack(hybrid)": wavpack_lossless_hybrid_codecs,
    "tak": tak_codecs,
    "tta": tta_codecs,
    "wma": wma_lossless_codecs,
    "lossyflac(hybrid)": lossyflac_codecs,
    "lossytak(hybrid)": lossytak_codecs,
    "lossywv(hybrid)": lossywv_codecs,
    "alac": alac_codecs,
}

# lossy codes
birates = [128, 160, 192, 256, 320]
wavpack_lossy_codecs = [wavpack(wavpack_path, ['-b' + str(b)]) for b in birates]
lame_cbr_codecs = [lame(lame_path, ['-b' + str(b), '-q' + str(q)]) for b, q in product(birates, [2, 7])] # note: CBR <= 96kbps leads to downsampling
lame_vbr_codecs = [lame(lame_path, ['-V' + str(v), '-q' + str(q)]) for v, q in product(range(7), [2, 7])] # note: VBR <= V7 leads to downsampling
wma_lossy_cbr_codecs = [wmaencode(wma_path, ['-c', 'pro', '-m', m, '-b', str(b)]) for m, b in product(['cbr', 'cbr2pass'], [128,160,192,256,384,440])]
wma_lossy_vbr_codecs = [wmaencode(wma_path, ['-c', 'pro', '-m', m, '-q', str(q)]) for m, q in product(['vbr', 'vbr2pass'], [10,25,50,75,90,98])]
optimfrog_lossy_codecs = [ofs(ofs_path, ["--quality", str(q)]) for q in [0,2,6]]
opus_codecs = [opus(opus_path, ["--bitrate", str(b//2)]) for b in birates] if not x64 else []
lossyflac_codecs = [lossyflac(lossywav_path, flac_path, ['-q', q], '-' + str(c)) for q, c in product(['I','H','S','X'], [1,4,7])]
lossytak_codecs = [lossytak(lossywav_path, takc_path, ['-q', q], '-p' + str(p)) for q, p in product(['I','H','S','X'], ['2m'])] if not x64 else []
lossywv_codecs = [lossywv(lossywav_path, wavpack_path, ['-q', q], a) for q, a in product(['I','H','S','X'], ['-f',None,'-h'])]
aac_vbr_codecs = ([neroaac(neroaac_path, ['-q', str(q)]) for q in [0.1, 0.3, 0.5, 0.7, 0.9]] if not x64 else []) \
    + [qaac(qaac_path, ['-V', str(v)]) for v in [31, 63, 95]]
aac_cbr_codecs = ([neroaac(neroaac_path, ['-cbr', str(c)]) for c in birates] if not x64 else []) \
    + [qaac(qaac_path, ['-c', str(c)]) for c in birates]
vorbis_codecs = [oggenc(ogg_path, ['-q', str(q)]) for q in [2, 7, 10]]
musepack_codecs = [mpc(mpc_path, q) for q in ["--standard", "--extreme", "--insane"]]

lossy_codecs = {
    # "optimFrog": optimfrog_lossy_codecs,

    "mp3(CBR)": lame_cbr_codecs,
    "mp3(VBR)": lame_vbr_codecs,
    "wavpack": wavpack_lossy_codecs,
    "wma(CBR)": wma_lossy_cbr_codecs,
    "wma(VBR)": wma_lossy_vbr_codecs,
    "opus": opus_codecs,
    "lossyflac": lossyflac_codecs,
    "lossytak": lossytak_codecs,
    "lossywv": lossywv_codecs,
    "aac(VBR)": aac_vbr_codecs,
    "aac(CBR)": aac_cbr_codecs,
    "vorbis": vorbis_codecs,
    "musepack": musepack_codecs,
}

def run_benchmark(save_spectrogram=True):
    results = {}
    for audio_file in files:
        print("> ----- Testing with", audio_file, "-----")
        # load audio metadata
        asize = osp.getsize(audio_file)
        afile = wave.open(audio_file)
        ameta = dict(
            nchannels=afile.getnchannels(),
            sample_width=afile.getsampwidth() * 8,
            frame_rate=afile.getframerate(),
            nframes=afile.getnframes()
        )

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
                
                # encode
                tstart = time.time()
                fresult = codec.encode(audio_file)
                encode_time = time.time() - tstart

                # get compressed size
                result_size = osp.getsize(fresult)

                # decode
                tstart = time.time()
                fback = codec.decode(fresult)
                decode_time = time.time() - tstart

                # calculate performance metrics
                raudio, sr = librosa.load(fback, sr=None)
                if 'wma' in series or 'vorbis' in series: # pad files generated by ffmpeg
                    raudio = librosa.util.fix_length(raudio, size=len(audio))
                rsdb, rspower = spectro(raudio)
                rpsdb, rpspower = weighted_spectro(raudio, sr)
                sdb_error = np.abs(rsdb - sdb)
                psdb_error = np.abs(rpsdb - psdb)
                sdb_snr = signal_to_noise(spower, rspower)
                psdb_snr = signal_to_noise(pspower, rpspower)
                print(", analyzed")

                # save results
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

        results[osp.basename(audio_file)] = {"lossless": lossless_results, "lossy": lossy_results, "metadata": ameta}

    with open("result.json", "w") as jout:
        json.dump(results, jout)

markers = [".","o","v","^","<",">","1","2","3","4","8","s","p","P","*","h","H","+","x","X","D","d","|","_"]

def plot_results(result_path="result.json", tag_points=True, bitrate_as_x=False):
    with open("result.json", "r") as jin:
        results = json.load(jin)

    for fname, fresults in results.items():
        raw_bitrate = fresults["metadata"]["nchannels"] * fresults["metadata"]["sample_width"]\
            * fresults["metadata"]["frame_rate"] / 1000
        xlabel = "average bitrate (kbps)" if bitrate_as_x else "compressed size ratio"
        fbasename = "figs/" + osp.basename(fname).replace(' ', '_')

        # plot lossless results
        lossless_results = fresults["lossless"]
        fig, ax = plt.subplots(ncols=2, figsize=(16, 8))
        for sidx, (series, slist) in enumerate(lossless_results.items()):
            slist.sort(key=lambda item: item['compression_ratio'])
            codec_names = [item['codec'] for item in slist]
            encode_times = np.array([item['encode_time'] for item in slist])
            decode_times = np.array([item['decode_time'] for item in slist])
            cratio = np.array([item['compression_ratio'] for item in slist])

            if bitrate_as_x:
                xvalue = cratio * raw_bitrate
            else:
                xvalue = cratio
            contour = contour_points(xvalue, encode_times, -0.6*np.pi)
            ax[0].plot(xvalue[contour], encode_times[contour], label=series, marker=markers[sidx])
            if tag_points:
                for idx in contour:
                    ax[0].text(xvalue[idx], encode_times[idx], codec_names[idx], fontsize=10)

            contour = contour_points(xvalue, decode_times, -0.6*np.pi)
            ax[1].plot(xvalue[contour], decode_times[contour], label=series, marker=markers[sidx])
            if tag_points:
                for idx in contour:
                    ax[1].text(xvalue[idx], decode_times[idx], codec_names[idx], fontsize=10)

        # plot lossy results
        ax[0].set(ylabel="encoding time (s)", xlabel=xlabel, yscale='log')
        ax[0].grid(True)
        ax[0].legend()
        ax[1].set(ylabel="decoding time (s)", xlabel=xlabel, yscale='log')
        ax[1].grid(True)
        ax[1].legend()
        fig.tight_layout()
        fig.savefig(fbasename + (".lossless_x64.jpg" if x64 else ".lossless.jpg"))

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
            if bitrate_as_x:
                xvalue = cratio * raw_bitrate
            else:
                xvalue = cratio
            contour = contour_points(xvalue, encode_times, "sw")
            ax[0].plot(xvalue[contour], encode_times[contour], label=series, marker=markers[sidx])
            if tag_points:
                for idx in contour:
                    ax[0].text(xvalue[idx], encode_times[idx], codec_names[idx], fontsize=10)

            contour = contour_points(xvalue, decode_times, "sw")
            ax[1].plot(xvalue[contour], decode_times[contour], label=series, marker=markers[sidx])
            if tag_points:
                for idx in contour:
                    ax[1].text(xvalue[idx], decode_times[idx], codec_names[idx], fontsize=10)

            contour = contour_points(xvalue, sdb_err, "sw")
            ax_err[0, 0].plot(xvalue[contour], sdb_err[contour], label=series, marker=markers[sidx])
            if tag_points:
                for idx in contour:
                    ax_err[0, 0].text(xvalue[idx], sdb_err[idx], codec_names[idx], fontsize=10)

            contour = contour_points(xvalue, psdb_err, "sw")
            ax_err[0, 1].plot(xvalue[contour], psdb_err[contour], label=series, marker=markers[sidx])
            if tag_points:
                for idx in contour:
                    ax_err[0, 1].text(xvalue[idx], psdb_err[idx], codec_names[idx], fontsize=10)

            contour = contour_points(xvalue, sdb_snr, "nw")
            ax_err[1, 0].plot(xvalue[contour], sdb_snr[contour], label=series, marker=markers[sidx])
            if tag_points:
                for idx in contour:
                    ax_err[1, 0].text(xvalue[idx], sdb_snr[idx], codec_names[idx], fontsize=10)

            contour = contour_points(xvalue, psdb_snr, "nw")
            ax_err[1, 1].plot(xvalue[contour], psdb_snr[contour], label=series, marker=markers[sidx])
            if tag_points:
                for idx in contour:
                    ax_err[1, 1].text(xvalue[idx], psdb_snr[idx], codec_names[idx], fontsize=10)

        ax[0].set(ylabel="encoding time (s)", xlabel=xlabel)
        ax[0].grid(True)
        ax[0].legend()
        ax[1].set(ylabel="decoding time (s)", xlabel=xlabel)
        ax[1].grid(True)
        ax[1].legend()
        ax_err[0, 0].set(ylabel="spectrogram error (dB)", xlabel=xlabel)
        ax_err[0, 0].grid(True)
        ax_err[0, 0].legend()
        ax_err[0, 1].set(ylabel="weighted spectrogram error (dB)", xlabel=xlabel)
        ax_err[0, 1].grid(True)
        ax_err[0, 1].legend()
        ax_err[1, 0].set(ylabel="signal-to-noise ratio (db)", xlabel=xlabel)
        ax_err[1, 0].grid(True)
        ax_err[1, 0].legend()
        ax_err[1, 1].set(ylabel="weighted signal-to-noise ratio (dB)", xlabel=xlabel)
        ax_err[1, 1].grid(True)
        ax_err[1, 1].legend()
        fig.tight_layout()
        fig_err.tight_layout()
        fig.savefig(fbasename + (".lossy_x64.jpg" if x64 else ".lossy.jpg"))
        fig_err.savefig(fbasename + (".lossy_err_x64.jpg" if x64 else ".lossy_err.jpg"))

        plt.show()

def save_table(result_path="result.json"):
    with open("result.json", "r") as jin:
        results = json.load(jin)
    if x64:
        fmd = open("result_x64.md", "w")
    else:
        fmd = open("result.md", "w")

    fmd.write('''# Criteria
- *Compression Ratio (CR)*: compressed file size / original uncompressed file size (lower the better)
- *Spectrogram Error*: direct difference between power spectrograms (lower the better)
- *Weighted Spectrogram Error*: direct difference between A-weighted power spectrograms (lower the better)
- *Signal-to-Noise Ratio (SNR)*: noise is calculated from signal power difference (higher the better)
- *Weighted SNR*: noise is calculated from A-weighted signal power difference (higher the better)
''')
    for fname, fresults in results.items():
        fmd.write("# Results for `%s`\n" % fname)
        fmd.write("Audio Format: %dch, %d-bit, %d Hz, %d samples\n" % (
            fresults["metadata"]["nchannels"],
            fresults["metadata"]["sample_width"],
            fresults["metadata"]["frame_rate"],
            fresults["metadata"]["nframes"]
        ))
        fmd.write('<table><tr><th rowspan="2">Format</th><th rowspan="2">Codec</th><th rowspan="2">Compression Ratio (%)</th><th rowspan="2">Encoding time (s)</th><th rowspan="2">Decoding time (s)</th><th colspan="2">Spectrogram Error (db)</th><th colspan="2">Signal-to-Noise Ratio (db)</th></tr>\n')
        fmd.write('<tr><th>linear</th><th>weighted</th><th>linear</th><th>weighted</th></tr>\n')

        # plot lossless results
        fmd.write('<tr><td colspan="9" style="text-align:center"> Lossless Codecs </td></tr>\n')
        lossless_results = fresults["lossless"]
        for series, slist in lossless_results.items():
            fmd.write('<tr><td rowspan="%d">%s</td>' % (len(slist), series))
            for idx, item in enumerate(slist):
                if idx != 0:
                    fmd.write('<tr>')
                fmd.write('<td>%s</td>' % item['codec'])
                fmd.write('<td>%.3f</td>' % (item['compression_ratio'] * 100))
                fmd.write('<td>%.3f</td>' % item['encode_time'])
                fmd.write('<td>%.3f</td>' % item['decode_time'])
                fmd.write('<td>-</td><td>-</td><td>-</td><td>-</td>')
                fmd.write('</tr>\n')

        # plot lossy results
        fmd.write('<tr><td colspan="9" style="text-align:center"> Lossy Codecs </td></tr>')
        lossy_results = fresults["lossy"]
        for series, slist in lossy_results.items():
            fmd.write('<tr><td rowspan="%d">%s</td>' % (len(slist), series))
            for idx, item in enumerate(slist):
                if idx != 0:
                    fmd.write('<tr>')
                fmd.write('<td>%s</td>' % item['codec'])
                fmd.write('<td>%.3f</td>' % (item['compression_ratio'] * 100))
                fmd.write('<td>%.3f</td>' % item['encode_time'])
                fmd.write('<td>%.3f</td>' % item['decode_time'])
                fmd.write('<td>%.3f</td>' % item['spectrogram_error'])
                fmd.write('<td>%.3f</td>' % item['weighted_spectro_error'])
                fmd.write('<td>%.3f</td>' % item['snr'])
                fmd.write('<td>%.3f</td>' % item['weighted_snr'])
                fmd.write('</tr>\n')

        fmd.write('</table>\n\n')

    fmd.close()

if __name__ == "__main__":
    run_benchmark()
    save_table()
    plot_results()
    # plot_results(tag_points=False, bitrate_as_x=True)
