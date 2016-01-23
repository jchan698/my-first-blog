#!/usr/bin/env python

#steps:
#GOAL is to match extra columns of zip code/coordinates to all athlete locations
#1.get all athlete information from spotrac.com
#2.get all athlete city information from the various websites/APIs

#http://www.nba.com/playerfile/ # basketball college, all teams, USE WIKI to look up college acronyms
#http://espn.go.com/nba/players #basketball home city

#http://www.pro-football-reference.com/players/ #football home city, high school, college, all teams

#http://www.hockey-reference.com/players/ #hockey home city and all teams
#(will still miss high school/ college for hockey players)

#http://www.baseball-reference.com/players/ #baseball home city, high school, and all teams
#http://mlb.mlb.com/mlb/players/?tcid=nav_mlb_players #baseball college

#3.use smarty street to get zip codes/coordinates for all cities



#PACKAGES TO IMPORT#-------------------------
#1. package(s) to get all athlete information from spotrac.com
from lxml import html

import requests


#2.package(s) to get all athlete city information from the various websites/APIs

import urllib
import urllib2

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#3. package(s) to use smarty street to get zip codes/coordinates for all cities to convert city into zip codes and coordinates

import requests

import xlrd
import xlwt

#CODING LINE#---------------------------------
#1.code to get athlete names

page = requests.get('http://www.spotrac.com/nba/contracts/')
tree = html.fromstring(page.text)
players  = tree.xpath('//div[@title="PLAYER"]/text()')
print 'Player: ', players

#2. scrape for that athletes information on a web page




page = requests.get('http://www.nba.com/playerfile/')
tree = html.fromstring(page.text)

table=pd.Series([])

for row in players 
	url = 'http://www.nba.com/playerfile/' 
	values = {'name' : row,,
          'language' : 'Python' }

	data = urllib.urlencode(values)
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
	the_page = response.read()

	college  = tree.xpath('//div[@title='College']/text()')

#combine them in a table
	table= pd.Series([table;row,college])


#use wiki





#3. code to convert city into zip codes and coordinates


zips= pd.Series([])

for row in table
  
	params = {
		'street': row[2],
		'auth-id': 'e076f836-9fbb-4e0c-ab48-3325ea9959f9',
		'auth-token': 'Ws5ZeW0iNJz013SYnnZk'}
	response = requests.get('https://api.smartystreets.com/street-address', params=params)

	data = response.json()

for row in data:
	print row['components'] [u'zipcode'] [u'coordinates']
	zips= pd.Series([zips;[u'zipcode'], [u'coordinates'])



