#!/usr/bin/python2.7
#coding:gbk
#Author:LYC
#Date:2013-5-12
#Mail:saber000@vip.qq.com

import urllib2
import urllib
import re
import thread
import time

message = (u'\u7b2c%d\u9875', u'\u6b63\u5728\u52a0\u8f7d\u4e2d...', u'\u7cd7\u767e\u8fde\u8fde\u770b @LYC', u'\u7528\u6b64\u5de5\u5177\u770b\u7cd7\u767e\u65e0\u56fe\u65e0\u771f\u76f8', u'\u8bf7\u8f93\u5165\u5f00\u59cb\u9875\u6570')

class LYC:
	BgnCharToNoneRex = re.compile("(\t|\n| |<a.*?>|<img.*?>)")
	EndCharToNoneRex = re.compile("<.*?>")
	BgnPartRex = re.compile("<p.*?>")
	CharToNewLineRex = re.compile("(<br>|</p>|<tr>|<div>|</div>)")
	CharToNextTabRex = re.compile("<td>")
	
	replaceTab = [("&lt;","<"),("&gt;",">"),("&amp;","&"),("&amp;","\""),("&nbsp;"," ")]
	
	def Magic(self,x):
		x = self.BgnCharToNoneRex.sub("",x)
		x = self.BgnPartRex.sub("\n    ",x)
		x = self.CharToNewLineRex.sub("\n",x)
		x = self.CharToNextTabRex.sub("\t",x)
		x = self.EndCharToNoneRex.sub("",x)
		
		for t in self.replaceTab:
			x = x.replace(t[0],t[1])
		return x

class DYY:
	def __init__(self,page):
		self.page = page
		self.pages = []
		self.lyc = LYC()
		self.enable = False
	def GetPage(self,x):
		u="http://m.qiushibaike.com/hot/page/" + x
		r=urllib2.urlopen(u)
		t=r.read()
		c = t.decode("u8")
		
		g = re.findall('<div.*?"content".*?title="(.*?)">(.*?)</div>',c,re.S)
		q = []
		for i in g:
			q.append([i[0],i[1].replace("\n","")])
		return q

	def Load(self):
		while self.enable:
			if len(self.pages) < 2:
				try:
					p = self.GetPage(str(self.page))
					self.page += 1
					self.pages.append(p)
				except:pass
			else:time.sleep(1)
		
	def Show(self,q,page):
		for i in q:
			print message[0] % page,i[0]
			print self.lyc.Magic(i[1])
			o = raw_input()
			if o == "quit":
				self.enable = False
				break
	
	def Start(self):
		self.enable = True
		page = self.page
		print message[1]
		thread.start_new_thread(self.Load,())
		while self.enable:
			if self.pages:
				q = self.pages[0]
				del self.pages[0]
				self.Show(q,page)
				page += 1
			else:time.sleep(1)

print message[2]
print message[3]
print message[4]
p = input(">")
dyy = DYY(p)
dyy.Start()
