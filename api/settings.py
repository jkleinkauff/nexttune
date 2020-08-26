import os


BASE_API = "api"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_AUDIO_META = f"{BASE_DIR}/{BASE_API}/music_data"
SENTRY_DNS = os.environ["SENTRY_DNS"]
