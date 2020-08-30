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

print(SENTRY_DNS)
