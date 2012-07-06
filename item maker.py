import xml.etree.ElementTree as ET

def setelement(theelement, thetext):
    ET.SubElement(newitem, theelement).text = thetext
    
def newelement(whatelement):
    setelement(whatelement, str(input(whatelement + ':   ')))



while True:
    tree = ET.parse('c:\\ENCOUNTER\\ITEMTHING.xml')
    root = tree.getroot()
    weaponTotal = int(ET.tostringlist(tree.findall("item")[-1])[1].decode("utf-8")[5:][:-1])

    newname = str(input("NAME:  "))
    newdesc = str(input("DESCRIPTION :  "))


    newitem = ET.SubElement(root,"item")
    newitem.set("id", str(weaponTotal+1))
    
    setelement("name", newname)
    setelement("desc", newdesc)
    
    ET.ElementTree(root).write("c:\\ENCOUNTER\\ITEMTHING.xml")
