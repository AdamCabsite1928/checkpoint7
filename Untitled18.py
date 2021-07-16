#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df=pd.DataFrame(exam_data)
df


# In[10]:



df.head(3)


# In[11]:


df.dropna()


# In[18]:


df[["score","name"]]


# In[15]:


print("Original rows:")
print(df)
print("\nAppend a new row:")
df.loc['k'] = [1, 'Suresh', 'yes', 15.5]
print("Print all records after insert a new record:")
print(df)
print("\nDelete the new row and display the original  rows:")
df = df.drop('k')
print(df)


# In[17]:


print("Original rows:")
print(df)
print("\nDelete the 'attempts' column from the data frame:")
df.pop('attempts')
print(df)


# In[26]:


conditions = [
    (df['score'] > 10),
    (df['score'] < 10)
    ]
values = ['1', '0']
df['Success'] = np.select(conditions, values)
df.head()


# In[35]:


df.to_csv("my_data.csv")


# In[ ]:




