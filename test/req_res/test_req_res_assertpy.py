import requests
from assertpy import assert_that

def test_get_user_with_assertpy():
    response = requests.get('https://reqres.in/api/users/2')

    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.json()).contains_key('data')
    assert_that(response.json()['data']).contains_entry({'id': 2})

def test_create_user_with_assertpy():
    new_user = {"name": "Jane Smith", "job": "Designer"}
    response = requests.post('https://reqres.in/api/users', json=new_user)

    assert_that(response.status_code).is_equal_to(201)
    assert_that(response.json()).contains_key('id')
    assert_that(response.json()['name']).is_equal_to("Jane Smith")

def test_update_user_with_assertpy():
    update_user = {"name": "Jane Doe", "job": "Manager"}
    response = requests.put('https://reqres.in/api/users/2', json=update_user)

    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.json()).contains_entry({'name': 'Jane Doe'})
    assert_that(response.json()).contains_entry({'job': 'Manager'})

def test_delete_user_with_assertpy():
    response = requests.delete('https://reqres.in/api/users/2')

    assert_that(response.status_code).is_equal_to(204)