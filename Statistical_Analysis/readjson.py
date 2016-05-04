# -*- coding: utf-8 -*-
import codecs
import re
import json
from string import punctuation
from pprint import pprint


data = open("input/tweets1.json").read()
tdata = json.loads(data)

for i in range(0, len(tdata)):
	result1 = tdata[i]["tweet_text"]
	#removing the URLs
	result2 = re.sub(r"http\S+", "", result1)
	result3 = re.sub(r'^\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\)#','',result2)
#	result4 = "".join(i for i in result3 if ord(i)<128 or ord(i) == unicode('#'))
	#remove extra spaces or lines
	result4 = re.sub('\s+', ' ',result3).strip()
	#remove "RT"
	result5 = re.sub("RT",'',result4).strip()
	#make the final string 	
	line = tdata[i]["user_id"] +","+result5+"\n"
	#write the output #id,tweet to the file
	with codecs.open('file1.txt', 'a', encoding = 'utf-8') as out:
		out.write(line)
		out.close

