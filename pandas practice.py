#!/usr/bin/env python
# coding: utf-8

# # pandas practice
# 
# Pandas is a tool for data processing which helps in data analysis
# 
# it provides functions and methods to efficiently manipulate large datasets
# 
# working wit Bigdata
# 
# data structure in pandas
# 
# series(one-dimensional array)
# dataframe(two dimensional array)

# In[2]:


import pandas as pd 


# In[3]:


print(pd.__version__)


# In[4]:


dataset = pd.read_csv('F:\\New Tech\\python\\dataset\\pokemon_data.csv') 
print(dataset)


# In[18]:


df = pd.read_csv('F:\\New Tech\\python\\dataset\\pokemon_data.csv')
print(dataset.head(3))


# In[19]:


df = pd.read_csv('F:\\New Tech\\python\\dataset\\pokemon_data.csv')
print(dataset.tail(5))


# In[25]:


dataset = pd.read_csv('F:\\New Tech\\python\\dataset\\pokemon_data.txt') 
print(dataset)


# In[26]:


dataset = pd.read_csv('F:\\New Tech\\python\\dataset\\pokemon_data.txt',delimiter='\t') 
print(dataset)


# # Reading Data in pandas

# In[28]:


#read Headers
print(dataset.columns)


# In[32]:


#Read each column
print(dataset['Name'])


# In[31]:


print(dataset['Name'][0:5])


# In[34]:


print(dataset[['Name','Attack']])


# In[36]:


#read each row
print(dataset.iloc[1:4])


# In[39]:


dataset.loc[dataset['Type 1'] == 'Fire']


# In[37]:


#Read a specific location(R,c)
print(dataset.iloc[2,1])


# In[40]:


dataset.describe()


# # Making some changes  to the data

# In[5]:


dataset.head(5)


# In[12]:


dataset['Total'] = dataset['HP'] +dataset['Attack']+dataset['Defense']+dataset['Sp. Atk']+dataset['Sp. Def']+dataset['Speed']
dataset.head(5)


# In[13]:


dataset = dataset.drop(columns=['Total'])
dataset.head(5)


# In[17]:


dataset['Total'] = dataset.iloc[:,4:10].sum(axis = 1)
dataset.head(5)


# In[18]:


dataset.to_csv('modified.csv',index =False)


# # Filtering Data

# In[21]:


dataset.loc[dataset['Type 1'] == 'Grass']


# In[25]:


dataset.loc[(dataset['Type 1'] == 'Grass') & (dataset['Type 2'] == 'Poison')]


# In[26]:


dataset.loc[(dataset['Type 1'] == 'Grass') & (dataset['Type 2'] == 'Poison') & (dataset['HP']>70)]


# In[32]:


new_dataset = dataset.loc[(dataset['Type 1'] == 'Grass') & (dataset['Type 2'] == 'Poison') & (dataset['HP']>70)]

new_dataset.reset_index(drop = True,inplace =True)

print(new_dataset)


# # Conditional Changes

# In[36]:


dataset.loc[dataset['Type 1'] == 'Fire','Type 1'] = 'Flamer'
dataset


# In[40]:


dataset.loc[dataset['Type 1'] == 'Flamer','Type 1'] = 'Fire'
dataset


# In[49]:


dataset.loc[dataset['Type 1'] == 'Fire','Legendary'] = True
dataset


# In[51]:


dataset.loc[dataset['Total'] > 500, ['Generation','Legendary']] = 'TEST VALUE'
dataset


# In[56]:


dataset = pd.read_csv('modified.csv')
dataset


#   # Aggregate Statistics (Groupby)

# In[57]:


dataset = pd.read_csv('modified.csv')
dataset.groupby(['Type 1']).mean()


# In[59]:


dataset = pd.read_csv('modified.csv')
dataset.groupby(['Type 1']).mean().sort_values('Defense',ascending = False)


# In[60]:


dataset = pd.read_csv('modified.csv')
dataset.groupby(['Type 1']).sum()


# In[61]:


dataset = pd.read_csv('modified.csv')
dataset.groupby(['Type 1']).count()


# In[64]:


dataset = pd.read_csv('modified.csv')

dataset['count'] = 1

dataset.groupby(['Type 1']).count()['count']


# In[65]:


dataset = pd.read_csv('modified.csv')

dataset['count'] = 1

dataset.groupby(['Type 1','Type 2']).count()['count']


# # WORKING WITH LARGE AMOUNTS OF DATA

# In[69]:


for dataset in pd.read_csv('modified.csv',chunksize = 5):
    print('chunk dataset')
    print(dataset)


# In[ ]:




