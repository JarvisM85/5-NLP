# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 08:51:03 2023

@author: sahil
"""

# How to use TFIDF
import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
corpus = ['The mouse had a tiny little mouse','The cat saw the mouse','The cat catch the mouse','The end of mouse story']
#Step1 : Initialize count vector
cv = CountVectorizer()
# To count the total no. of TF
word_count_vector = cv.fit_transform(corpus)
word_count_vector.shape
# Now next step is to apply IDF
tfidf_transform = TfidfTransformer(smooth_idf=True,use_idf=True)
tfidf_transform.fit(word_count_vector)
# This matrix is in raw matrix form , let us convert into Dataframe
df_idf = pd.DataFrame(tfidf_transform.idf_,index=cv.get_feature_names_out(),columns=["idf_weights"])
# Sort ascending
df_idf.sort_values(by=['idf_weights'])


#################################################################

from sklearn.feature_extraction.text import TfidfVectorizer
corpus = ["Thor eating pizza, Loki is eating pizza, Ironman ate pizza already",
          "Apple is announcing new iphone tomorrow",
          "Tesla is announcing new model-3 tomorrow",
          "Google is announcing new pixel-6 tomorrow",
          "Microsoft is announcing new surface tomorrow",
          "Amazon is announcing new eco-dot tomorrow",
          "I am eating biryani and you are eating grapes"]

#let us create the vectorizer and fit the corpus and transform them according
v = TfidfVectorizer()
v.fit(corpus)
transform_output = v.transform(corpus)
# let's print the vocabulary 

print(v.vocabulary_)
#let's print the idf of each word:
    
all_feature_names = v.get_feature_names_out()

for 


















































































































