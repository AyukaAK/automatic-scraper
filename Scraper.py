#!/usr/bin/env python
# coding: utf-8

# # Automatic Scrape of BBC website
# 
# https://www.bbc.com/

# In[13]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[14]:


response = requests.get("https://www.bbc.com/")
doc = BeautifulSoup(response.text)


# In[18]:


# Grab all of the media titles
# Make sure to just copy paste from the website .media__title 
titles = doc.select(".media__title a")
titles


# In[19]:


for title in titles:
    print(title.text.strip())


# In[20]:


# Start with an empty list
rows = []

for title in titles:
    # Go through each title, building a dictionary
    # with a 'title' and a 'url'
    row = {}
    
    # title
    row['title'] = title.text.strip()
    # link
    row['url'] = title['href']
    
    # Then add it to our list of rows
    rows.append(row)

# then we're going to make a dataframe from it!!!
df = pd.DataFrame(rows)
df.head()


# In[21]:


df.to_csv("bbc.csv", index=False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




