#!/usr/bin/env python
import requests

#r = requests.get('https://api.github.com/user', auth=('jchan698', 'moviendoYa675'))
#print r.status_code

#response = urllib.urlopen('https://api.smartystreets.com/street-address?street=123+Main+52001&auth-id=<e076f836-9fbb-4e0c-ab48-3325ea9959f9>&auth-token=<Ws5ZeW0iNJz013SYnnZk>')
#addresses = json.loads(response.read())

params = {
	'city': 'boston',
	'state': 'Massachusetts',
	'auth-id': 'e076f836-9fbb-4e0c-ab48-3325ea9959f9',
	'auth-token': 'Ws5ZeW0iNJz013SYnnZk'}
response = requests.get('https://api.smartystreets.com/street-address', params=params)

data = response.json()

for row in data:
	print row['components'] [u'zipcode']
	print row

#print response
#print response.status_code
#print response.text
#print len(response.text)

#response.encoding = 'utf-8'
#print response.text
#print len(response.text)
#print response.content
#print len(response.content)
#print response.encoding
#print len(response.raw.read(10))