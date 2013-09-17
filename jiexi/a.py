#!/usr/bin/env python2
import pickle
import sqltools2
import os
SQL_TEXT = 'insert into celebrity values("%s","%s","%s")'

def main(cur):
	sql = getStr(2000)
	cur.execute(sql);
def getStr(num):
	tmp='create table python('
	for i in range(num):
		tmp += 'd'+str(i)+' double,'
	return tmp[:-1]+')'
if __name__ == '__main__':
	conn, cur = sqltools2.connect()
	main(cur)
	sqltools2.disconnect(conn, cur)
