import pytest
from modules.api.clients.github import GitHub

'''
#old version of tests

@pytest.mark.api
def test_user_exists():
    api = GitHub()
    user = api.get_user_defunkt()
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exist():
    api = GitHub()
    r = api.get_non_exist_user()
    assert r['message'] == 'Not Found'
'''

@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exist(github_api):
    r = github_api.get_user('sergiibutenko')
    assert r['message'] == 'Not Found'