#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import csv


# In[4]:


data: [] = list()
data = csv.reader(open('data/202106_202106_population.csv', 'rt', encoding='UTF-8'))


# In[5]:


# print([i for i in data])


# In[6]:


arr = []
[arr.append(int(j)) for i in data if '필동' in i[0] for j in i[3:]]
print([i for i in arr])


# In[7]:


plt.style.use('ggplot')
plt.plot(arr)


# In[ ]:




