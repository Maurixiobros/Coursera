from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

total = 0

tags = soup('span') 
for tag in tags:
    
    try:
        num = int(tag.contents[0])  
        total += num  
    except ValueError:
        pass  


print("Total sum:", total)