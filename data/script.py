import codecs

with codecs.open("withoutHashTag2.txt","r",encoding='utf-8') as f:
	for line in f:
		l = line.split(",")
		with codecs.open("OriginalTest.txt","a",encoding='utf-8') as o:
			o.write(l[1])
			o.close

