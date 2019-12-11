import os
import re
from bs4 import BeautifulSoup as bs
import sys

for c,d,fs in os.walk(sys.argv[1]):
	if c[len(c)-1]!='/':
		c=c+'/'
	for f in fs:
		try:
			if re.search("\.html$",f):
				with open(c+f,"r") as f_:
					soup=bs(f_.read(),"html.parser")
				title=soup.find_all("title")[0]
				os.rename(c+f,c+re.search("^[^.]+",f).group()+"_"+title.text+".html")
		except Exception as e:
			print(e)
