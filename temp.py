import xml.etree.ElementTree as ET
tree = ET.parse('colegio.xml')
root = tree.getroot()
print(root.tag)
primer_nivel = []
segundo_nivel = []
tercer_nivel = []

for child in root:
    for item in child:
        for item2 in item:
            tercer_nivel.append(item2)
        segundo_nivel.append(item)
    primer_nivel.append(child)

print("primer nivel")
for item in primer_nivel:
    print(item.tag)

print("segundo nivel")
for item in segundo_nivel:
    print(item.tag)

print("tercer nivel")
for item in tercer_nivel:
    print(item.tag)