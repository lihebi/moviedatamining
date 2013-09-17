#!/usr/bin/env python
import json
import os
'''
h = '{"name":"test",\n"type":{"name":"seq","parameter":["1","2"]}}'
out = open('json.out','w')
out.write(h)
'''
def show_construction(j,depth):
	depth += 1
	if type(j) is str:
		print(j)
		return
	for i in j.keys():
		print('\t'*depth,i,':',end='')
		show_construction(j[i],depth)
h = open('final.json').read()
#h = '{"1":"lihebi","2":{"a":"aa","b":"bb"}}'
s = json.loads(h)
#show_construction(s,0)
#print(s)
#print(s.keys())
#print(s['5']['Info']['genres'])
'''
print(s['name'])
print(s['type']['name'])
print(s['type']['parameter'][1])
'''
