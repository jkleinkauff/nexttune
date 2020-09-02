import spotipy
from spotipy.oauth2 import SpotifyOAuth
from django.conf import settings
import time


class SpotifyHelper:
    def __init__(self):
        self.cli_id = settings.SPOTIFY_APP_CLI_ID
        self.cli_sec = settings.SPOTIFY_APP_CLI_SEC
        self.callback = settings.SPOTIFY_CALLBACK
        self.scope = settings.SPOTIFY_SCOPE

    def get_oauth(self):
        print(settings.SPOTIFY_SCOPE)
        sp_oauth = spotipy.oauth2.SpotifyOAuth(
            client_id=settings.SPOTIFY_APP_CLI_ID,
            client_secret=settings.SPOTIFY_APP_CLI_SEC,
            redirect_uri=settings.SPOTIFY_CALLBACK,
            scope=settings.SPOTIFY_SCOPE,
        )
        return sp_oauth

    # to do not reuse spotify auth, for some methods will be better to recreate it
    def get_auth_uri(self):
        self.__init__()
        return self.get_oauth().get_authorize_url()

    # to do not reuse spotify auth, for some methods will be better to recreate it
    def get_access_token(self, code):
        self.__init__()
        # spauth = self.get_oauth()
        return self.get_oauth().get_access_token(code, check_cache=False)

    # Checks to see if token is valid and gets a new token if not
    def get_token(self, session):
        token_valid = False
        token_info = session.get("token_info", {})
        if not (session.get("token_info", False)):
            token_valid = False
            return token_info, token_valid

        # Checking if token has expired
        now = int(time.time())
        is_token_expired = session.get("token_info").get("expires_at") - now < 60

        # Refreshing token if it has expired
        if is_token_expired:
            token_info = (
                SpotifyHelper()
                .get_oauth()
                .refresh_access_token(session.get("token_info").get("refresh_token"))
            )

        token_valid = True
        return token_info, token_valid

    def call_api_method(self, session, method, params={}, re_if_not_auth=True):
        session["token_info"], authorized = self.get_token(session)
        session.modified = True
        if not authorized:
            return {}

        sp = spotipy.Spotify(auth=session.get("token_info").get("access_token"))
        result = {}
        http_code = 200
        # import pdb

        # pdb.set_trace()
        try:
            result = getattr(sp, method)(**params)
        except Exception as e:
            result, http_code = e.msg, e.http_status

        return result  # , http_code


class SpotifyWrapper:
    def __init__(self, session):
        self._spotifyhelper = SpotifyHelper()
        self._session = session

    def user_top_tracks(self):
        top_tracks_params = {"limit": 10, "time_range": "short_term"}
        response = []
        result = self._spotifyhelper.call_api_method(
            self._session, "current_user_top_tracks", params=top_tracks_params
        )

        for i, m in enumerate(result["items"]):  # loop through songs
            song = {
                "name": m["name"],
                "album_art": m["album"]["images"][0]["url"],
                "url": m["href"],
                "track_id": m["href"][m["href"].rfind("/") + 1 :],
            }
            response.append(song)
        return response

    def play_song(self, track_id):
        params = {"uris": [f"spotify:track:{track_id}"]}
        result = self._spotifyhelper.call_api_method(
            self._session, "start_playback", params=params
        )
        # print(result)
        return result

    def current_playing(self):
        # current_user_playing_track
        response = {}
        result = self._spotifyhelper.call_api_method(
            self._session, "current_user_playing_track"
        )

        if result:
            response["name"] = result["item"]["name"]
            response["artist"] = result["item"]["artists"][0]["name"]
            response["popularity"] = result["item"]["popularity"]
            response["album_art"] = result["item"]["album"]["images"][1]["url"]

        # import pdb

        # pdb.set_trace()
        # print(response)
        return response