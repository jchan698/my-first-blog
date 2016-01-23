#!/usr/bin/env python
import sys
import requests
import lxml
import lxml.html
import json

#import html_scrape # YOU DONT NEED THIS

'''
html -> raw html text
elem -> an lxml.ElementTree object
page_elem -> an elem containing the entire parsed html page
athlete_elem -> an elem containing a row in the player table
athlete_elems -> list of athlete_elem(s)
athlete -> a dict of properties of an athlete 
athletes -> a list of athlete(s)
'''

def download_html_from_remote():
    return requests.get('http://opendorse.com/blog/top-100-highest-paid-athlete-endorsers-of-2013/').text

def get_element_from_html(html):
    return lxml.html.fromstring(html)


def find_table_on_page(page_element):
    athletes = []


	#column for athlete names
    for index1 in xrange(2,109):	
	tables1 = page_element.xpath("//*[@id='post-2673']/div/h3[" + str(index1) + "]/text()")
	tables1='|'.join(tables1)


    #add column for endorsement values
    for index2 in xrange(5,562):	
        tables2= page_element.xpath("//*[@id='post-2673']/div/p[" + str(index2) + "]/strong/span") 
        
    athletes.append(lxml.html.tostring(tables1.split('|')[0],tables2[0]))
    return athletes
    print athletes 

html = download_html_from_remote()
page = get_element_from_html(html)
athletes = find_table_on_page(page)
for a in athletes:
    print a

#writes athletes to csv
import csv
with open('endorsement_earnings.csv', 'athletes') as csvfile:
    endorsewriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

# https://docs.python.org/2/library/csv.html#module-contents

