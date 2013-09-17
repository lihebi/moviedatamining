#!/usr/bin/env python2
#coding=utf-8
import MySQLdb, pickle, time, sqltools2, os, re, cPickle
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
SQL_QUERY = 'select dbid, doubanid, imdbid, name, directors, stars, genres, tags, date, runtime, point, ratenumber from movie3'
SQL_QUERY_CELE = 'select dbid, doubanid, name from celebrity'
x = [];movies=[];celes=[]
class Movie:
	def __init__(self, r):
		self.dbid, self.doubanid, self.imdbid, self.name, self.directors, self.stars, self.genres, self.tags, self.date, self.runtime, self.point, self.ratenumber=r
class Celebrity:
	def __init__(self, r):
		self.dbid, self.doubanid, self.name = r
		self.aver=0
		self.sum=0
		self.count=0
def main(cur):
	global x, movies, celes
	cur.execute(SQL_QUERY)
	for r in cur.fetchmany(300000):
		movie = Movie(r)
		if filt(movie):
			movies.append(movie)
	celes = cPickle.load(open('celes.cpickle', 'rb'))
	for cele in celes:
		cele.aver = cele.sum/cele.count
		x.append(cele.aver)
	for cele in celes:
		if cele.aver>9:
			print cele.name
	time.sleep(10)
	count=0
	dCele = createdict(celes)
	x = [cele.aver for cele in celes]
	plt.hist(x, range=(0,10), bins=10, color='r')
	plt.figure(2)
	for lihebi in range(5):
		for movie in movies:
			count+=1
			print count
			stars = movie.stars.split(', ')
			for i in range(len(stars)):
				for j in range(i+1, len(stars)):
					cele1 = getCeleFromName(dCele, stars[i])
					cele2 = getCeleFromName(dCele, stars[j])
					if cele1 and cele2:
						cele1.aver = cele1.aver + (cele2.aver-cele1.aver)*0.3
						cele2.aver = cele2.aver + (cele1.aver-cele2.aver)*0.3
	x = [cele.aver for cele in celes]
	plt.hist(x, range=(0,10), bins=10, color='b')
	plt.show()
def createdict(celes):
	d={}
	for cele in celes:
		d[cele.name] = cele
	return d
def getCeleFromName(dCele, name):
	if dCele.has_key(name):
		return dCele[name]
	else:
		return False
def filt(movie):
	if getnumber(movie.ratenumber)<1000: return False
	if getdate(movie.date)<2000: return False
	return True
def getnumber(ratenumber):
	if ratenumber:
		return int(ratenumber)
	else:
		return 0
def getdate(datestring):
	tmp = re.compile('\d{4}').findall(datestring)
	if tmp: date=tmp[0]
	else: date=0
	return int(date)
def getpoint(pointstring):
	if pointstring:
		point=float(pointstring)
	else:
		point=0
	return point
if __name__ == '__main__':
	(conn, cur) = sqltools2.connect()
	main(cur)
	sqltools2.disconnect(conn, cur)
