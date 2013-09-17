#!/usr/bin/env python2
#coding=utf-8

import MySQLdb
import pickle
import time
CREATE_TABLE = 'create table celebrity(DbId varchar(30), DoubanId varchar(30), Name varchar(100))'
def connect():
	conn =  MySQLdb.connect(host='localhost', user='hebi', passwd='', port=3306)
	conn.select_db('test')
	return conn
def create_table(cur):
	cur.execute(CREATE_TABLE)
def insert(cur):
	d = pickle.load(open('celebrity.pickle','rb'))
	print 'loaded'
	count=1
	for key in d.keys():
		cur.execute('insert into celebrity values("%s", "%s", "%s")'%(count, key, d[key]))
		print count
		count +=1
if __name__ == '__main__':
	conn = connect()
	cur = conn.cursor()
	#-------------------------------------------------------
	#create_table(cur)
	insert(cur)
	#-------------------------------------------------------
	conn.commit()
	cur.close()
	conn.close()
