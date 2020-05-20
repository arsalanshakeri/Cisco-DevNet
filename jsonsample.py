import json

stream = open('sample.json','r')

#with open('sample.json','r') as stream:
#    jsonstr=stream.read().replace('/n','')

jsonobj = json.load(stream)

print(jsonobj[0]['FirstName'])
#print(type(jsonobj))

#jsonobj=json.loads(stream)

#print(type(jsonobj))