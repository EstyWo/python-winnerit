import pytest
import requests
from assertpy import assert_that
#
base_url = "https://reqres.in/api"
def test_get_user():
    response = requests.get(f'{base_url}/users/99')
    print(response.json())
    print(response.status_code)
    assert response.status_code == 404
    assert response.json() == {}

def test_login_success():
    user_details = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = requests.post(f'{base_url}/login', json = user_details)
    assert response.status_code == 200
    assert 'token' in response.json()

#assertpy
def test_get_user_with_assertpy():
    response = requests.get('https://reqres.in/api/users/99')
    assert_that(response.status_code).is_equal_to(404)
    assert_that(response.json()).is_empty()

def test_login_success_with_assertpy():
    user_details = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = requests.post("https://reqres.in/api/login", json = user_details)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.json()).contains_key('token')

#assertpy_fixture

@pytest.fixture
def base_url2():
    return 'https://reqres.in/api'

def test_get_user_with_assertpy_2(base_url2):
    response = requests.get(f'{base_url2}/users/99')
    assert_that(response.status_code).is_equal_to(404)
    assert_that(response.json()).is_empty()

def test_login_success_with_assertpy_2(base_url2):
    user_details = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = requests.post(f'{base_url2}/login', json = user_details)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.json()).contains_key('token')

