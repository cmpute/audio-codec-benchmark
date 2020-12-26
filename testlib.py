import os
import os.path as osp
from hashlib import sha1
from subprocess import DEVNULL, call, check_call

import librosa
import numpy as np
from scipy.spatial import ConvexHull

cqt_fmin = librosa.note_to_hz('A1')
ffmpeg_path = './codecs/ffmpeg.exe'

class Codec: # TODO: add flag indicating whether supporting hires files
    def __init__(self, path, cmd_args):
        '''
        path: path to the codec binary
        cmd_args: (extr) command line args for encoding, used for adjusting compression level
        '''
        self.path = osp.abspath(path)
        if cmd_args is None:
            self.cmd_args = []
        elif isinstance(cmd_args, (list, tuple)):
            self.cmd_args = list(cmd_args)
        else:
            self.cmd_args = [cmd_args]

    def encode(self, fin):
        pass

    def decode(self, fin):
        pass

    def __str__(self):
        if self.cmd_args:
            return f"{self.__class__.__name__} ({' '.join(self.cmd_args)})"
        else:
            return f"{self.__class__.__name__} (default)"

class flac(Codec):
    def __init__(self, path, cmd_args, keep_meta=False):
        super().__init__(path, cmd_args)
        self.extra_args = ['--keep-foreign-metadata'] if keep_meta else []

    def encode(self, fin):
        fout = fin + ".flac"
        check_call([self.path, fin, "-sf", "-o", fout] + self.cmd_args + self.extra_args, stdout=DEVNULL, stderr=DEVNULL)
        return fout

    def decode(self, fin):
        fout = fin + ".wav"
        check_call([self.path, fin, "-sfd", "-o", fout] + self.extra_args, stdout=DEVNULL, stderr=DEVNULL)
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
        wvunpack = self.path.replace("wavpack", "wvunpack")
        check_call([wvunpack, '-y', fin, fout], stdout=DEVNULL, stderr=DEVNULL)
        if osp.exists(fin.replace(".wv", ".wvc")):
            os.remove(fin.replace(".wv", ".wvc"))
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

class takc(Codec):
    def __init__(self, path, cmd_args):
        super().__init__(path, cmd_args)

    def encode(self, fin):
        fout = fin + ".tak"
        check_call([self.path, "-e", "-silent", "-overwrite"] + self.cmd_args + [fin, fout])
        return fout

    def decode(self, fin):
        fout = fin + ".wav"
        check_call([self.path, "-d", "-silent", "-overwrite", fin, fout])
        return fout

class tta(Codec):
    def __init__(self, path, cmd_args):
        super().__init__(path, cmd_args)

    def encode(self, fin):
        fout = fin + ".tta"
        check_call([self.path, "-e"] + self.cmd_args + [fin, fout], stdout=DEVNULL, stderr=DEVNULL)
        return fout

    def decode(self, fin):
        fout = fin + ".wav"
        check_call([self.path, "-d", fin, fout], stdout=DEVNULL, stderr=DEVNULL)
        return fout

class wmaencode(Codec):
    def __init__(self, path, cmd_args):
        super().__init__(path, cmd_args)

    def encode(self, fin):
        fout = fin + ".wma"
        check_call([self.path, fin, fout, "-s"] + self.cmd_args)
        return fout

    def decode(self, fin):
        fout = fin + ".wav"
        check_call([ffmpeg_path, "-y", "-i", fin, fout], stdout=DEVNULL, stderr=DEVNULL)
        return fout

class lossywav(Codec): # Pipeline mode is not working, so intermediate files are saved
    def __init__(self, path, base_codec, cmd_args):
        super().__init__(path, cmd_args)
        self.base_codec = base_codec

    def encode(self, fin):
        lossy_out = fin.replace(".wav", ".lossy.wav")
        lwcdf_out = fin.replace(".wav", ".lwcdf.wav")
        check_call([self.path, fin, '-f', '-S'] + self.cmd_args)
        lossy_encoded = self.base_codec.encode(lossy_out)
        if osp.exists(lwcdf_out):
            self.base_codec.encode(lwcdf_out)
            os.remove(lwcdf_out)
        return lossy_encoded

    def decode(self, fin):
        correction_fin = fin.replace('.lossy', '.lwcdf')
        if osp.exists(correction_fin): # hybrid mode
            lossy_out = self.base_codec.decode(fin)
            lwcdf_out = self.base_codec.decode(correction_fin)
            lossy_fname = lossy_out.replace("lossy.wav", "hybrid").rstrip("wav") + "lossy.wav"
            lwcdf_fname = lwcdf_out.replace("lwcdf.wav", "hybrid").rstrip("wav") + "lwcdf.wav"
            if osp.exists(lossy_fname):
                os.remove(lossy_fname)
            if osp.exists(lwcdf_fname):
                os.remove(lwcdf_fname)
            os.remove(correction_fin) # prevent conflict with lossy results
            os.rename(lossy_out, lossy_fname)
            os.rename(lwcdf_out, lwcdf_fname)
            check_call([self.path, lossy_fname, '-M', '-f', '-S'], stdout=DEVNULL, stderr=DEVNULL)
            return lossy_out.replace("lossy.wav", "hybrid")
        else:
            lossy_out = self.base_codec.decode(fin)
            return lossy_out

class lossyflac(lossywav):
    def __init__(self, lossywav_path, flac_path, lossywav_args, flac_args):
        self.flac_codec = flac(flac_path, flac_args, keep_meta=True)
        self.flac_codec.cmd_args += ['-b', '512']
        super().__init__(lossywav_path, self.flac_codec, lossywav_args)

    def __str__(self):
        return f"lossyflac ({' '.join(self.cmd_args)}|{' '.join(self.flac_codec.cmd_args[:-2])})"

class lossytak(lossywav):
    def __init__(self, lossywav_path, tak_path, lossywav_args, tak_args):
        self.tak_codec = takc(tak_path, tak_args)
        self.tak_codec.cmd_args += ['-fsl512']
        super().__init__(lossywav_path, self.tak_codec, lossywav_args)

    def __str__(self):
        return f"lossytak ({' '.join(self.cmd_args)}|{' '.join(self.tak_codec.cmd_args[:-1])})"

class lossywv(lossywav):
    def __init__(self, lossywav_path, wavpack_path, lossywav_args, wavpack_args):
        self.wavpack_codec = wavpack(wavpack_path, wavpack_args)
        self.wavpack_codec.cmd_args += ['--blocksize=512', '--merge-blocks']
        super().__init__(lossywav_path, self.wavpack_codec, lossywav_args)

    def __str__(self):
        return f"lossywv ({' '.join(self.cmd_args)}|{' '.join(self.wavpack_codec.cmd_args[:-2])})"

class lossywmalsl(lossywav):
    def __init__(self, lossywav_path, wma_path, lossywav_args):
        self.wma_codec = wmaencode(wma_path, ['-c', 'lsl'])
        super().__init__(lossywav_path, self.wma_codec, lossywav_args)

    def decode(self, fin):
        correction_fin = fin.replace('.lossy', '.lwcdf')
        if osp.exists(correction_fin):
            raise RuntimeError("WMA decoding is currently not robustly handled, decoding lossyWMALSL with correction is not supported yet!")
        else:
            lossy_out = self.base_codec.decode(fin)
            return lossy_out

    def __str__(self):
        return f"lossywmalsl ({' '.join(self.cmd_args)})"

class refalac(Codec):
    def __init__(self, path, cmd_args):
        super().__init__(path, cmd_args)

    def encode(self, fin):
        fout = fin + ".m4a"
        check_call([self.path, fin, "-o", fout, "-s"] + self.cmd_args)
        return fout

    def decode(self, fin):
        fout = fin + ".wav"
        check_call([self.path, fin, "-o", fout, "-s", "-D"])
        return fout

class ofr(Codec): # OptimFrog
    def __init__(self, path, cmd_args):
        super().__init__(path, cmd_args)

    def encode(self, fin):
        fout = fin + ".ofr"
        call([self.path, "--encode", "--silent", "--overwrite"] + self.cmd_args + [fin, "--output", fout])
        return fout

    def decode(self, fin):
        fout = fin + ".wav"
        call([self.path, "--decode", "--silent", "--overwrite", fin, "--output", fout])
        return fout

class ofs(Codec): # OptimFrog Dual Stream
    def __init__(self, path, cmd_args):
        super().__init__(path, cmd_args)

    def encode(self, fin):
        fout = fin + ".ofs"
        call([self.path, "--encode", "--silent", "--overwrite"] + self.cmd_args + [fin, "--output", fout])
        return fout

    def decode(self, fin):
        fout = fin + ".wav"
        if osp.exists(fin.replace(".ofs", ".ofc")):
            call([self.path, "--decode", "--silent", "--overwrite", "--correction", fin, "--output", fout])
            os.remove(fin.replace(".ofs", ".ofc"))
        else:
            call([self.path, "--decode", "--silent", "--overwrite", fin, "--output", fout])
        return fout

class opus(Codec):
    def __init__(self, path, cmd_args):
        super().__init__(path, cmd_args)

    def encode(self, fin):
        fout = fin + ".opus"
        call([self.path, "--quiet"] + self.cmd_args + [fin, fout])
        return fout

    def decode(self, fin):
        fout = fin + ".wav"
        decoder = self.path.replace("opusenc", "opusdec")
        call([decoder, "--quiet", fin, fout])
        return fout

class oggenc(Codec):
    def __init__(self, path, cmd_args):
        super().__init__(path, cmd_args)

    def encode(self, fin):
        fout = fin + ".ogg"
        check_call([self.path, fin, "-o", fout, "-Q"] + self.cmd_args)
        return fout

    def decode(self, fin):
        fout = fin + ".wav"
        check_call([ffmpeg_path, "-y", "-i", fin, fout], stdout=DEVNULL, stderr=DEVNULL)
        return fout

class neroaac(Codec):
    def __init__(self, path, cmd_args):
        super().__init__(path, cmd_args)

    def encode(self, fin):
        fout = fin + ".m4a"
        check_call([self.path, "-if", fin, "-of", fout] + self.cmd_args, stdout=DEVNULL, stderr=DEVNULL)
        return fout

    def decode(self, fin):
        fout = fin + ".wav"
        decoder = self.path.replace("neroAacEnc", "neroAacDec")
        check_call([decoder, "-if", fin, "-of", fout], stdout=DEVNULL, stderr=DEVNULL)
        return fout

class qaac(Codec):
    def __init__(self, path, cmd_args):
        super().__init__(path, cmd_args)

    def encode(self, fin):
        fout = fin + ".m4a"
        check_call([self.path, "-o", fout, "-s"] + self.cmd_args + [fin])
        return fout

    def decode(self, fin):
        fout = fin + ".wav"
        check_call([self.path, "-o", fout, "-s", "-D", fin], stdout=DEVNULL, stderr=DEVNULL)
        return fout

class mpc(Codec):
    def __init__(self, path, cmd_args):
        super().__init__(path, cmd_args)

    def encode(self, fin):
        fout = fin + ".mpc"
        call([self.path, "--silent", "--overwrite"] + self.cmd_args + [fin, fout])
        return fout

    def decode(self, fin):
        fout = fin + ".wav"
        decoder = self.path.replace("mpcenc", "mpcdec")
        call([decoder, fin, fout], stdout=DEVNULL, stderr=DEVNULL)
        return fout

def spectro(audio):
    spectro = np.abs(librosa.stft(audio, n_fft=4096))
    sdb = librosa.amplitude_to_db(spectro, ref=np.max)
    return sdb, spectro**2

def weighted_spectro(audio, sr):
    C = np.abs(librosa.cqt(audio, sr=sr, fmin=cqt_fmin))
    freqs = librosa.cqt_frequencies(C.shape[0], fmin=cqt_fmin)
    perceptual_sdb = librosa.perceptual_weighting(C**2, freqs, ref=np.max)
    return perceptual_sdb, librosa.db_to_power(perceptual_sdb)

def signal_to_noise(s_source, s_result): # s: power spectrogram
    return 10*(np.log10(np.sum(s_source)) -\
               np.log10(np.sum(np.abs(s_source - s_result))))

def array_hash(audio):
    return sha1(audio).digest()

def contour_points(x, y, direction): # direction: ne, nw, se, sw
    if len(x) <= 2:
        return np.arange(len(x))

    if isinstance(direction, str):
        if direction == "ne":
            direction = np.pi / 4
        elif direction == "sw":
            direction = -3*np.pi / 4
        elif direction == "nw":
            direction = 3*np.pi / 4
        elif direction == "se":
            direction = -np.pi / 4
        else:
            raise ValueError("unrecognized direction.")

    dsin, dcos = np.sin(direction), np.cos(direction)
    projected = dsin*x - dcos*y
    pstart, pend = np.argmax(projected), np.argmin(projected)

    hull = ConvexHull(np.array([x, y]).T)
    part_hull = []
    part_inside = False
    for idx in list(hull.vertices) + list(hull.vertices):
        if idx == pstart:
            part_inside = True
        if part_inside:
            part_hull.append(idx)
        if idx == pend and part_inside:
            return np.array(part_hull)
