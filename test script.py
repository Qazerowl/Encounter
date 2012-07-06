import xml.etree.ElementTree as ET

tree = ET.parse('c:\\ENCOUNTER\\ITEMTHING.xml')


weaponTotal = int(ET.tostringlist(tree.findall("item")[-1])[1].decode("utf-8")[5:][:-1])

def getstat(statname, number):
    return ET.tostringlist(tree.findall("item/" + statname)[number])[2].decode("utf-8")

print("What do you want to fight with?")
for weapon in range(weaponTotal):
    weapon = int(weapon)
    print (str(weapon+1) + ": " + getstat("name",weapon))
weapon = int(input(""))-1

weaponname = getstat("name",weapon)
weapondesc = getstat("desc",weapon)

print("You are weilding a " + weaponname + ", " + weapondesc + ".")
