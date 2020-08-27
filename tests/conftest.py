import pytest
from api.main import create_app
from api import settings


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()

    testing_client = flask_app.test_client()

    # ctx = flask_app.app_context()
    # ctx.push()

    yield testing_client


@pytest.fixture(scope='module')
def test_settings():
    return settings
