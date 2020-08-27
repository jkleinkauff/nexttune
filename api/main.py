import sentry_sdk
from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
from sentry_sdk.integrations.flask import FlaskIntegration
from api.resources.music import MusicResource, MusicListResource
from api.resources.genre import GenreListResource
from api import settings


sentry_sdk.init(
    dsn=settings.SENTRY_DNS,
    integrations=[FlaskIntegration()]
)


class CustomApi(Api):

    def handle_error(self, e):
        return ({"error": str(e)}), e.code


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    api = CustomApi(app)

    api.add_resource(MusicListResource, "/music")
    api.add_resource(
        MusicResource, "/music/<string:genre>/<string:artist>/<string:songname>")

    api.add_resource(GenreListResource, "/genre")

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
