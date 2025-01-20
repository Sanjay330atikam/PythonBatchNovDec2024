"""
Purpose: Reading(Parsing)XML file
"""

import xml.etree.ElementTree as ET
from pprint import pp

tree = ET.parse("books.xml") # to take the xml book content
# print(dir(tree))
# print(tree.find('book'))
# print(tree.findall('book'))

books={}
for each in tree.findall('book'):
    isbn = each.attrib['isbn']
    for each_sub in each.findall('title'):
        book_title = each_sub.text
        # print(book_title)
        books[isbn]=(book_title)
pp(books)
    

# print(dir(each))