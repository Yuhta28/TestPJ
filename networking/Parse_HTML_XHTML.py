from bs4 import BeautifulSoup
import urllib3
import requests

# Get the contents
#response = urllib3.PoolManager
open_url = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)')
# Create bs4 object
bs4Obj = bs4.BeautifulSoup(open_url,'lxml')
print(type(bs4Obj))

# cannot python

#parsed_html = BeautifulSoup(html)
#print(parsed_html.body.find('div', attrs={'class':'toc'}))