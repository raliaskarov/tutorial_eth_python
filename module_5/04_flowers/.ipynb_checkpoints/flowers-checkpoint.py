#!/usr/bin/env python
# coding: utf-8

# In[67]:


import time
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
from sklearn.cluster import KMeans



# In[68]:


# output folder
import os
os.makedirs("./cx_out", exist_ok=True)


# In[69]:


# Load data


# In[70]:


dataset = datasets.load_iris()


# In[71]:


print(dataset['DESCR'])


# In[72]:


data = pd.DataFrame(dataset['data'], columns=dataset['feature_names'])
data['target'] = dataset['target']


# In[73]:


print(data.info())
print(data.describe())
print(data.head(3))


# In[74]:


data


# In[75]:


## Pair plot


# In[ ]:





# In[76]:


rel1 = sns.pairplot(data, hue='target', diag_kind='hist')
rel1.savefig('./cx_out/pair1.png')


# In[77]:


## Push to Class


# In[78]:


# define class
class Flower:
    def __init__(self, petal_width, petal_length, sepal_width, sepal_length):
        self.petal_width=petal_width
        self.petal_length=petal_length
        self.sepal_width=sepal_width
        self.sepal_length=sepal_length

    def petal_area(self):
        return self.petal_width * self.petal_length

    def sepal_area(self):
        return self.sepal_width * self.sepal_length

# push data to class
petal_areas = []
sepal_areas = []
for i in range(data.shape[0]):
    flower = Flower(petal_width=data.loc[i,"petal width (cm)"],
                      petal_length=data.loc[i,"petal length (cm)"],
                      sepal_width=data.loc[i,"sepal width (cm)"],
                      sepal_length=data.loc[i,"sepal length (cm)"]
                     )
    petal_area = flower.petal_area().item()
    sepal_area = flower.sepal_area().item()
    petal_areas.append(petal_area)
    sepal_areas.append(sepal_area)


# In[82]:


# add columns to df
data["sepal area (cm2)"] = sepal_areas
data["petal area (cm2)"] = petal_areas


# In[83]:


data


# In[84]:


rel2 = sns.pairplot(data, hue='target', diag_kind='hist')
rel2.savefig('./cx_out/pair2.png')


# In[85]:


# save to python
get_ipython().system('jupyter nbconvert --to script leisure_behavior.ipynb')

