import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count: '))  
position = int(input('Enter position: '))  

print("Retrieving:", url)
for i in range(count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')

    url = tags[position - 1].get('href', None)
    print("Retrieving:", url)

name = url.split('_')[-1].split('.')[0]
print("Last name:", name)