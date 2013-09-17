#!/usr/bin/env python2
import pickle
import tools
import os
import time
import urllib
path = '../save/subject'
d = {}
def main():
	count=0
	idlist=[]
	namelist=[]
	for root,dirs,files in os.walk(path):
		for f in files:
			count+=1
			filename = path+'/'+f
			if f=='1470617.html': continue
			if f=='5112313.html': continue
			(ids, names) = tools.getcelebrity(open(filename).read())
			for i in range(len(ids)):
					idlist.append(ids[i])
					namelist.append(names[i])
			result = tools.solve(filename)
			d[count]=result
			if count%100 == 0:
				print count
	print len(idlist)
	print len(namelist)
	pickle.dump(idlist, open('../tmp/idlist.pickle', 'wb'))
	pickle.dump(namelist, open('../tmp/namelist.pickle', 'wb'))
	pickle.dump(d, open('../tmp/d.pickle', 'wb'))

if __name__ == '__main__':
	try:
		main()
	except Exception as e:
		print e
		os.system('beep')
	os.system('beep')
