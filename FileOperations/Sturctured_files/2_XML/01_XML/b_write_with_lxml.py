"""
Purpose: Write an xml file using lxml module 
"""
try:
    from lxml import etree
except ModuleNotFoundError as ex:
    print(repr(ex))
    from os import system

    system("pip install lxml")
    from lxml import etree

# creating lxml file
root = etree.Element("root")

child1 = etree.Element('child1')
root.append(child1)

# another child with text
child2 = etree.Element("child2")
child2.text='some text'
root.append(child2)

xml_str = etree.tostring(root)
print(xml_str)
# b'<root><child1/><child2>some text</child2></root>'

xml_str = etree.tostring(root,pretty_print = True)
print(xml_str.decode('utf-8'))
# b'<root><child1/><child2>some text</child2></root>'
# <root>
#   <child1/>
#   <child2>some text</child2>
# </root>
