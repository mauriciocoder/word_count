import pytest
from flask import Flask
from flask.testing import FlaskClient


@pytest.fixture
def app() -> Flask:
    from src.api import app

    yield app


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()


def test_count_words_empty_payload(client: FlaskClient):
    response = client.post(
        "/count_words",
        json=[],
    )
    assert response.status_code == 400


def test_count_words_numeric_payload(client: FlaskClient):
    response = client.post(
        "/count_words",
        json=[123],
    )
    assert response.status_code == 400


def test_count_words_numeric_and_word_in_payload(client: FlaskClient):
    response = client.post(
        "/count_words",
        json=[123.123, "abc"],
    )
    assert response.status_code == 400


def test_count_words_valid(client: FlaskClient):
    response = client.post(
        "/count_words",
        json=["hello world", "word count exercise"],
    )
    assert response.status_code == 200
    assert response.data == b"[2,3]\n"
