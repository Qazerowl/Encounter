import xml.etree.ElementTree as ET

def load(path):
    return ET.parse(path)

def itemtotal(tree):
    return int(ET.tostringlist(tree.findall('item')[-1])[1].decode('utf-8')[5:][:-1])

def getval(tree,value,number):
    return ET.tostringlist(tree.findall('item/' + value)[number])[2].decode('utf-8')
