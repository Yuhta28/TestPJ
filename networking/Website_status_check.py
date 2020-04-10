import requests
r = requests.get('http://pythonspot.com/')
print(r.status_code)