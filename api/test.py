import requests
from pathlib import Path

BASE = "http://localhost:5000/"

path = Path(__file__).parent / "music_data/abc.mp3"

data = open(path, 'rb')
headers = {'content-type': 'audio/mpeg'}

response = requests.put(
    BASE + "music/soad/aerials", data=data, headers=headers)

print(response.json())
