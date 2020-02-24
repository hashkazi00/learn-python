#!/usr/bin/env python
# coding: utf-8

# # Pandas

# It is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.

# In[1]:


import pandas
pandas.__version__
pdfg="/Users/hashkazi/Desktop/feeds.csv"


# ## Creating a DataFrame

# - Understanding DataFrame format

# In[2]:


import pandas as pd
data = [21,22,23,34,25]
df = pd.DataFrame(data, columns = ['Number'])
print(type(df))
df
x=df[["Number"]]
print(x)


# - List of list method

# In[3]:


data = [['Maths',65],['English',75],['Science',70]]
df = pd.DataFrame(data, columns=['Subject','Marks'], dtype=float)
df


# - Dictionary of list method

# In[17]:


data = {'Subject':['Maths','English','Science'], 'Marks':[65,75,70]}
pd.DataFrame(data)


# - List of dictionary method

# In[4]:


data = [{'Subject':'Maths','Marks':65},{'Subject':'English','Marks':75},{'Subject':'Science','Marks':70}]
df = pd.DataFrame(data)
df


# ## Understanding DataFrames

# In[7]:


d  = {'Names':['Bob','Jessica','Mary','John','Mel','Max'],
      'birthdates':[1968,1955,1977,1978,1973,2001]}
df = pd.DataFrame(data=d)
df
df.head(2)
df.tail(3)


# In[12]:


a=df.columns


# In[13]:


df.index


# ## Pandas Series object

# In[14]:


df['Names']


# In[15]:


print(type(df['Names']))


# In[16]:


df[['Names']]


# In[17]:


print(type(df[['Names']]))


# In[18]:


df[['Names','birthdates']]


# In[20]:


df[['Names',"birthdates"]]


# In[21]:


df


# - Renaming columns

# In[ ]:





# In[22]:


df.columns=['Names','Birthdates']
df


# ## Appending

# In[23]:


#method1
new_data = pd.DataFrame([['Mark',1951]],                        columns = ['Names','Birthdates'])
df=df.append(new_data)
df


# In[30]:


i = [0,1,2,3,4,5,6]
df.index=i
df


# In[31]:


#method2
df.loc[99] = ['Stark',1973]
df


# In[33]:


#method1
new=pd.DataFrame(columns=['Names','Birthdates','Age'])
df = df.append(new)
df


# In[41]:


#method2
df['Sex'] = 'male'
df


# In[42]:


df.loc[0,'age'] = 50
df.loc[3,'Age'] = 40
df.loc[5,'Age'] = 17
df.loc[6,'Age'] = 67
df.loc[1,'Age'] = 63

df.loc[1,'Sex'] = 'female'
df.loc[2,'Sex'] = 'female'
df.loc[7,'Age'] = 57
df


# ## DataFrame indexing and slicing

# In[1]:


df.loc[4:7,"Birthdates":]


# In[1]:


df.loc[df.index[:3],['Names','Sex','Age']]


# In[25]:


df.iloc[0:3]


# In[26]:


df.iloc[0:6:2]


# In[48]:


df.iloc[::-1]


# In[28]:


df


# In[51]:


mydf = df.head()
mydf[[True,False,True,True,False]]


# In[50]:


df


# In[52]:


age_filter = df['Age'] > 30
age_filter


# In[53]:


df[age_filter]


# In[54]:


df[df['Age'] > 30]


# In[55]:


df[df['Age'] < 30]


# In[56]:


age_sex_filter = ((df['Sex'] == 'male') & (df['Age'] > 30))
df[age_sex_filter]


# ## Operations

# In[36]:


df


# In[57]:


df['Age'].max()


# In[58]:


df['Age'].min()


# In[59]:


df['Age'].mean()


# In[60]:


df['Age'].median()


# In[61]:


df['Age'].std()


# In[34]:


df[df['Age'].isnull()]


# In[35]:


df['Age'].sum()


# In[36]:


df['Birthdates'].count()


# In[37]:


df['Birthdates'].value_counts()


# In[70]:


df['Birthdates'].value_counts().index


# ## Plotting

# In[71]:


df['Birthdates'].value_counts().plot(kind='bar')


# In[72]:


df


# In[73]:


mapping = {'male':0,'female':1}
df['Gender']=df['Sex'].apply(lambda x:mapping[x])
df


# In[74]:


import matplotlib.pyplot as plt
plt.xticks(df['Gender'],['male','female'])
plt.bar(df['Gender'],df['Age'], align = 'center', color = 'RY')


# In[75]:


df['Birthdates'].plot(kind='hist')


# In[76]:


df


# In[77]:


df.drop(['Sex'],axis=1, inplace = True)
df


# In[78]:


df1 = df.dropna(subset = ['Age'])
df1


# In[79]:


df.fillna(30)


# In[80]:


df.fillna(df['Age'].mean())


# ## Groupby function

# In[81]:


df


# In[58]:


for name,value in df.groupby('Birthdates'):
    print("***********")
    print(name)
    print("***********")
    print(value)


# In[59]:


df['Birthdates'].unique()


# In[60]:


for name,value in df.groupby('Gender'):
    print("***********")
    print(name)
    print("***********")
    print(value)


# In[61]:


df['Gender'].unique()


# In[10]:


gf=pd.read_csv(pdfg)
gf.head()


# In[15]:


import pandas as banana

df=banana.DataFrame({'a':[11,21,31],'b':[21,22,23]})

df.head()


# In[68]:


import matplotlib.pyplot as plt


# In[69]:


import matplotlib


# In[82]:


import numpy as np


# In[ ]:




