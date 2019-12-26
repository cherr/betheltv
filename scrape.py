#!/usr/bin/python

import sys
import requests
from dateutil.parser import parse
from bs4 import BeautifulSoup
from string import Template

print ("generating .nfo for %s" % (sys.argv[1]))
page = requests.get("https://www.bethel.tv/watch/%s" % (sys.argv[1]))
soup = BeautifulSoup(page.content, 'html.parser')

d = {
	'id': sys.argv[1],
	'title': soup.find(class_="description__title").get_text(),
	'subtitle': soup.find(class_="description__subtitle").get_text(),
	'author': soup.find(class_="author__name").get_text(),
	'aired': parse(soup.find(class_="description__subtitle").get_text()).date(),
	'text': soup.find(class_="description__text").get_text()
}

filein = open('src.nfo')
src = Template(filein.read())
fileout = open("%s.nfo" % sys.argv[1], "x")
fileout.write(src.substitute(d))
fileout.close()
