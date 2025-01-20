"""
Purpose: Reading(Parsing)XML String
"""
import xml.etree.ElementTree as ET

input_string ="""
<stuff>
  <users>
    <user x = '2'>
        <id>001</id>
        <name>Sanjay</name>
    </user>
    <user x ='7'>
         <id>007</id>
        <name>Sanju</name>
    </user>
  </users>
</stuff>"""

stuff_tree =ET.fromstring(input_string)
nodes = stuff_tree.findall("users")#child level
print(nodes)

nodes = stuff_tree.findall("user")#can't find in child level
print(nodes)

nodes = stuff_tree.findall("users/user")#to check in subchild level
print(nodes)
print('user count:',len(nodes))

for item in nodes:
    print('\nname',item.find('name').text)
    print('id',item.find('id').text)
    print('Attribute:',item.get('X'))