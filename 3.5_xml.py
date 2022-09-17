import urllib.request, urllib.error
import xml.etree.ElementTree as ET
import ssl


# sample data = http://py4e-data.dr-chuck.net/comments_42.xml
# actual data = http://py4e-data.dr-chuck.net/comments_1651252.xml

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'

print('Retrieving:', url)
url_handle = urllib.request.urlopen(url, context=ctx)
data = url_handle.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)
counts = tree.findall('.//count')
total = 0
for count in counts:
    total += int(count.text)
print('Sum:', total)
