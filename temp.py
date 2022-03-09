import xml.etree.ElementTree as ET

tree = ET.parse('./xml/colegio.xml')
root = tree.getroot()
print("root tag: ", root.tag)

print(root.find(''))