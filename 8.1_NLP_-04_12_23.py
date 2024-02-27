# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 08:51:23 2023

@author: sahil
"""
import gensim
import pandas as pd
df=pd.read_json('C:/5-NLP/reviews_Cell_Phones_and_Accessories_5.json.gz',lines=True)
df
df.shape
#Simple Preprocessing and Tokenization
review_text=df.reviewText.apply(gensim.utils.simple_preprocess)
review_text

# Let us check first word of each review
review_text.loc[0]

# Let us check first row of the datarame
df.reviewText.loc[0]
# Training the WordZVec Model
model = gensim.models.Word2Vec(window=10,min_count=2,workers=4)
'''
where window is how many words you are going to 
consider as sliding window. You can choose any count, 
min_count- There must minimum 2 words in each sentence.
workers :number of threads. 
'''

# Build Vocabulary
model.build_vocab(review_text, progress_per=1000)
#progress_per : after 1000 words it shows progress
#Train the WordZVec
#it will take time , have patience
model.train(review_text, total_examples=model.corpus_count,epochs=model.epochs)
#Save the Model
model.save("C:/5-NLP/word2vec-amazon-cell-accessories-reviews-short.model")
model.wv.most_similar("bad")
model.wv.similarity(w1="cheap",w2="inexpensive")
model.wv.similarity(w1="great",w2="good")























































































