import requests
import settings
from pathlib import Path


BASE = "http://localhost:5000/"

data = open(f"{settings.BASE_AUDIO_META}/abc.mp3", 'rb')
headers = {'content-type': 'audio/mpeg'}

response = requests.put(
    BASE + "music/godsmack/awake", data=data, headers=headers)

print(response.json())
