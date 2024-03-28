#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


data = pd.read_csv("spam.csv")


# In[4]:


data


# In[5]:


data.head()


# In[6]:


data.tail()


# In[7]:


data.columns


# In[8]:


data.info()


# In[9]:


data.isnull().sum()


# In[12]:


data['Spam']=data['Category'].apply(lambda x:1 if x=='spam' else 0)
data.head(5)


# In[14]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(data.Message,data.Spam,test_size=0.25)


# In[15]:


from sklearn.feature_extraction.text import CountVectorizer


# In[16]:


from sklearn.naive_bayes import MultinomialNB


# In[17]:


from sklearn.pipeline import Pipeline
clf=Pipeline([
    ('vectorizer',CountVectorizer()),
    ('nb',MultinomialNB())
])


# In[18]:


clf.fit(X_train,y_train)


# In[19]:


emails=[
    'Sounds great! Are you home now?',
    'Will u meet ur dream partner soon? Is ur career off 2 a flyng start? 2 find out free, txt HORO followed by ur star sign, e. g. HORO ARIES'
]


# In[20]:


clf.predict(emails)


# In[21]:


clf.score(X_test,y_test)


# In[ ]:




