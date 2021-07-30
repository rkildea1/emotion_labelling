#!/usr/bin/env python
# coding: utf-8

# 


import sqlalchemy #pip install mysql-connector and #pip install sqlalchemy
import pandas as pd
import nltk
# import text2emotion as te #pip install text2emotion
from nrclex import NRCLex #pip install nrclex & #pip install nltk
nltk.download('punkt')
import regex as re
import emoji
import text2emotion as te
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from ekphrasis.classes.spellcorrect import SpellCorrector
from ekphrasis.classes.tokenizer import SocialTokenizer
import preprocessor as twp
import random
from nltk.util import ngrams
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.collocations import *




# In[4]:


# import mysql.connector
# df = pd.read_csv("/Users/ronan/OneDrive - Technological University Dublin/Masters/Year 2/Dissertation/Twitter Data Exports/2021/Feb/evening/feb-evening-merged.csv")
# dataFrame   = pd.DataFrame(data=df) 
user1 = "ronankildea@twi-rk"
pass1 = ""
ip1 = "twi-rk.mysql.database.azure.com"
dbname1 = "backup_may31" 


database_username = user1
database_password = pass1
database_ip       = ip1
database_name     = dbname1

engine = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                               format(database_username, database_password, 
                                                      database_ip, database_name))






# In[6]:


#write the table to a dataframe
df = pd.read_sql_table("final_cleaned_set_800",engine)


# In[32]:


myths_1 = ["5G Mobile networks","5G", "Alcohol", "Antibiotics", "Bleach", "Cold weather", "snow", 
"Dexamethasone", "Drugs", "Garlic", "Hand dryers", "Holding your breath", "Hot and humid climates", 
"Hot baths", "Hot peppers", "Houseflies", "Hydroxychloroquine", "Masks", "CO2 intoxication Masks", 
"exercise", "Medicines", "Methanol", "ethanol", "Misinformation", "Mosquitoes", "Older people",
"younger people", "Pneumonia", "Recovery", "Saline", "Shoes", "Sunny", "hot weather", "Supplements",
"Swimming", "Thermal scanners", "Ultra-violet", "bacteria", "antibiotics"]

myths = []
for i in myths_1:
    i = i.lower()
    myths.append(i)


# In[33]:


cleaned_tweets_list = list(df.iloc[:,6])  #turn the column to a series, and to a list 


# In[34]:


my_dict = {}
for myth in myths:
    count = 0
    for tweet in cleaned_tweets_list:
        if myth in tweet:
            count += 1
        else:
            pass
    my_dict[myth] = count
print(my_dict)
               


# In[35]:


tweet_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True) 
tweet_dict


# In[36]:


org_tweets_list = list(df.iloc[:,4])  #turn the column to a series, and to a list 
my_dict = {}
for myth in myths:
    count = 0
    for tweet in org_tweets_list:
        if myth in tweet:
            count += 1
        else:
            pass
    my_dict[myth] = count
               


# In[37]:


org_tweet_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True) 
org_tweet_dict


# In[41]:



print("The ordered dictionary of Myths and Count of Tweets where present: \n\n",org_tweet_dict)

