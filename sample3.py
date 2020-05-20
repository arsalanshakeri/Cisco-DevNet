import xmltodict

stream = open('sample.xml','r')

xml = xmltodict.parse(stream.read())

for e in xml['people']:
    print(e["Person"]["LastName"])
