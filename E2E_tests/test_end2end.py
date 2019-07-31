import json

import requests



idVal =None
def test_add_new_data():
  appURL="http://thetestingworldapi.com/api/studentsDetails"
  f = open("resourses/e2eReqData.json",'r')
  req_json_in=json.loads(f.read())
  resp = requests.post(appURL,req_json_in)

  print(resp.status_code)
  assert resp.status_code == 201

  print(resp.text)

  f_out= open("resourses/e2eRespoData.json",'w')
  f_out.write(resp.text)


  f.closed
  f_out.close()

def test_modify_data():
  postEndPoint = "http://thetestingworldapi.com/api/technicalskills"

  f = open("resourses/postdetail.txt",'r')
  jsonPsstdt = json.loads(f.read())
  # jsonPsstdt['id']=int(idVal)
  respost=requests.post(postEndPoint,jsonPsstdt)
  f_postO=open("resourses/post_out_detail.txt",'a+')
  f_postO.write(str(respost.status_code) + "\n")
  f_postO.write(".................. \n")
  f_postO.write(respost._content + "\n")
  f_postO.write("-------------------------------------- \n ")

  f.close()
  f_postO.close()


def test_get_data():
  getEndPoint="http://thetestingworldapi.com/api/technicalskills/3011"
  respoGet=requests.get(getEndPoint)
  f_get_out = open("resourses/post_out_detail.txt",'a+')
  f_get_out.write(str(requests.codes)+"\n"+"......"+"\n")
  f_get_out.write(str(respoGet.status_code)+"\n")
  f_get_out.write("........ \n")
  f_get_out.write(respoGet.text+"\n")

  f_get_out.close()