import urllib.request
import json


# sample data = http://py4e-data.dr-chuck.net/comments_42.json
# actual data = http://py4e-data.dr-chuck.net/comments_1651253.json

url = input('Enter url: ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_42.json'

url_handle = urllib.request.urlopen(url)
data = url_handle.read().decode()
js = json.loads(data)
total = 0
comments = js['comments']
for comment in comments:
    total += int(comment['count'])
print('Sum:', total)
