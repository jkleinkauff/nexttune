import os
from dotenv import load_dotenv

load_dotenv()


AUDIO_PLAYLIST_FOLDER = os.environ["AUDIO_PLAYLIST_FOLDER"]
AUDIO_DOWNLOAD_FOLDER = os.environ["AUDIO_DOWNLOAD_FOLDER"]
AUDIO_PLAYLIST_ARCHIVE = os.environ["AUDIO_PLAYLIST_ARCHIVE"]
AUDIO_30SEC_FOLDER = os.environ["AUDIO_30SEC_FOLDER"]
AUDIO_SPECTROGRAM_FOLDER = os.environ["AUDIO_SPECTROGRAM_FOLDER"]
AUDIO_SLICED_SPECTROGRAM_FOLDER = os.environ["AUDIO_SLICED_SPECTROGRAM_FOLDER"]