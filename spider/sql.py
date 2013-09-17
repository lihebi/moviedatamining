#!/usr/bin/env python2
#coding=utf-8

import MySQLdb
import pickle
import time
CREATE_TABLE = 'create table movie(DbId varchar(30), DoubanId varchar(30), ImdbId varchar(30), ChineseName varchar(100), EnglishName varchar(100), Directors varchar(300), Stars varchar(300), Genres varchar(300), Tags varchar(300), Date varchar(30), Point varchar(30), RateNumber varchar(30))'
def connect():
	conn =  MySQLdb.connect(host='localhost', user='hebi', passwd='', port=3306)
	conn.select_db('test')
	return conn
def create_table(cur):
	cur.execute(CREATE_TABLE)
def insert_all(cur):
	d = pickle.load(open('test.dat', 'rb'))
	print 'loaded'
	time.sleep(1)
	for count in d.keys():
		insert_single(cur, d, count)
		print count
def insert_single(cur, d, count):
	tup = info_to_tuple(d, count)
	cur.execute(('insert into movie values("%s"'+', "%s"'*11+')')%tup)
	#print (('insert into movie values("%s"'+', "%s"'*11+')')%tup)
def info_to_tuple(d, count):
	tup = []
	tup.append(count)
	li = ('doubanid', 'imdbid', 'chinesename', 'englishname', 'directors', 'stars', 'genres', 'tags', 'date', 'point', 'ratenumber')
	for l in li:
		if type(d[count][l]) == str:
			tup.append(d[count][l])
		else:
			tup.append(', '.join(d[count][l]))
	return tuple(tup)
if __name__ == '__main__':
	conn = connect()
	cur = conn.cursor()
	#-------------------------------------------------------
	#create_table(cur)
	insert_all(cur)
	#-------------------------------------------------------
	conn.commit()
	cur.close()
	conn.close()
