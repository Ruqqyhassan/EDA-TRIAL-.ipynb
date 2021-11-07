#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


pip install pandas


# In[4]:


df= pd.read_csv('C:/Users/Hassan-Sodiq/Downloads/StudentsPerformance.csv')


# In[5]:


df.head()


# In[57]:


#In our data set, there are 518 female and 482 male.
df.gender.value_counts()


# In[6]:


#Our data frame has 1000 rows and 8 columns.
df.shape


# In[60]:


#the count of each race/ethnicity
df['race/ethnicity'].value_counts()


# In[68]:


# the count of different lunch
df['lunch'].value_counts()


# In[69]:


df['test preparation course'].value_counts()


# In[7]:


df.gender.value_counts


# In[ ]:





# In[ ]:





# In[8]:


df['gender']


# In[9]:


df.describe()


# In[10]:


df.info


# In[54]:


df['race/ethnicity'].values


# In[11]:


#There are 5 different ethnic groups in the data frame, with group C appearing most and group A appearing least
df['race/ethnicity'].value_counts()


# In[12]:


# 5 unique ethnic groups
df['race/ethnicity'].nunique()


# In[13]:


df['race/ethnicity'].unique()


# In[14]:


df['race/ethnicity'].mode()


# In[16]:


df['race/ethnicity'].describe()


# In[15]:


#mean math score
m= math_mean= df['math score'].mean()
math_mean


# In[80]:


m


# In[50]:





# In[17]:


#mean reading score
r= reading_mean= df['reading score'].mean()
reading_mean


# In[82]:


#mean writing score
w=writing_mean= df['writing score'].mean()
writing_mean


# In[18]:


df.gender.describe()


# 

# In[19]:


#2 unique genders with more female than male
df.gender.value_counts()


# In[132]:


df.parental level of education.value_counts()


# In[21]:


df.('parental_level_of_education')


# In[63]:


#df.parental_level_of_education was not responding, so i had to create my own series.
p=parental_level_of_education= df.iloc[:,2]


# In[64]:


p=parental_level_of_education


# In[65]:


p


# In[90]:


# creating  a data frame of gender against mean of each scores
df.groupby('gender')[['math score','reading score','writing score']].mean()


# In[93]:


df.head()


# In[91]:


# grouping the scores by race/ethnicity
df.groupby('race/ethnicity')[['math score','reading score','writing score']].mean()


# In[94]:


#grouping the scores by test preparation score
df.groupby('test preparation course')[['math score','reading score','writing score']].mean()


# In[95]:


#grouping the scores bylunch
df.groupby('lunch')[['math score','reading score','writing score']].mean()


# In[98]:


df.level of education


# In[1]:


#graphical representation of the data
import matplotlib.pyplot as plt


# In[4]:


import numpy as np
import pandas as pd


# In[5]:


df= pd.read_csv('C:/Users/Hassan-Sodiq/Downloads/StudentsPerformance.csv')


# In[ ]:





# In[ ]:





# In[24]:


import pandas as pd


# In[25]:


from matplotlib import pyplot as plt


# In[26]:


df.gender


# In[27]:


#confusion, just trying things out
female= df[df.gender=='female']


# In[46]:


female


# In[51]:


female['race/ethnicity'].value_counts()


# In[56]:


female['race/ethnicity'].dtype()


# In[52]:


# trial and clear ERROR
female
y=female.iloc[:,5]
x=female.iloc[:,1]
plt.plot(x,y)
plt.show()


# In[ ]:





# In[41]:


#From this bar, it can be inferred that race C has the highest population of students, and race A the lowest.
df['race/ethnicity'].value_counts().plot.bar()


# In[135]:


plt.subplot()
df['race/ethnicity'].value_counts().plot.bar()
plt.subplot()
df['gender'].value_counts().plot.bar()
plt.subplot()
df['lunch'].value_counts().plot.bar()
plt.subplot()
df['test preparation course'].value_counts().plot.bar()
plt.show()


# In[ ]:





# In[42]:


# the population of female student is more than the male.
df['gender'].value_counts().plot.bar()


# In[88]:


#population of students who had standard lunch is more than those who had free/ reduced.
df['lunch'].value_counts().plot.bar()


# In[90]:


# more students had no test preparation course 
df['test preparation course'].value_counts().plot.bar()


# In[91]:


#since the horizontal green line represent the median, the reading score has higher median compared to math score and writing score
#the tiny circles represent outliers, saying students can score really low grades
df.boxplot()


# In[ ]:





# In[93]:


import seaborn as sns


# In[95]:


#mean math score is about 65
sns.displot(df['math score'])


# In[96]:


#mean reading score is about 68
sns.displot(df['reading score'])


# In[97]:


sns.displot(df['writing score'])


# In[114]:


# There is really strong correlation between the 3 scores, as the correlation coefficeients are all greater than 0.8
corr = df.corr()
sns.heatmap(corr, annot=True, square=True)
plt.plot(figsize=(20,8))
plt.show()


# In[99]:


sns.relplot(x='math score', y='writing score', hue='gender', data=df)


# In[100]:


sns.relplot(x='math score', y='writing score', hue='race/ethnicity', data=df)


# In[101]:


sns.relplot(x='math score', y='writing score', hue='lunch', data=df)


# In[117]:


#plot the dataframe
df.plot(x="gender", y=["math score", "reading score"], kind="bar", figsize=(20, 8))
 
# print bar graph
plt.show()


# In[118]:


plt.show()


# In[108]:


df.groupby('parental level of education')[['math score', 'reading score', 'writing score']].mean()


# In[111]:


#the highest scores were by students of parents with higher degree(associate, bachelor's, master's),  this might be because students were getting better support from home, since higher level of education
df.groupby('parental level of education')[['math score', 'reading score', 'writing score']].mean().T.plot(figsize=(10,8))


# In[127]:


#same infromationm as above in horizontak bar graph
df.groupby('parental level of education')[['math score', 'reading score', 'writing score']].mean().plot.barh(figsize=(10,8))


# In[107]:


df.groupby('race/ethnicity')[['math score', 'reading score', 'writing score']].mean()


# In[120]:


df.groupby('race/ethnicity')[['math score', 'reading score', 'writing score']].mean().T.plot(figsize=(12,8))


# In[128]:


#ethnic group E had the average highest scores
df.groupby('race/ethnicity')[['math score', 'reading score', 'writing score']].mean().plot.barh(figsize=(12,8))


# In[121]:


# the large difference is visible in this line graph of the effect of lunch on the rest score. standatrd lunch yielded better result
.df.groupby('lunch')[['math score', 'reading score', 'writing score']].mean().T.plot(figsize=(12,8))


# In[129]:


df.groupby('lunch')[['math score', 'reading score', 'writing score']].mean().T.plot.barh(figsize=(12,8))


# In[122]:


df.groupby('test preparation course')[['math score', 'reading score', 'writing score']].mean().T.plot(figsize=(12,8))


# In[130]:


#those who took the preparation course did better, practice makes perfect.
df.groupby('test preparation course')[['math score', 'reading score', 'writing score']].mean().T.plot.barh(figsize=(12,8))


# In[125]:


df.groupby('test preparation course')[['math score', 'reading score', 'writing score']].mean().plot.bar(figsize=(12,8))


# In[126]:


df.groupby('test preparation course')[['math score', 'reading score', 'writing score']].mean().plot.barh(figsize=(12,8))


# In[123]:


df.groupby('parental level of education')[['math score', 'reading score', 'writing score']].mean().T.plot(figsize=(12,8))


# In[124]:


df.groupby('gender')[['math score', 'reading score', 'writing score']].mean().T.plot(figsize=(12,8))


# In[86]:


df[['gender','math score', 'reading score', 'writing score']]


# In[87]:


df.describe(include='all')

