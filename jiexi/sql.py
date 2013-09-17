#!/usr/bin/env python2
#coding=utf-8

import MySQLdb
import pickle
import time
import sqltools2
import os
CREATE_TABLE = 'create table movie3(DbId varchar(30), DoubanId varchar(30), ImdbId varchar(30), Name varchar(100), Directors varchar(300), Stars varchar(300), Genres varchar(300), Tags varchar(300), Date varchar(30), Runtime varchar(30), Point varchar(30), RateNumber varchar(30))'
def create_table(cur):
	cur.execute(CREATE_TABLE)
def insert_all(cur):
	d = pickle.load(open('../tmp/d.pickle', 'rb'))
	d[40311]['tags'].pop()
	print 'loaded'
	os.system('beep')
	for count in d.keys():
		print count, d[count]['doubanid']
		insert_single(cur, d, count)
def insert_single(cur, d, count):
	tup = info_to_tuple(d, count)
	cur.execute(('insert into movie3 values("%s"'+', "%s"'*11+')')%tup)
def info_to_tuple(d, count):
	tup = []
	tup.append(count)
	li = ('doubanid', 'imdbid', 'name', 'directors', 'stars', 'genres', 'tags', 'date', 'runtime', 'point', 'ratenumber')
	for l in li:
		if type(d[count][l]) == str:
			tup.append(d[count][l].replace('"',''))
		else:
			#print d[count][l]
			if not d[count][l]:
				d[count][l] = []
			tup.append((', '.join(d[count][l]).replace('"','')))
	return tuple(tup)
if __name__ == '__main__':
	conn, cur = sqltools2.connect()
	#create_table(cur)
	insert_all(cur)
	sqltools2.disconnect(conn, cur)
