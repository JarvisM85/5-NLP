# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 09:03:47 2023

@author: sahil
"""

import re
sentence5 = "sharad twitted, Wittnessing 70th republic day India from Rajput, Delhi,Mesmorizing performance by Indian Army!"
re.sub(r'([^\s\w]|_)+',' ', sentence5).split()


##########################
# extracting n-grams using custom defined function

import re
def n_gram_extractor(input_str, n):
    tokens = re.sub(r'([^\s\w]|_)+',' ', input_str).split()
    for i in range(len(tokens)-n+1):
        print(tokens[i:i+n])
        
n_gram_extractor("The cute little boy is playing with kittens",2)
n_gram_extractor("The cute little boy is playing with kittens",3)
n_gram_extractor("The cute little boy is playing with kittens",4)

#############################

from nltk import ngrams
#extraction n-grams with nltk
list(ngrams("The cute little boy is playing with kittens".split(),2))
list(ngrams("The cute little boy is playing with kittens".split(),3))

#############################
from textblob import TextBlob
blob = TextBlob("The cute little boy is playing with kittens.")
blob.ngrams(n=2)
blob.ngrams(n=3)

################################################

#Tokenization using Keras
sentence5
from keras.preprocessing.text import text_to_word_sequence
text_to_word_sequence(sentence5)

######################################################################

#Tokenization using TextBlob
from textblob import TextBlob
blob=TextBlob(sentence5)
blob.words

######################################################################

#Tweet Tokenizer
from nltk.tokenize import TweetTokenizer
tweet_tokenizer=TweetTokenizer()
tweet_tokenizer.tokenize(sentence5)

######################################################################

#Multi-word Expression



######################################################################

#Regular expression Tokenizer
from nltk.tokenize import RegexpTokenizer
reg_tokenizer=RegexpTokenizer('\w+|\$[\d\.]+|\S+')
reg_tokenizer.tokenize(sentence5)

######################################################################

#White space tokenizer
from nltk.tokenize import WhitespaceTokenizer
wh_tokenizer=WhitespaceTokenizer()
wh_tokenizer.tokenize(sentence5)

#####################################################################

from nltk.tokenize import WordPunctTokenizer
wp_tokenize=WhitespaceTokenizer()
wp_tokenize.tokenize(sentence5)

#####################################################################

sentence6='I love playing cricket. Cricket players practices hard in  '
from nltk.stem import RegexpStemmer
regex_stemmer=RegexpStemmer('ing$')
' '.join(regex_stemmer.stem(wd) for wd in sentence6.split())

#####################################################################

sentence7='Before eating, it would be nice to sanitize your hands.'
from nltk.stem.porter import PorterStemmer
ps_stemmer=PorterStemmer()
words=sentence7.split()
' '.join([ps_stemmer.stem(wd) for wd in words])

####################################################################

#Lemmatization
import nltk
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize
nltk.download('wordnet')
lemmatizer=WordNetLemmatizer()
sentence8='The codes executrd today are far better than what'
word=word_tokenize(sentence8)
' '.join([lemmatizer.lemmatize(word) for word in words])

####################################################################

#Singularize and Pluralization
from textblob import TextBlob
sentence9=TextBlob('She sells seashells on the seashore')
words=sentence9.words

sentence9.words[2].singularize()
#'seashell'

sentence9.words[5].pluralize()
#'seashores'

##################################################################

#Language translation from spanish to english
from textblob import TextBlob
en_blob=TextBlob(u'muy bien')
en_blob.translate(from_lang='es',to='en')
#TextBlob("very good")

###################################################################

from nltk import word_tokenize
sentence9=TextBlob('She sells seashells on the seashore')
custom_stop_word_list=['She','on','the','am','is']
words=word_tokenize(sentence9)
' '.join


##########################################################
#####################################################
# DATE => 25/11/2023

# Extracting general 

import pandas as pd
df = pd.DataFrame([['The vaccine for covid-19 will be announced on 1st Augest'],
                   ['Do you know how much expections the world population is having from this redearch?'],
                   ['The risk of virus will come to an end on 31st July']])

df.columns=['text']
df

# Now let us measure the number of words
from textblob import TextBlob
df['number_of_words']=df['text'].apply(lambda x:len(TextBlob(x).words))
df['number_of_words']

###################################
# Detect presence of words wh
wh_words = set(['why','who','which','what','where','when','how'])
df['is_wh_words_present'] = df['text'].apply(lambda x:True if len(set(TextBlob(str(x)).words).intersection(wh_words))>0 else False)
df['is_wh_words_present']











df['subjectivity'] = df['text'].apply(lambda x.TextBlob(str(x)).sentiment.subjectivity)
df['subjectivity']