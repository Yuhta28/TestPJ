import requests

import requests

r = requests.get('https://api.github.com/events')
print(r.json())