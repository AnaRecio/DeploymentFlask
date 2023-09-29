#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression


# In[3]:


data=pd.read_csv("./diabetes.csv")


# In[7]:


data.shape


# In[4]:


data.head()


# In[5]:


data.info()


# In[6]:


data.describe()

data = data.astype(float)


# In[8]:


Outcome_mappings = {0: "Not Diabetic", 1: "Diabetic"}


# In[9]:


X = data.iloc[:, 0:-1]
y = data.iloc[:, -1]


# In[10]:


logreg = LogisticRegression(max_iter=1000)
logreg.fit(X, y)


# In[12]:


def outcome(a, b, c, d, e, f, g, h):
    arr = np.array([a, b, c, d, e, f, g, h]) 
    arr = arr.astype(np.float)
    query = arr.reshape(1, -1)
    prediction = Outcome_mappings[logreg.predict(query)[0]]
    return prediction

# %%
