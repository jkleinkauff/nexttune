from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from urllib.parse import urlencode
from django.conf import settings
from .spotify_utils import SpotifyHelper, SpotifyWrapper


def index(request):
    # TODO do just one wrapper or area specific wrappers.. but not 'spotifyhelper' to call
    # api specific endpoints
    obj1 = SpotifyHelper().call_api_method(request.session, "current_user")
    user_data = {"user": "", "top_tracks": ""}
    if obj1:
        obj2 = SpotifyWrapper(request.session).user_top_tracks()
        user_data = {"user": obj1, "top_tracks": obj2}
    return render(request, "ui/index.html", user_data)


def ui_login(request):
    # import pdb

    # pdb.set_trace()
    uri = SpotifyHelper().get_auth_uri()
    return redirect(uri)


def play_song(request, track_id):
    SpotifyWrapper(request.session).play_song(track_id)
    return HttpResponse(200)


def current_track(request):
    result = SpotifyWrapper(request.session).current_playing()
    return JsonResponse(result)