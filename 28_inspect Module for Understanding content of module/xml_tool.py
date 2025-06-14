import xml.etree.ElementTree as ET
from tkinter.font import names

## if we are parsing xml from file.
tree=ET.parse("input.xml")
root=tree.getroot()

## if we want to using xml as string argument
root1=ET.fromstring("""<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>
""" )

print(root.tag,root.attrib)

for each_child in root:
	print(each_child.tag,each_child.attrib)

for neighbor in root.iter('country'):
	print(neighbor.attrib)


for country in root.findall('country'):
	name=country.get('name')
	rank=country.find('rank').text
	print(name,rank)

print(root.findall("."))
print(root.findall("./country/neighbor"))
	root.findall(".//year/..[@name='Singapore']")

