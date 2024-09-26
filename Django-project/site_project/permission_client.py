import requests
import pprint
from requests.auth import HTTPBasicAuth

url = 'http://127.0.0.1:8000/api/site/categories/'

response = requests.get(url)

print(response.status_code)

username = 'user'
password = 'user'

basic = HTTPBasicAuth(username, password)
response = requests.get(url, auth=basic)
print(response.status_code)

response = requests.post(url, auth=basic, data={})
print(response.status_code)

basic = HTTPBasicAuth('manager', 'manager')
response = requests.post(url, auth=basic, data={})
print(response.status_code)
pprint.pprint(response.json())