import pytest
from app import app as myapp


@pytest.fixture()
def app():
    print(1111111111111111)
    myapp.testing = True

    # other setup can go here

    yield myapp

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    print(22222222222222222222)
    return app.test_client()


@pytest.fixture()
def runner(app):
    print(333333333333333)
    return app.test_cli_runner()

