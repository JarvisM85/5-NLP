# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 09:56:20 2023

@author: sahil
"""


from bs4 import BeautifulSoup as bs
import requests

link="https://sanjivanicoe.org.in/index.php/contact"

page=requests.get(link)
page

page.content


soup=bs(page.content,'html.parser')
soup

print(soup.prettify())

list(soup.children)

soup.find_all('p')

soup.find_all('div',class_='table')

soup.find_all('p')[1].get_text()

soup.find_all('p')[2].get_text()