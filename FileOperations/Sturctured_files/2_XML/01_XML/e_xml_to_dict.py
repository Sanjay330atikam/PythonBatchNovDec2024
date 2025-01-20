"""
Purpose: XML to Dict Conversion
        pip install xmltodict
        
"""
"""Difference between Pprint()and PPprint()
pp-gives in same sequence
p-sort them"""


import xmltodict
from pprint import pp
with open('books.xml','r') as fh:
    file_content =fh.read()
    doc = xmltodict.parse(file_content)

pp(doc)

mapping={}
for each in doc['catlog']['book']:
    mapping[each['@isbn']] = each['title']

pp(mapping)