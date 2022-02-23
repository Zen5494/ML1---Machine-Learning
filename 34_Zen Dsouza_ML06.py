#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data=pd.read_json("train.json")


# In[5]:


data.head()


# In[8]:



import mysql.connector


# In[9]:


conn = mysql.connector.connect(host= 'localhost',user= 'root',password= '',database='demo')


# In[11]:


df = pd.read_sql_query('select * from students',conn)


# In[12]:


df.head()


# In[ ]:




