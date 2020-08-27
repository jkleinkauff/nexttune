from flask import request
from flask_restful import Resource
from api import settings

# music_post_args = reqparse.RequestParser()
# music_post_args.add_argument(
#     "audio_data", type=bytes, location="data", help="music audio", required=True)


class MusicListResource(Resource):
    def get(self):
        return "mussssics"


class MusicResource(Resource):
    def put(self, genre, artist, songname):
        # args = music_post_args.parse_args()
        music = {}
        music["artist"] = artist
        music["songname"] = songname
        with open(f"{settings.BASE_AUDIO_META}/{artist}_{songname}.mp3", "wb") as f:
            f.write(request.data)
            f.close()
        return music, 201
