# import json
# import requests

# username = "admin"
# password = "admin"
# url = "http://127.0.0.1:8000/api/add-to-cart/"

# s = requests.Session()
# headers = {"Content-Type": "application/json"}
# payload = {"id": "1", "quantity": "1"}
# post = s.post(url, data=json.dumps(payload), headers=headers,auth=(username, password))

# print(post.text)
# print(post.status_code)



# another system

import json
import requests

username = "admin"
password = "admin"
url = "http://127.0.0.1:8000/api/add-to-cart/"


headers = {"Content-Type": "application/json"}
payload = {"id": "1", "quantity": "1"}
post = requests.post(url, data=json.dumps(payload), headers=headers,auth=(username, password))

print(post.text)
print(post.status_code)

