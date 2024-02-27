# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 08:22:14 2023

@author: sahil
"""

#         20 November 2023

'''
                    NATURAL LANGUAGE PROCESSING
                    ===========================
'''

sentence='we are learning TextMining from Sanjivani AI'
#If we want to know position of learning
sentence.index('learning')
#It will show learning in at position 7

#######################################################################

sentence.split().index('TextMining')
#It will split the words in list and count the position if you want to see
#the list select sentence.split() and it will show at 3

#######################################################################

#Suppose we want to print any word in reverse order
sentence.split()[2][::-1]

#######################################################################

#Suppose we want to print first and last word of sentence 
words=sentence.split()
first_word=words[0]
first_word
last_word=words[-1]
last_word

#Now we want to concat the first and last word
concat_word=first_word+' '+last_word
concat_word

#######################################################################

#Suppose we want to print even words from the sentences
[words[i] for i in range(len(words)) if i%2==0]

#######################################################################

sentence
#Now we want to display only AI
sentence[-2:]   #Only AI
sentence[-3:]   #AI with space before

#######################################################################

#Display entire sentence in reverse order
sentence[::-1]

#######################################################################

#Suppose we want to select each word and print in reverse order
words
print( " ".join(word[::-1]for word in words))

######################################################################

#Tokenization
import nltk
nltk.download('punkt')
from nltk import word_tokenize
words=word_tokenize('I am reading NLP Fundamentals')
print(words)



import nltk
nltk.download('punkt')

#Parts of speech(PoS) tagging
nltk.download('average_percentage_tagger')
nltk.pos_tag(words)

#####################################################################
#Stop words for nltk library
from nltk.corpus import stopwords
stop_words=stopwords.words('English')

print(stop_words)
sentence1='I am learning NLP:It is one of the most popular library'
#First will tokenize the sentence
sentence_words=word_tokenize(sentence1)
print(sentence_words)
#Now let us filter the sentence using stop_words
sentence_no_stops=' '.join([words for words in sentence_words])
print(sentence_no_stops)
sentence1

####################################################################

#Suppose we wnat to replace words in string
sentence2='I visited MY from IND on 14-02-19'
normalized_sentence=sentence2.replace('MY','Malaysia').replace('IND','India').replace('-19','-2020')
print(normalized_sentence)

####################################################################

pip install autocorrect

from autocorrect import Speller
spell=Speller(lang='en')
spell('English')