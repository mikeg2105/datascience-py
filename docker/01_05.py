
# coding: utf-8

# ![title](Header__0009_1.png "Header")
# ___
# # Chapter 1 - Data Munging Basics
# ## Segment 5 - Grouping and data aggregation

# In[25]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# ### Grouping data by column index

# In[26]:


address = '~/scripts/mtcars.csv'
cars = pd.read_csv(address)

cars.columns = ['car_names','mpg','cyl','disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']
cars.head()


# In[29]:


# object_name.groupby('Series_name')
# ♔┈♔┈♔┈( WHAT THIS DOES )┈♔┈♔┈♔
# To group a  DataFrame by its values in a particular column, call the .groupby() method off of the DataFrame, and then pass
# in the column Series you want the DataFrame to be grouped by.
cars_groups = cars.groupby(cars['cyl'])
cars_groups.mean()

print(cars_groups.mean())

