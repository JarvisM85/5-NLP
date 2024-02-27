# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 08:54:44 2023

@author: sahil
"""

import pandas as pd
#read the dataset
df = pd.read_csv("C:/2-Datasets/Ecommerce_data.csv")
print(df.shape)
df.head(5)
#check the distribution of labels








#checking the results
df.head(5)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_text = train_test_split(df.Text,df.label_num,test_size=0.2,
                                                    random_state=2022,
                                                    stratify=df.label_num)

print("Shape of X_train :",)











