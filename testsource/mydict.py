#!/usr/bin/env python
from bs4 import BeautifulSoup  
import tornado.httpclient  
cli=tornado.httpclient.HTTPClient()  
link='http://www.iciba.com/'  
search=input('search: ')  
link+=search  
data=cli.fetch(link)  
body=data.body.decode('utf8')  
soup=BeautifulSoup(body)  
group=soup.find_all(class_='group_pos')  
group2=group[0].find_all('p')  
for ele in group2:  
	print(ele.find(class_='fl').get_text())  
	result=ele.find_all('label')  
	for r in result:  
		print(r.get_text())  
