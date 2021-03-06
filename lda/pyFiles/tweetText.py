documents = []
#fileName='/Users/admin/Documents/pythonworkspace/notebooks/politicalTweetsLDA/finalResults/bernieTweetText.txt'
#with open(fileName) as f:
#    docs = f.readlines()
data = []
tweets=[]
fileName='/Users/admin/Documents/pythonworkspace/notebooks/politicalTweetsLDA/finalResults/trumpResults/trumpTweets.txt'
with open(fileName) as f:
    data = f.readlines()

for item in data:
        tweetText = item.split(',',1)
        #print (tweetText[1])
        tweets.append(tweetText[1])


documents = [s.rstrip() for s in tweets]

from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim

tokenizer = RegexpTokenizer(r'\w+')

# create English stop words list
en_stop = get_stop_words('en')

# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()


#documents = []
# compile sample documents into a list
doc_set = documents

print (len(documents))

# list for tokenized documents in loop
texts = []

# loop through document list
for i in doc_set:
    
    # clean and tokenize document string
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)

    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in en_stop]
    
    # stem tokens
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    
    # add tokens to list
    texts.append(stemmed_tokens)

# turn our tokenized documents into a id <-> term dictionary
dictionary = corpora.Dictionary(texts)
dictionary.save("bernieDictionarySave.dict")
print(len(dictionary))

# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]
gensim.corpora.mmcorpus.MmCorpus.save_corpus('bernieCorpusSave.mm', corpus)
#print(corpus)

ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=5, id2word = dictionary, passes=20,minimum_probability=0.000001)

print(ldamodel.print_topics(num_topics=5))

ldamodel.save('bernieSampleModel.model')

