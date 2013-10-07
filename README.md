moviedatamining
===============

Use to crawl the movies' meta data from http://movie.douban.com, format and extract useful information as well as analysizing the data.

Language
========
python

Libraries & Tools
=================
Scipy, Matplotlib, BeautifulSoup4, Mysql.

Codes Structure
===============
Spide: it contains the codes for spiders, the worker to crawl data from the web. Use proxy and multi-thread.
Jiexi: Extract data from html pages downloaded, use regular expression and some xml library like beautifulsoup4.
Shuju: codes here are used to analysize data. Use scipy and matplotlib.
