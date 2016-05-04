from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.sentiment.util import *
from textblob import TextBlob
input = open("/home/madhura/ML_Spring16/MLProject/SentimentAnalysis_NLTK_NB/file.txt").read().splitlines()
n_instances = len(input)
var=[]
for line in input:
    var.append(line.split(",")[1])

allstr=""
for i in var:
    allstr += str(i) + "\n"

textblb = []
for i in var:
    textblb.append(TextBlob(i))

sentiments=[]
for i in textblb:
    sentiments.append(i.sentiment)

polarities=[]
for i in sentiments:
    polarities.append(i[0])

labels=[]
for i in polarities:
     if i>=0.0:
         labels.append("pos")
     else:
         labels.append("neg")

labeled_data = []
for i in range(len(var)):
    labeled_data.append(var[i]+","+labels[i])

temp=""
for s in labeled_data:
    temp += s + "\n"

file1 = open("/home/madhura/ML_Spring16/SentimentAnalysis_NLTK_NB/labeled.txt","w+")
file1.write(temp)
