import urllib3
download_url = 'https://wordpress.org/plugins/about/readme.txt'
request_methods = urllib3.PoolManager() # Need instance to request
response = request_methods.request('GET', download_url)
print(response.data) # show data

f = open('reademe.txt','wb') # download text
# f = open('reademe.html','wb') # download web page
f.write(response.data) # to add in text
f.close() # end