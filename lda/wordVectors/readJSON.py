import json

data = []
tweets = []
#fileName = '/Users/admin/Documents/ML/MLProject/tweets_Politics_Subsample.json'
fileName='/Users/admin/Documents/ML/MLProject/file.txt'
with open(fileName) as f:
    data = f.readlines()

#print data
#with open(fileName, 'r') as f:
#    data = json.load(f)

for item in data:
	tweetText = item.split(',',1)
	#print (tweetText[1])
	tweets.append(tweetText[1])

print tweets
outfile='/Users/admin/Documents/ML/MLProject/lda/tweetText.txt'
f = open(outfile, 'w')
json.dump(tweets, f)
f.close()
