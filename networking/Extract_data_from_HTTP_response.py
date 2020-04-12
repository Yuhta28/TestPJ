from bs4 import BeautifulSoup
import requests

# get html data
r = requests.get('http://stackoverflow.com/')
html_doc = r.content

# create a beautifulsoup object
soup = BeautifulSoup(html_doc)

# get title
print(soup.title)

# print all links
for link in soup.find_all('a'):
    print(link.get('href'))