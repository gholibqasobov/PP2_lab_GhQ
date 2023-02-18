import json

file = open('sample-data.json', 'r')
s = file.read()
file.close()
d = json.loads(s)
imdata = d['imdata']

print("""
Interface Status
================================================================================
DN                                                 Description           Speed      MTU
-------------------------------------------------- -------------------   ------    ------""")

for item in imdata:
    print(item['l1PhysIf']['attributes']['dn'], end='\t')
    print(item['l1PhysIf']['attributes']['descr'], end='\t'*7)
    print(item['l1PhysIf']['attributes']['speed'], end='\t'*2)
    print(item['l1PhysIf']['attributes']['mtu'])

