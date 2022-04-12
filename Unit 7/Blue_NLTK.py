import nltk
from nltk.corpus import wordnet as wn
# from nltk.book import *
from nltk.corpus import *
import re
# for doc in nltk.corpus.state_union.fileids():
#     print("File name:", doc[:len(doc)-4])
#     current_doc = nltk.corpus.state_union.words(doc)
#     analyzable_doc = nltk.Text(current_doc)
#     print("Concurrence of men: ", analyzable_doc.count("men"))
#     print("Concurrence of women: ", analyzable_doc.count("women"))
#     print("Concurrence of people: ", analyzable_doc.count("people"))

# cfd = nltk.ConditionalFreqDist(
#     (target, fileid[:4])
#     for fileid in nltk.corpus.state_union.fileids()
#         for w in nltk.corpus.state_union.words(fileid)
#             for target in ['men', 'women', 'people']
#                 if w.lower().startswith(target))

# cfd.plot()


# print("\nPart meronyms for car: ")
# print(wn.synset('car.n.01').part_meronyms())
# print()
# print("Substance meronyms for shirt: ")
# print(wn.synset('shirt.n.01').substance_meronyms())
# print()
# print("Member holonyms for elephant: ")
# print(wn.synset('elephant.n.01').member_holonyms(), "\n")

# print(text7.concordance('however'))

# CMU_DICT = cmudict.entries()
# distinct = set()
# print(CMU_DICT)
# count = 0
# last_entry = ""
# for entry in cmudict.entries():
#     if entry[0] not in distinct:
#         distinct.add(entry[0])
#     elif entry[0] != last_entry:
#         last_entry = entry[0]
#         count+=1

# print((count/len(distinct)*100))

# def find_most_common(text):
#     reg = re.compile('^\w*$')
#     fdist1 = FreqDist(text)
#     most_common = fdist1.most_common(200)
#     real_common = []
#     for word, freq in most_common:
#         if word.lower() not in stopwords.words('english'):
#             if reg.match(word):
#                 real_common.append(word)
#     return real_common[:50]

# x = find_most_common(text1)
# print(x)

# bigrams = list(nltk.bigrams(text2))
# fd = FreqDist(bigrams)
# fd = fd.most_common(5000)
# common = [(bigram[0][0], bigram[0][1]) for bigram in fd if (bigram[0][0].isalpha() and bigram[0][0].lower() not in stopwords.words('english') and bigram[0][1].isalpha() and bigram[0][1].lower() not in stopwords.words('english'))]
# print(common[:49])

# l = 0
# count = 0
# for word in wn.all_synsets('n'):
#     l += 1
#     count += len(word.lemmas())

# for word in wn.all_synsets('v'):
#     l += 1
#     count += len(word.lemmas())

# for word in wn.all_synsets('a'):
#     l += 1
#     count += len(word.lemmas())

# print((count/l))

import nltk
# from nltk.book import *
from nltk.corpus import gutenberg
from nltk.corpus import brown
from nltk.corpus import webtext
from nltk.corpus import state_union
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import random
import requests
from nltk.corpus import udhr
import urllib.request
from bs4 import BeautifulSoup

# def zipf_law(text):
#     fdist = FreqDist([w.lower() for w in text if w.isalpha()])
#     fdist = fdist.most_common()                                 # sort the frequency distribution
#                                                                 # note that it converts the type from dict to list
#     rank = []
#     freq = []
#     n = 1                                                     
    
#     for i in range(len(fdist)):
#         freq.append(fdist[i][1])                               
                                                                
#         rank.append(n)
#         n += 1
    
#     plt.plot(rank, freq, 'bs')
#     plt.xscale('log')                                         
   

#     plt.xlabel('word rank')
#     plt.ylabel('word frequency')
#     plt.show()

# zipf_law(brown.words())


# r = requests.get("http://news.bbc.co.uk/")
# soup = BeautifulSoup(r.text, 'html.parser')

# # print(soup.prettify())
# souptext = soup.get_text().split()
# textfromWeb = ""
# for x in range(0, 9):
#     textfromWeb += souptext[x] + " "

# print(textfromWeb)

from nltk.corpus import movie_reviews
documents = [(list(movie_reviews.words(fileid)), category) for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
# print(all_words)
word_features = list(all_words)[:2000]
def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

featuresets = [(document_features(d), c) for (d,c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print(nltk.classify.accuracy(classifier, test_set))
classifier.show_most_informative_features(30)