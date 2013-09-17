#!/usr/bin/env python2
import MySQLdb

def connect(db='test'):
	conn = MySQLdb.connect(host='localhost', user='hebi', passwd='', port=3306)
	conn.select_db(db)
	cur = conn.cursor()
	return (conn, cur)
def disconnect(conn, cur):
	conn.commit()
	cur.close()
	conn.close()
