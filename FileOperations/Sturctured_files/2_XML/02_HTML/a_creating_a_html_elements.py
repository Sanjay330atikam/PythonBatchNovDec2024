"""
Puorpose: Creating html using lxml
      lxml has simple syntax and faster in performance
"""

from lxml import etree

root_elem = etree.Element("html")

etree.SubElement(root_elem,"head")
etree.SubElement(root_elem,"title")
etree.SubElement(root_elem,"body")

print(etree.tostring(root_elem,pretty_print=True).decode('utf-8'))
# <html>
#   <head/>
#   <title/>
#   <body/>
# </html>

html=root_elem[0]
print(f"{html.tag       =}")
for element in root_elem:
    print(f"{element.tag =}")

print(f"{etree.iselement(root_elem) =}")
# html.tag       ='head'
# element.tag ='head'
# element.tag ='title'
# element.tag ='body'
# etree.iselement(root_elem) =True