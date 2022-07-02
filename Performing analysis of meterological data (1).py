#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
get_ipython().run_line_magic('matplotlib', 'inline')


# In[29]:


df = pd.read_csv("https://raw.githubusercontent.com/Abhishek20182/Performing-Analysis-of-Meteorological-Data/main/weatherHistory.csv")


# In[28]:


df.head()


# In[4]:


#shape of Dataset
df.shape


# In[5]:


#Statistical Summary of DataFrame
df.describe()


# In[6]:


#Concise Summary of the DataFrame
df.info()


# In[7]:


#Missing Values on Dataset from String to Date Time
df.isnull().sum()


# In[8]:


#Changing Formatted Date from String to Datetime
df['Formatted Date'] = pd.to_datetime(df['Formatted Date'], utc=True)


# In[9]:


#Now Formatted Date is in Date Time Format
df.info()


# In[10]:


df.sample(20)


# In[11]:


#Checking Wheather this dataset has Duplicate Values or not
sum(df.duplicated())


# In[12]:


#Number of Distinct Observation 
df.nunique()


# In[13]:


#DataFrame for Duplicate Values
df_duplicated = df[df.duplicated()]
df_duplicated


# In[14]:


df_duplicated.shape


# In[15]:


#DataFrame for only NaN Values for exploration.
df_null = df[df.isna().any(axis=1)]
df_null.head(20)


# In[16]:


df_null.tail(20)


# In[17]:


#Droping NaN(Not a Number)
df_target = df.dropna()
df_target.shape


# In[18]:


df_target.info()


# In[19]:


df_target.columns


# In[20]:


df_target = df_target.set_index("Formatted Date")
df_target


# In[21]:


#Creating new DataFrame only for Apparent Temperature and Humidity
df_column = ['Apparent Temperature (C)', 'Humidity']
df_monthly_mean = df_target[df_column].resample("MS").mean() #MS-Month Starting
df_monthly_mean.head()


# In[31]:


sns.set_style("whitegrid")
sns.FacetGrid(df_monthly_mean, height=8).map(plt.scatter, "Apparent Temperature (C)", "Humidity")
plt.show()


# In[32]:


plt.figure(figsize=(14,6))
sns.lineplot(data = df_monthly_mean)
plt.show()


# In[33]:


sns.set_style("whitegrid")
sns.FacetGrid(df_target, hue="Summary", height=8).map(plt.scatter, "Apparent Temperature (C)", "Humidity").add_legend()
plt.show()


# In[34]:


# For Apparent Temperature (C)
sns.FacetGrid(df_target, hue="Summary", height=10).map(sns.distplot, "Apparent Temperature (C)").add_legend()
plt.show()


# In[35]:


# For Humidity
sns.FacetGrid(df_target, hue="Summary", height=10).map(sns.distplot, "Humidity").add_legend()
plt.show()


# In[36]:


Conclusion:
H0 is not accepted because there is no change in Humidity from 2006–2016. So, we will accept the H1.

 


# In[ ]:




