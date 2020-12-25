
import os.path as osp
from hashlib import sha1
from subprocess import DEVNULL, check_call

import librosa
import numpy as np

cqt_fmin = librosa.note_to_hz('A1')

class Codec:
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

def contour_points(x, y, direction):
    # direction: ne, nw, se, sw
