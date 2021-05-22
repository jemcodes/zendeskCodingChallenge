import json
import pytest
import responses
from dotenv import load_dotenv
from app import app as flask_app

load_dotenv()


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


@responses.activate
def test_index(app, client):
    responses.add(
        responses.GET, 'https://jemcodes.zendesk.com/api/v2/tickets/',
        json={'tickets': []}, status=200)
    res = client.get('/')
    assert res.status_code == 200
    assert 'Ticket List' in res.get_data(as_text=True)


@responses.activate
def test_index_errors(app, client):
    responses.add(
        responses.GET, 'https://jemcodes.zendesk.com/api/v2/tickets/',
        status=500)

    res = client.get('/')
    assert res.status_code == 200
    assert 'Cue the sad trombone sounds - something went wrong!' \
        in res.get_data(as_text=True)
