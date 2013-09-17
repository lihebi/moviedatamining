#!/usr/bin/env python2.7
#coding=utf-8
import MySQLdb
import json
#conn = MySQLdb.connect(host='localhost',user='root',passwd='lihebi',db='db',port=3306,charset='gb2312')
'''
conn = MySQLdb.connect(host='localhost',user='root',passwd='lihebi',port=3306)
conn.select_db('python_db')
cur = conn.cursor()
'''
h = open('zjson.out').read()
j = json.loads(h)
'''
for i in j.keys():
	print(j[i]['Info'].keys())
	print(j[i]['Info']['name'])
	print(j[i]['rating'].keys())
'''
'''
try:
	cur.execute('create table test(name varchar(100))')
except:
	print'already exist'
	pass
for i in j.keys():
	print('insert into test values("'+j[i]['Info']['name']+'")')
	cur.execute('insert into test values("'+j[i]['Info']['name']+'")')
'''
'''
cur.execute('select name from movie')
results = cur.fetchmany(4)
for r in results:
	for i in r:
		print(i)
	print(type(r))
'''
'''
conn.commit()
cur.close()
conn.close()
'''
