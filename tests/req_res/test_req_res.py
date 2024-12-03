import pytest
import requests

base_url = "https://reqres.in/api"
# def test_get_user():
#     response = requests.get(f'{base_url}/users/2')
#     # print(response.json())
#     # print(response.status_code)
#     # print(response.reason)
#     # assert 200 <= response.status_code <= 210
#     assert response.status_code == 200
#     assert response.json()['data']['id'] == 2
#     assert response.json()["data"]['email'] == "janet.weaver@reqres.in"

# def test_create_user():
#     new_name = "Alex"
#     new_user = {"name": new_name, "job": "Developer"}
#     response = requests.post('https://reqres.in/api/users', json=new_user)
#
#     assert response.status_code == 201
#     assert 'id' in response.json()
#     assert response.json()['name'] == new_name

# def test_update_user():
#     update_user = {"name": "Jane Doe", "job": "Manager"}
#     response = requests.put('https://reqres.in/api/users/2', json=update_user)
#
#     assert response.status_code == 200
#     assert response.json()['name'] == "Jane Doe"
#     assert response.json()['job'] == "Manager"

# def test_delete_user():
#     response = requests.delete('https://reqres.in/api/users/2')
#     assert response.status_code == 204
#     assert response.text == ""

params = [(2, "janet.weaver@reqres.in"), (3, "emma.wong@reqres.in")]
@pytest.mark.parametrize("user_id, email", params)
def test_get_users(user_id, email):
    response = requests.get(f'https://reqres.in/api/users/{user_id}')

    assert response.status_code == 200
    assert response.json()['data']['id'] == user_id
    assert response.json()["data"]['email'] == email