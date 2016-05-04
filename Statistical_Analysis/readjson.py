# -*- coding: utf-8 -*-
import codecs
import re
import json
from string import punctuation
from pprint import pprint


data = open("input/tweets2.json").read()
tdata = json.loads(data)

for i in range(0, len(tdata)):
	result1 = tdata[i]["tweet_text"]
	#removing the URLs
	result2 = re.sub(r"http\S+", "", result1)

	#with hashtags
	result = re.sub(r'^\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\)#','',result2)
	
	#without hashtags
	#result3 = ''.join(c for c in result2 if c not in punctuation)
	#result4 = re.sub(r'[^\x00-\x7f]',r'', result3)

	#remove extra spaces or lines
	result5 = re.sub('\s+', ' ',result).strip()
	#remove "RT"
	result6 = re.sub("RT",'',result5).strip()
	#make the final string 	
	line = tdata[i]["user_id"] +","+result6+"\n"
	#write the output #id,tweet to the file
	with codecs.open('originalWithHashtags1.txt', 'a', encoding = 'utf-8') as out:
		out.write(line)
		out.close

