import json

import requests

# post endpoint
URL = "https://reqres.in/api/users"

# read post data json file
file = open("D:\\CybPro\\PycharmProjects\\SamplepyTestProj\\resourses\\postData.json",'r')
post_input=file.read()
json_post_input = json.loads(post_input)
print(json_post_input)
resp =  requests.post(URL,json_post_input)

print(resp.status_code)

assert resp.status_code==201 ,"failed to perform post....."

print(resp.content)

# retrive headers from response
print(resp.headers)

print(resp.headers.get('content'))