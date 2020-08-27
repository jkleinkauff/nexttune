import pytest


def test_music_get(test_client):

    response = test_client.get('/music')
    assert response.status_code == 200


def test_music_put(test_client, test_settings):
    data = open(f"{test_settings.BASE_AUDIO_META}/abc.mp3", 'rb')
    headers = {'content-type': 'audio/mpeg'}

    response = test_client.put(
        '/music/genre/artist/sonsg', data=data, headers=headers)

    assert response.status_code == 201
