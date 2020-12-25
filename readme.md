# Audio codecs comparsion

- FLAC (flac v1.3.2): Downloaded from https://xiph.org/flac/download.html
- MP3 (lame 3.100.1): Downloaded from https://www.rarewares.org/mp3-lame-bundle.php
- APE (mac 5.69): Downloaded from https://www.monkeysaudio.com/download.html
- Wavpack (wavpack 5.3.0): Downloaded from http://www.wavpack.com/downloads.html
- TAK (takc 2.3.0): Downloaded from http://thbeck.de/Tak/Tak.html
- TTA (tta 2.3): Downloaded from https://sourceforge.net/projects/tta/files/tta/ttaenc-win/
- WMA (WmaEncoder 0.2.9c): Downloaded from https://hydrogenaud.io/index.php/topic,90519.0.html
- lossyWAV (lossyWAV 1.4.2): Downloaded from https://wiki.hydrogenaud.io/index.php?title=LossyWAV
- ALAC (refalac v2.71): Downloaded from https://github.com/nu774/qaac/releases/tag/v2.71
- OptimFrog (ofc & ofs v5.100): Downloaded from http://losslessaudio.org/Downloads.php
- MPEG-4 ALS (): Downloaded from https://web.archive.org/web/20170826003357/http://www.nue.tu-berlin.de:80/menue/research_new/projects/projects/mpeg_4_audio_lossless_coding_als/parameter/en

For missing encoder or decoder, [`ffmpeg (4.3.1-2020-11-19 x64)`](https://www.gyan.dev/ffmpeg/builds/) is used. Also note that OptimFrog encoding and decoding always crashes for me, and the dual stream encoding cannot preserve lossless audio (due to the crash , I guess).

## Results

Bass_tek2 - PLight (*Hardcore*)

![Lossless codecs comparison]("figs/Hands Up - Hommarju.wav.lossless.jpg")
![Lossy codecs comparison]("figs/Hands Up - Hommarju.wav.lossy.jpg")
