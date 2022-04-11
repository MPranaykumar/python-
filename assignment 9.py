#!/usr/bin/env python
# coding: utf-8

# ##
# We have the min and max temperatures in a city In India for each months of the year.
# We would like to find a function to describe this and show it graphically, the dataset
# given below.
# Task:
# 1.fitting it to the periodic function
# 2.plot the fit
# Data
# Max = 39, 41, 43, 47, 49, 51, 45, 38, 37, 29, 27, 25
# Min = 21, 23, 27, 28, 32, 35, 31, 28, 21, 19, 17, 1
# ##

# In[3]:


import numpy as np
import matplotlib.pyplot as plt


# In[7]:


max_temperature = np.array([39, 41, 43, 47, 49, 51, 45, 38, 37, 29, 27, 25])
min_temperature= np.array([21, 23, 27, 28, 32, 35, 31, 28, 21, 19, 17, 18])
months=np.arange(12)
plt.plot(months,max_temperature,'go')
plt.plot(months,min_temperature,'co')
plt.xlabel('month')
plt.ylabel('min and max temperature')
print('Fitting it to a periodic function')


# In[8]:


from scipy import optimize


# In[10]:


def yearly_temps(times, avg, ampl, time_offset):
    return (avg+ ampl * np.cos((times + time_offset) * 1.8 * np.pi / times.max()))

res_max, cov_max = optimize.curve_fit(yearly_temps, months,
                                      max_temperature,[40, 20, 0])
res_min, cov_min = optimize.curve_fit(yearly_temps, months,
                                      min_temperature, [-40, 20, 0])


# In[14]:


days = np.linspace(0, 12, num=365)

plt.figure()
plt.plot(months, max_temperature, 'go')
plt.plot(days, yearly_temps(days, *res_max), 'm-')
plt.plot(months, min_temperature, 'co')
plt.plot(days, yearly_temps(days, *res_min), 'y-')
plt.xlabel('Month')
plt.ylabel('Temperature')

plt.show()
print("Plotting the fit")


# In[17]:


##This assignment is for visualization using matplotlib:###


# In[15]:


import pandas as pd


# In[20]:


df=pd.read_csv("https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv")


# In[22]:


df.head()


# In[24]:


labels = ['male','female']
sizes = df.sex.value_counts()
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, colors = ['Blue'
,'Red'])
#ax1.axis('equal')
plt.show()


# In[26]:


plt.figure()
cat1 = df[df.sex=='male'].plot.scatter('age', 'fare', color='red',label='male')
df[df.sex=='female'].plot.scatter('age', 'fare',color='blue',label='female'
,ax=cat1)


# In[ ]:




