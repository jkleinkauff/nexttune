from django.http import HttpResponse
from . import spotify_utils
from .spotify_utils import SpotifyHelper


def spotify_callback(request):
    code = request.GET["code"]
    token_info = SpotifyHelper().get_access_token(code)
    request.session["token_info"] = token_info
    print(token_info)

    # sp_oauth = spotify_utils.get_oauth_obj()
    # code = request.GET["code"]
    # token_info = sp_oauth.get_access_token(code, check_cache=False)
    # spotify_utils.save_session(request, "token_info", token_info, clear_current=True)

    # return redirect("/")
    return HttpResponse('<script type="text/javascript">window.close();</script>')


def go(request):
    import pdb

    pdb.set_trace()

    request.session["token_info"], authorized = spotify_utils.get_token(request.session)
    # session.modified = True
    if not authorized:
        return redirect("/")
    sp = spotipy.Spotify(auth=request.session.get("token_info").get("access_token"))
    response = sp.current_user_top_tracks(limit=10)

    # print(json.dumps(response))

    return render_template("results.html", data=data)
