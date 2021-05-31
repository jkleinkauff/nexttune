import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = True if os.environ["FLASK_ENV"] == "development" else False
HOST = "127.0.0.1" if DEBUG else "0.0.0.0"
PORT = 5000 if DEBUG else 80
BASE_API = "api"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_AUDIO_META = f"{BASE_DIR}/{BASE_API}/music_data"
SENTRY_DNS = os.environ["SENTRY_DNS"]
# spotify settings
SPOTIFY_CALLBACK = os.environ["SPOTIFY_CALLBACK"]
SPOTIFY_API_BASE = os.environ["SPOTIFY_API_BASE"]
SPOTIFY_SCOPE = os.environ["SPOTIFY_SCOPE"]
SPOTIFY_APP_CLI_ID = os.environ["SPOTIFY_APP_CLI_ID"]
SPOTIFY_APP_CLI_SEC = os.environ["SPOTIFY_APP_CLI_SEC"]
# audio folders
AUDIO_SLICED_SPECTROGRAM_FOLDER = os.environ["AUDIO_SLICED_SPECTROGRAM_FOLDER"]

# model
MODEL_PATH = os.environ["MODEL_PATH"]
