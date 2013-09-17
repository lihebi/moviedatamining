#!/usr/bin/env python2

from Queue import Queue
import os, pickle
from sql import connect
import MySQLdb

class Data():
	def __init__(self):
		self.url = []
		self.celebritylist = []
	def dump(self):
		pickle.dump(self.url, open('../tmp/url.pickle', 'wb'))
	def load(self):
		self.url = pickle.load(open('../tmp/url.pickle', 'rb'))
	def getfromdb(self):
		conn = connect()
		cur = conn.cursor()
		cur.execute('select DoubanId from celebrity')
		for r in cur.fetchmany(100000):
			self.celebritylist.append(r[0])
	def fillurl(self):
		for i in self.celebritylist:
			self.url.append('http://movie.douban.com/celebrity/'+i+'/movies')
	def show(self):
		for i in self.url:
			print i
if __name__ == '__main__':
	data = Data()
	data.getfromdb()
	data.fillurl()
	data.show()
