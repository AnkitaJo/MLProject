# -*- coding: utf-8 -*-
import codecs

trumpstring = "trump donald donaldtrump"
berniestring = "sanders bernie berniesanders"
hillarystring = "hillary clinton hillaryclinton"
cruzstring = "cruz ted tedcruz"

with open("originalWithoutHashtags1.txt") as f:
	for l in f:
		line = l.lower()
                s = line.split()
                for s1 in s:
                        if s1 in trumpstring:
                                with codecs.open("trumpTweets.txt","a",encoding='utf-8') as out:
					out.write(line)
					out.close
                        if s1 in berniestring:
                                with codecs.open("bernieTweets.txt","a",encoding='utf-8') as out:
					out.write(line)
					out.close
                        if s1 in hillarystring:
                                with codecs.open("hillaryTweets.txt","a",encoding='utf-8') as out:
					out.write(line)
					out.close				
                        if s1 in cruzstring:
				with codecs.open("cruzTweets.txt","a",encoding='utf-8') as out:
					out.write(line)
					out.close


		 
