# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 08:37:24 2023

@author: sahil
"""

from bs4 import BeautifulSoup as bs
import requests
link = 'https://www.flipkart.com/zebronics-zeb-pixaplay-18-3800-lm-remote-controller-portable-dolby-audio-e-focus-1080p-dual-band-wifi-wireless-screen-mirroring-bluetooth-5-1-app-download-android-smart-projector/p/itm9c5698bd20f7d?pid=PROGMY7YW5GEJFUD'
page = requests.get(link)
page
page.content
soup = bs(page.content, 'html.parser')
print(soup.prettify())
title = soup.find_all('p',class_="_2-NBzT")
title
review_title=[]
for i in range(0,len(title)):
    review_title.qppend(title[i].get_text())
review_title
len(review_title)

## got 10 reivew titles
## Let us Scrap reting 
     
rating = soup.find_all('div',class_='_3LWZlK _1BlPMq')
rating
rate = []
for i in range(0,len(rating)):
    rate.append(rating[i].get_text())
rate
len(rate)
rate.append('')
rate.append('')
rate.append('')
len(rate)

##########

# Now let us scrap the review body
review = soup.find_all('div',class_='t-ZTKy')
review
review_body=[]
for i in range(0,len(review)):
    review_body.append(review[i].get_text())
review_body
len(review_body)

### We got 10 review_body
### Now we have to save 
import pandas as pd
df = pd.DataFrame()
df['Review_Title'] = review_title
df['Rate'] = rate
df['Review'] = review_body
df


######################
## To create .csv file
df.to_csv("C:/5-NLP/flipkart_reviews.csv",index = True)
#######################
# Sentiment analysis
import pandas as pd
from textblob import TextBlob
sent = "This is very excellent garden"
pol = TextBlob(sent).sentiment.polarity
pol
df = pd.read_csv("C:/5-NLP/flipkart_reviews.csv")
df.head()
df['polarity'] = df['Review'].apply(lambda x:TextBlob(str(x)).sentiment.polarity)
df['ploarity']








































