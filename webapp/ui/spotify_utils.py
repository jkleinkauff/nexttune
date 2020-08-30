import spotipy
from spotipy.oauth2 import SpotifyOAuth
from django.conf import settings
import time


def get_oauth_obj():
    sp_oauth = spotipy.oauth2.SpotifyOAuth(
        client_id=settings.SPOTIFY_APP_CLI_ID,
        client_secret=settings.SPOTIFY_APP_CLI_SEC,
        redirect_uri=settings.SPOTIFY_CALLBACK,
        scope=settings.SPOTIFY_SCOPE,
    )
    return sp_oauth


def save_session(request, session_name, token_info, clear_current=False):
    if clear_current and request.session.get(session_name, None) == "dummy":
        del request.session[session_name]

    request.session[session_name] = token_info


def get_token(session):
    token_valid = False
    token_info = session.get("token_info", {})

    # token already stored?
    if not (session.get("token_info", False)):
        token_valid = False
        return token_info, token_valid

    # token expired ?
    is_token_expired = False
    is_token_expired = session.get("token_info").get("expires_at") - time.time() < 60

    if is_token_expired:
        sp_oauth = spotipy.oauth2.SpotifyOAuth(
            client_id=settings.SPOTIFY_APP_CLI_ID,
            client_secret=settings.SPOTIFY_APP_CLI_SEC,
            redirect_uri=settings.SPOTIFY_CALLBACK,
            scope=settings.SPOTIFY_SCOPE,
        )
        import pdb

        pdb.set_trace()
        token_info = sp_oauth.refresh_access_token(
            session.get("token_info").get("refresh_token")
        )

    token_valid = True
    return token_info, token_valid


def get_sp_client(access_token):
    sp = spotipy.Spotify(auth=access_token)
    return sp
