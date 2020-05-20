import xmltodict

stream = open('sample.xml','r')

xml = xmltodict.parse(stream.read())

for e in xml['people']['Person']:
    print(e[1])
