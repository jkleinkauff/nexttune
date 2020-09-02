# djbootstrap4/bootstrap4/urls.py
from django.urls import path
from . import views, views_login_callback

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.ui_login, name="login-spotify"),
    path("callback", views_login_callback.spotify_callback),
    path("play_song/<str:track_id>", views.play_song, name="play_song"),
    path("current_playing", views.current_track, name="current-playing"),
]
