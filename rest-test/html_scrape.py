#!/usr/bin/env python
'''
Library for scraping html
'''

import lxml
import lxml.html

def get_html_from_element(element):
    return lxml.html.tostring(element)

def get_row_elements_from_table_element(table_element):
    return table_element.xpath("tbody/tr")

def get_dict_from_row_element(row_element, column_codes):
    '''
    column_codes is an array of tuples that specify how to retrieve each column.  For example:
        column_codes = [
        # key             index  xpath       attrib (None => lambda elem: elem.text)
        # ---             -----  -----       --------------------------------------
        ('name',          0,     '/a',       None),
        ('url',           0,     '/a',       lambda elem: elem.attrib['href']),
        ]
    The value of the index is used to determine which <td> element in the row to scrape from.
    The xpath string and attrib expression is used to specify which subelement and property to use to get the 
    desired value of the dict key.
    In this example, it will scrape two fields, name and url, and create a dict key for each of them.
    The key 'name' will be taken from the first (index = 0, i.e. zero-based) <td> element.  
    The "/a" means it will use the first <a> element inside that <td> element.
    If attrib = None, it will extract the .text member of the resultant lxml xpath query.
    Specifying a lambda or other functor allows you to get custom attributes of the element.
    '''
    obj = {}
    for column_code in column_codes:
        obj[column_code[0]] = get_column_elem_helper(row_element, column_code[1], column_code[2], column_code[3])
    return obj

def get_column_elem_helper(row_element, column_index, extra_xpath, member = None):
    if not member:
        member = lambda elem: elem.text
    column_index += 1
    column_element = row_element.xpath("(td)[{column_index}]{extra_xpath}".format(column_index=column_index, extra_xpath=extra_xpath))
    return member(column_element[0])