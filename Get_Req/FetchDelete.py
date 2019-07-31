# endpoint
import requests

URL = "https://reqres.in/api/users/2"

response = requests.request("delete",URL)

print(response.status_code)

assert  response.status_code==204 , "wrong status eval..."