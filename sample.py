import xml.etree.ElementTree as ET 

stream = open('sample.xml','r')

xml=ET.parse(stream)

root=xml.getroot()

for e in root:
    for p in e:
        print(ET.tostring(p))

    print("")
#    print(ET.tostring((e)))
#
# 
#     print("")

    print(e.get("Id"))
