from django.http import HttpResponse
from django.shortcuts import render, redirect

from urllib.parse import urlencode
from django.conf import settings
import random
import base64
import requests
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from . import spotify_utils


def index(request):
    # output = ", ".join([q.question_text for q in latest_question_list])
    obj1 = get_user_info(request)
    print(obj1)
    # return HttpResponse(output)
    return render(request, "ui/index.html", obj1)


def ui_login(request):
    sp_oauth = spotify_utils.get_oauth_obj()
    auth_url = sp_oauth.get_authorize_url()
    print(auth_url)

    return redirect(auth_url)


def get_user_info(request):
    request.session["token_info"], authorized = spotify_utils.get_token(request.session)
    if not authorized:
        return {}
    sp = spotify_utils.get_sp_client(
        request.session.get("token_info").get("access_token")
    )

    return sp.current_user()
