import sentry_sdk
from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
from sentry_sdk.integrations.flask import FlaskIntegration
import settings

sentry_sdk.init(
    dsn=settings.SENTRY_DNS,
    integrations=[FlaskIntegration()]
)


class CustomApi(Api):

    def handle_error(self, e):
        return ({"error": str(e)}), e.code


app = Flask(__name__)
api = CustomApi(app)

musics = {}

music_post_args = reqparse.RequestParser()
# music_post_args.add_argument(
#     "audio_data", type=bytes, location="data", help="music audio", required=True)


class MusicListResource(Resource):
    def get(self):
        return "musics"


class MusicResource(Resource):
    def put(self, artist, songname):
        # args = music_post_args.parse_args()
        music = {}
        music["artist"] = artist
        music["songname"] = songname
        with open(f"{settings.BASE_AUDIO_META}/{artist}_{songname}.mp3", "wb") as f:
            f.write(request.data)
            f.close()
        return music, 201


api.add_resource(MusicListResource, "/music")
api.add_resource(MusicResource, "/music/<string:artist>/<string:songname>")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
    # app.run(debug=True)
