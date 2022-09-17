import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re


# sample data - http://py4e-data.dr-chuck.net/known_by_Fikret.html
# actual data - http://py4e-data.dr-chuck.net/known_by_Zachariya.html

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))
i = 0
while i < count:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    match = re.search(r'href="(.+)"', str(tags[position-1]))
    link = match.group().split('"')
    url = link[1]
    print('Retrieving:', url)
    i += 1
