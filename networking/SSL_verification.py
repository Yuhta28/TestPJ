from io import StringIO
import requests
print(requests.get('https://github.com',verify=True)) # Response [200]