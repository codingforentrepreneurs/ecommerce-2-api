import requests



base_url = "http://127.0.0.1:8000/api/"

login_url = base_url + "auth/token/"

products_url = base_url + "products/"

refresh_url = login_url + "refresh/"
#requests.get
#requests.post(login_url, data=None, headers=None, params=None)


data = {
	"username": "jmitchel3",
	"password": "123"
}
login_r = requests.post(login_url, data=data)
login_r.text
json_data = login_r.json()

import json

print(json.dumps(json_data, indent=2))

token = json_data["token"]
print token

headers = {
	"Authorization": "JWT %s" %(token),
}

p_r = requests.get(products_url, headers=headers)
print p_r.text
print(json.dumps(p_r.json(), indent=2))



#Refresh URL TOKEN

data = {
	"token": token
}
refresh_r = requests.post(refresh_url, data=data)


print refresh_r.json()

token = refresh_r.json()["token"]







