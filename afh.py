#!/usr/bin/env python3
from requests import post
fid = input('Input fid:')
headers = {'Content-Type':'application/x-www-form-urlencoded'}
data = {'submit':'submit',
        'action':'getdownloadmirrors',
        'fid':fid}
ret = post(url = 'https://androidfilehost.com/libs/otf/mirrors.otf.php', data = data, headers = headers)
content = ret.json()
if len(content['MIRRORS']) < 1:
    print('No download link available.')
    exit()
for i in content['MIRRORS']:
    print(f"Server name: {i['name']}")
    print(f"Download link: {i['url']}\r\n")
