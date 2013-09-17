#!/usr/bin/env python2
import sys, codecs, pickle
import os

def print_all(movie, writer):
	for i in movie.keys():
		if not movie[i]:
			writer.write(i+': \n')
		elif type(movie[i]) == str:
			writer.write(i+': '+movie[i]+'\n')
		else:
			print type(movie[i])
			writer.write(i+': '+', '.join(movie[i])+'\n')
	writer.write('-'*100+'\n')
d = pickle.load(open('../tmp/d.pickle', 'rb'))
print 'loaded'
os.system('beep')
writer = open('out.txt','w')
count=0
for i in d.keys():
	count+=1
	print_all(d[i], writer)
