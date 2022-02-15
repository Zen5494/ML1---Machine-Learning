#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[3]:


df = pd.read_csv('placement.csv')


# In[4]:


df.head()


# In[5]:


plt.scatter(df['cgpa'],df['package'])
plt.xlabel('CGPA')
plt.ylabel('Package(in lpa)')


# In[9]:


cor = df.corr()


# In[11]:


import seaborn as sns

sns.heatmap(cor,annot=True)


# In[13]:


X = df.iloc[:,0:1]
y = df.iloc[:,-1]


# In[14]:


y


# In[15]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=2)


# In[16]:


from sklearn.linear_model import LinearRegression


# In[17]:


lr = LinearRegression()


# In[18]:


lr.fit(X_train,y_train)


# In[19]:


X_test


# In[20]:


y_test


# In[21]:


lr.predict(X_test.iloc[0].values.reshape(1,1))


# In[22]:


lr.predict([[8.58]])


# In[23]:


plt.scatter(df['cgpa'],df['package'])
plt.plot(X_train,lr.predict(X_train),color='red')
plt.xlabel('CGPA')
plt.ylabel('Package(in lpa)')


# In[25]:


m = lr.coef_
m


# In[26]:


b = lr.intercept_
b


# In[27]:


# y = mx + b

m * 8.58 + b


# In[102]:


m * 9.5 + b


# In[28]:


m * 100 + b


# In[ ]:




