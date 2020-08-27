import pytest


def test_genre_get(test_client):

    response = test_client.get('/genre')
    assert response.status_code == 200
