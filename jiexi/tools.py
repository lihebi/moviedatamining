#!/usr/bin/env python2

import re, os
import sys
import codecs

def solve(filename):
	reader = open(filename)
	content = reader.read()
	doubanid = getdoubanid(filename)
	imdbid = getimdbid(content)
	name = getname(content)
	directors = getdirectors(content)
	stars = getstars(content)
	genres = getgenres(content)
	tags = gettags(content)
	date = getdate(content)
	runtime = getruntime(content)
	point = getpoint(content)
	ratenumber = getnum(content)
	return {'doubanid':doubanid, 'imdbid':imdbid, 'name':name, 'directors':directors, 'stars':stars, 'genres':genres, 'tags':tags, 'date':date, 'runtime':runtime, 'point':point, 'ratenumber':ratenumber}
def getname(content):
	tmp = re.compile('<span\ property="v:itemreviewed">.+</span>').findall(content)[0]
	return re.compile('>.+<').findall(tmp)[0][1:-1]
def getdate(content):
	tmp = re.compile('v:initialReleaseDate.+').findall(content)
	if tmp:
		tmp1 = re.compile('\d{4}-\d{2}-\d{2}').findall(tmp[0])
		tmp2 = re.compile('\d{4}').findall(tmp[0])
		if tmp1:
			return tmp1[0]
		elif tmp2:
			return tmp2[0]
	else:
		try:
			tmp = re.compile('"year">.*<').findall(content)[0]
			return re.compile('\d{4}').findall(tmp)
		except IndexError:
			return ''
def getstars(content):
	l = re.compile('v:starring[^/]+</a>').findall(content)
	return [re.compile('>[^>]*<').findall(i)[0][1:-1] for i in l]
def getdirectors(content):
	pattern = re.compile('v:directedBy.+')
	l = re.compile('v:directedBy.+').findall(content)
	try: return [re.compile('>[^>]+<').findall(li)[0][1:-1] for li in l]
	except IndexError: return []
def getgenres(content):
	l = re.compile('v:genre">[^>]+<').findall(content)
	return [i[9:-1] for i in l]
def getpoint(content):
	return re.compile('v:average">.+').findall(content)[0][11:-9]
def getnum(content):
	l = re.compile('v:votes">.+').findall(content)
	try: return re.compile('>[^>]+<').findall(l[0])[0][1:-1]
	except IndexError: return ''
def gettags(content):
	l = re.compile('movie.douban.com/tag.+</span').findall(content)
	return [re.compile('>[^>]+<').findall(li)[0][1:-1] for li in l]
def getimdbid(content):
	try: return re.compile('>tt\d+<').findall(content)[0][1:-1]
	except IndexError: return ''
def getdoubanid(filename):
	return filename.split('/')[-1].split('.')[0]
def gettaglink(content):
	pattern = re.compile('movie.douban.com/tag/[^\"]*')
	l = pattern.findall(content)
	taglinks=[]
	for li in l:
		if not li in taglinks:
			taglinks.append(li)
	return taglinks
def getcelebrity(content):
	pattern = re.compile('/celebrity/\d+/[^/]*</a>')
	l = pattern.findall(content)
	idlist = []
	namelist = []
	for i in l:
		id = re.compile('/\d+/').findall(i)[0][1:-1]
		if id=='1315280':
			continue
		name = re.compile('>.+</a>').findall(i)[0][1:-4]
		idlist.append(id)
		namelist.append(name)
	return (idlist, namelist)
def getruntime(content):
	try:
		tmp = re.compile('property="v:runtime" content="\d+"').findall(content)[0]
		return re.compile('\d+').findall(tmp)[0]
	except IndexError:
		return ''
if __name__ == '__main__':
	pass
