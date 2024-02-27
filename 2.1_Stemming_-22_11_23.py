# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 08:30:20 2023

@author: sahil
"""

## Stemming
stemmer = nltk.stem.PorterStemmer()
stemmer.stem("programming")
stemmer.stem("programming")
stemmer.stem("programming")
stemmer.stem("programming")

###

##Lematization
#Lematizer looks into dictionary Words
nltk.download("wordnet")
from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
lemmatizer.lematize("programed")
lemmatizer.lematize("programs")

lemmatizer.lematize("battling")

lemmatizer.lematize("amazing")


##################################################
##################################################
import nltk
from nltk import word_tokenize

import nltk
nltk.download('punkt')


#DATE => 23/11/23
nltk.download("maxent_ne_chunker")
nltk.download('words')
sentence4 = "We are learning NLP in python by Sanjivani"
##first we will tokenize
words = word_tokenize(sentence4)
words = nltk.pos_tag(words)
i = nltk.ne_chunk(words,binary=True)
[a for a in i if len(a)==1]


####################################################
## sentence tokenization
from nltk.tokenize import sent_tokenize
sent = sent_tokenize("We are learning NLP in Python. Delivered by SanjivaniAI ")
sent

##["We are learning NLP in Python. Delivered by SanjivaniAI " ]

##################################3
import nltk
from nltk import word_tokenize
nltk.download('wordnet')

import nltk
nltk.download('omw-1.4')

from nltk.wsd import lesk
sentence1 = "keep your savings in bank"
print(lesk(word_tokenize(sentence1),'bank'))
## output ==> Synset ('savings_bank.n.02)
sentence2 = "It is so risky to drive over the banks of river"
print(lesk(word_tokenize(sentence2),'bank'))
## output ==> Synset('bank.v.07')


####

#Synset('bank.v.07') a slope in turn of a road or tracks;
# the outside is higher than the inside in order to reduce the 
###
# "bank" as multiple meanings. if you want to find exact meaning
# execute following 





