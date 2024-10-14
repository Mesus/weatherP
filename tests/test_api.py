import json


def test_logout(client):
    rv = client.get('/weather/北京')

    assert rv.status_code == 200
    assert rv.json['code'] == 0