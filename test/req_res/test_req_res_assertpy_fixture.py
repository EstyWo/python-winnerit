import pytest
import requests
from assertpy import assert_that

@pytest.fixture
def base_url():
    return 'https://reqres.in/api'

def test_get_user_with_assertpy(base_url):
    response = requests.get(f'{base_url}/users/2')
    print(response.json())
    print(response.status_code)
    print(response.reason)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.json()).contains_key('data')
    assert_that(response.json()['data']).contains_entry({'id': 2})

def test_create_user_with_assertpy(base_url):
    new_user = {"name": "Jane Smith", "job": "Designer"}
    response = requests.post(f'{base_url}/users', json=new_user)
    print(response.json())
    print(response.status_code)
    print(response.reason)
    assert_that(response.status_code).is_equal_to(201)
    assert_that(response.json()).contains_key('id')
    assert_that(response.json()['name']).is_equal_to("Jane Smith")

def test_update_user_with_assertpy(base_url):
    update_user = {"name": "Jane Doe", "job": "Manager"}
    response = requests.put(f'{base_url}/users/2', json=update_user)
    print(response.json())
    print(response.status_code)
    print(response.reason)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.json()).contains_entry({'name': 'Jane Doe'})
    assert_that(response.json()).contains_entry({'job': 'Manager'})

def test_delete_user_with_assertpy(base_url):
    response = requests.delete(f'{base_url}/users/2')
    print(response.status_code)
    print(response.reason)
    assert_that(response.status_code).is_equal_to(204)