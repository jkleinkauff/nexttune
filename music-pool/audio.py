import matplotlib.pyplot as plt
import librosa
import librosa.display


class Audio(object):
    def __init__(self, filename):
        self.file = filename

    def load(self, sr=22050):
        signal, sr = librosa.load(self.file, sr=sr)
        self.signal = signal
        self.sr = sr

    def create_mel_spec_image(self, output):
        melspectrogram_array = librosa.feature.melspectrogram(
            y=self.signal, sr=self.sr, n_mels=128, fmax=8000
        )
        mel = librosa.power_to_db(melspectrogram_array)
        # Length and Width of Spectogram
        fig_size = plt.rcParams["figure.figsize"]
        fig_size[0] = float(mel.shape[1]) / float(100)
        fig_size[1] = float(mel.shape[0]) / float(100)
        plt.rcParams["figure.figsize"] = fig_size
        plt.axis("off")
        plt.axes([0.0, 0.0, 1.0, 1.0], frameon=False, xticks=[], yticks=[])
        librosa.display.specshow(mel, cmap="gray_r")
        plt.savefig(
            output,
            cmap="gray_r",
            bbox_inches=None,
            pad_inches=0,
        )
        plt.close()

    def cut_audio(self, sec, output):
        try:
            sec = str(sec)
            import subprocess as sp

            sp.call(
                [
                    "ffmpeg",
                    "-ss",
                    "60",
                    "-i",
                    self.file,
                    "-acodec",
                    "copy",
                    "-t",
                    sec,
                    output,
                ]
            )

        except Exception as ex:
            pass
