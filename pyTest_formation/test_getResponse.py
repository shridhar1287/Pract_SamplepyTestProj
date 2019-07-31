import json
import  requests

# endpoint uri
URL="https://reqres.in/api/users?page=2"

def test_get_reqres_data():
    # request command
    respo = requests.get(URL)
    # response obj printing
    print(respo)
    #response status code
    print(respo.status_code)
    # display response content
    print(respo.content)
    print("response data --> {0}".format(respo._content))
    # print(f"respo DT -->--> {respo.content}")

    # response headers
    print("headers-->{0}".format(respo.headers))
    # response encoding
    print(respo.encoding)
    # response cokkiees
    print(respo.cookies)
    print("................................")
    # convert to json format
    respo_json = json.loads(respo._content)

    print(respo_json)
    print("............. \n json print -->> {0}".format(json.loads(respo.text)))

    assert  respo.status_code==201 ,"get request failed..."


def test_get_reqres2_data():
    # request command
    respo = requests.get(URL)

    assert  respo.status_code==200 ,"get request failed..."