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
    """"Test that ticket list route renders ticket list view"""
    responses.add(
        responses.GET, 'https://jemcodes.zendesk.com/api/v2/tickets/',
        json={'tickets': []}, status=200)

    res = client.get('/')
    assert res.status_code == 200
    assert 'Ticket List' in res.get_data(as_text=True)


@responses.activate
def test_index_errors(app, client):
    """"Test that ticket list route renders error for 500 status code"""
    responses.add(
        responses.GET, 'https://jemcodes.zendesk.com/api/v2/tickets/',
        status=500)

    res = client.get('/')
    assert res.status_code == 200
    assert 'Cue the sad trombone sounds - something went wrong!' \
        in res.get_data(as_text=True)


@responses.activate
def test_single_ticket(app, client):
    """"Test that single ticket route renders single ticket view"""
    responses.add(
        responses.GET, 'https://jemcodes.zendesk.com/api/v2/tickets/1',
        json={'ticket': []}, status=200)
    res = client.get('/1')
    assert res.status_code == 200
    assert 'Single Ticket' in res.get_data(as_text=True)


@responses.activate
def test_single_ticket_errors(app, client):
    """"Test that single ticket route renders error for 500 status code"""
    responses.add(
        responses.GET, 'https://jemcodes.zendesk.com/api/v2/tickets/1',
        status=500)

    res = client.get('/1')
    assert res.status_code == 200
    assert 'Uh oh! Looks like a classic Dinosaur Ate My Ticket situation!' \
        in res.get_data(as_text=True)
