#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib


# In[2]:


data = pd.read_csv("tank1_data.csv")


# In[3]:


data.head(2)


# In[4]:


data.describe()


# In[5]:


sns.distplot(data['height'])


# In[7]:


sns.distplot(data['Hourly_averge_flow '])


# In[ ]:


sns.distplot(data['volume'])


# In[15]:


sns.barplot(x = data['HOUR'] , y = data['height'])


# In[ ]:





# In[ ]:





# # Task 1
# # Level to volume conversion

# In[28]:


def level_to_volume(level):
    return 100*level


# # Task 2
# # Low Level Alert trigger when the average hourly volume is below 50% of the total capacity of the tank.
# 

# In[16]:


def threshold_alert(df , i , j , max_capacity):
    threshold_capacity = max_capacity / 2
    average_hourly_volume  = ((df.loc[df['HOUR'][i],'volume'] )+ df.loc[df['HOUR'][j] , 'volume' ])/ 2
    if average_hourly_volume < threshold_capacity:
        return "alert" , average_hourly_volume
    else:
        return "safe mode"


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Task 3
# # Leak Alert trigger if a water level change occurs between the hours of 1 am and 4 am on any day.

# In[18]:


df1 = data[data['HOUR'] == 1] 
df2 = data[data['HOUR'] == 2]
df3 = data[data['HOUR'] == 3]
df4 = data[data['HOUR'] == 4]


# In[19]:


frames = [df1, df2, df3 , df4]

result = pd.concat(frames)
type(result['height'])


# In[20]:


def leak_alert(df):
    flow_column = df['height']
    return (flow_column).values


# In[71]:


for i in range(len(result)):
    for j in range(len(result)):
        if leak_alert(result)[i] != leak_alert(result)[j]:
           # add trigger here


# In[ ]:





# In[ ]:




