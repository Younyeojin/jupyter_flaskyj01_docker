#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


def plot_show():
    plt.title('plotting')
    plt.plot([10, 20, 30, 40])
    plt.show()


# In[3]:


plot_show()


# In[4]:


def plot_two_list_show():
    plt.plot([1, 2, 3, 4], [12, 43, 25, 15])
    plt.show()


# In[5]:


plot_two_list_show()


# In[6]:


def plot_legend():
    plt.title('legend')
    plt.plot([10, 20, 30, 40], label='asc')
    plt.plot([40, 30, 20, 10], label='desc')
    plt.legend()
    plt.show()


# In[7]:


plot_legend()


# In[8]:


def plot_change_color():
    plt.title('color')
    plt.plot([10, 20, 30, 40], color='skyblue', label='skyblue')
    plt.plot([40, 30, 20, 10], 'pink', label='pink')
    plt.legend()
    plt.show()


# In[9]:


plot_change_color()


# In[10]:


def plot_line_style():
    plt.title('linestyle')
    plt.plot([10, 20, 30, 40], color='r', linestyle='--', label='dashed')
    plt.plot([40, 30, 20, 10], color='g', ls=':', label='dotted')
    plt.legend()
    plt.show()


# In[11]:


plot_line_style()


# In[12]:


def scatter():
    plt.title('marker')
    plt.plot([10, 20, 30, 40], 'r.', label='circle')
    plt.plot([40, 30, 20, 10], 'g^', label='triangle up')
    plt.legend()
    plt.show()


# In[13]:


scatter()


# In[ ]:




