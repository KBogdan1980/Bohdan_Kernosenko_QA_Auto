import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get("https://api.github.com/zen")
    print(r.format("Response is {r.text}"))

@pytest.mark.http
def test_second_request():
    r = requests.get("https://api.github.com/users/defunkt")
    body = r.json()
    headers = r.headers

    assert body['name'] == 'Chris Wanstrath'
    assert r.status_code == 200
    assert headers['Server'] == 'GitHub.com'


@pytest.mark.http
def test_status_code_request():
    r = requests.get("https://api.github.com/users/sergii_butenko")

    assert r.status_code == 200 #404

'''
@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt')
    print(r.format("Response Body is {r.json()}"))
    print(r.format("Response Status Coce is {r.status_code}"))
    print(r.format("Response Body is {r.headers}"))
'''