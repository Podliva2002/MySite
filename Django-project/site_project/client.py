import requests
import pprint
from requests.auth import HTTPBasicAuth

url = 'http://127.0.0.1:8000/api/site/categories/'

response = requests.get(url)

print(response.status_code)
pprint.pprint(response.json())


username = 'admin'
password = '123456789'

# basic = HTTPBasicAuth(username, password)
# response = requests.get(url, auth=basic)
pare = 'YWRtaW46MTIzNDU2Nzg5'

headers = {
    'Authorization': f'Basic {pare}'
}

response = requests.get(url, headers=headers)

print(response.status_code)
pprint.pprint(response.json())

token = 'f71c7ad8c6752faf6d5cf2352f6a3cd4b516268e'

headers = {
    'Authorization': f'Token {token}'
}

response = requests.get(url, headers=headers)

print(response.status_code)
pprint.pprint(response.json())
