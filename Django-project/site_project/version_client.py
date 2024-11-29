import requests
import pprint


url = 'http://127.0.0.1:8000/api/site/categories/'

response = requests.get(url)

pprint.pprint(response.json())