"""
Purpose: XML
         - It is an extensible markup Language
         - desgined to store and transport data

XML vs HTML
   - XML : It is used to store and transport data.So, the XML is an Compiler
   - HTML : It is used to format and display the same data.
"""

import xml

# print(dir(xml))

import xml.etree.ElementTree as ET# xml is so big that's why we are import Element Tree
from xml.dom import minidom
"""
Minidom: - used as etree but this can be used to write 
            xml file very easily by importing minidom.
"""

root = ET.Element('root')
child = ET.SubElement(root,'child')# root is parent and child object is child
child.text = " Iam first child"

child2= ET.SubElement(root,'child2')
child2.text="Iam your second child"

# to display the xml string
result_str=ET.tostring(root)
print(result_str)
# decode_str = result_str.decode('utf-8')

# <root><child> Iam first child</child><child2>Iam your second child</child2></root>'

result_str2 = minidom.parseString(ET.tostring(root)).toprettyxml()
print(result_str2)
# <root>
#         <child> Iam first child</child>
#         <child2>Iam your second child</child2>
# </root>

# writing to a file
with open('write_a_xml.xml','w') as fh:
    # fh.write('decode_str')
    fh.write('result_str')









