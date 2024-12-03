import requests
import pprint

# GET request
# print("GET Request:")
# response = requests.get('https://reqres.in/api/users')
# # pprint.pprint(response.json())
# # pprint.pprint(response.json()['data'][0]['id'])
# # pprint.pprint(response.json()['data'][3]['id'])
# print(response.status_code)
# print(response.reason)
# print(response.text)
# print(response.headers)
# print(response.headers['Content-Type'])

# POST request
# print("\nPOST Request:")
# new_user = {"name": "John Doe", "job": "Developer"}
# response = requests.post('https://reqres.in/api/users', json=new_user)
# print(response.json())
# print(response.status_code)
# print(response.reason)

# PUT request
# print("\nPUT Request:")
# update_user = {"name": "Jane Doe", "job": "Manager"}
# response = requests.put('https://reqres.in/api/users/2', json=update_user)
# print(response.json())
# print(response.status_code)
# print(response.reason)

# DELETE request
# print("\nDELETE Request:")
# response = requests.delete('https://reqres.in/api/users/2')
# print(response.status_code)
# print(response.reason)

# POST Invalid Request
print("\nPOST Invalid Request:")
credentials = { "email": "peter@klaven"}
response = requests.post('https://reqres.in/api/login', json=credentials)
print(response.status_code)
print(response.reason)
print(response.json())