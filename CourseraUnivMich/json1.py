import json
import urllib.request

url = input('Enter location: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_2199173.json'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved',len(data),'characters')

try:   
    js = json.loads(data)
except:
    js = None

if not js or 'comments' not in js:
    print('JSON does not contain comments')
    print(data)
    quit()

if len(js['comments']) == 0:
    print('No comments found')
    quit()

comments = js['comments']
count = len(comments)
total_sum = sum([int(comment['count']) for comment in comments])

print('Count:', count)
print('Sum', total_sum)