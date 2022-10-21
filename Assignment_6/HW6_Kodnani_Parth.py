#!/usr/bin/env python
# coding: utf-8

# * Name: Parth Kodnani 
# * Course: BUDT704 
# * Section: 0502
# * Date: 11/21/2021

# # Analysis of Health Inspections Across Prince George's County

# In[2]:


# Importing the necessary libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import re


# ## Data Cleaning
# 1. We check the dataset for unnecesary errors and process them to make it ready for our analysis.
# 2. We create several dummy variables to represent different categories.
# 3. We convert the dates from string objects to datetime objects.
# 4. We process the columns to make them suitable for further analysis.

# ### Case 1
# 1. Read in the data. 
# 2. Create a table of the unique values of Category. Which categories do you believe/observe represent a restaurant? Justify your response. 
# 3. Create a single dummy variable for Restaurant that combines multiple values from Category based on your selections.

# ### Steps for Case 1
# 1. We import the dataset to create a dataframe.
# 2. We check all the unique categories of Establishments and we we try to group those categories which could belong under the 'Restaurant' Tag.
# 3. We identify these categories with a single dummy variable.

# In[3]:


dfFoodInspection = pd.read_csv(r'HW6_pgcounty_food_inspection.csv') # To create a dataframe from given data
dfFoodInspection.head()


# In[4]:


# To find the substitute categories of Restaurants
uniqueSeries = pd.DataFrame(dfFoodInspection['Category'].unique())
uniqueSeries


# ### Observation
# * All types of Fast food stores constitute as a part of Restaurants.
# * Carry out food also usually comes from restaurants/ fast food stores; hence even they can be categorized as a part of Restaurants.
# * Delis and diners can also be considered as a part of Restaurants as these places form a subset of the Restaurant chain.
# * Seafood, Pizza are usually served in restaurants; hence categorizes as part of Restaurants.
# * Coffee Shops, Bakery, Cafeteria, Bar/Lounge can all be considered as a part of the bigger term 'Restaurant'.
# * Delivery-only services can be called a virtual restaurant.
# 
# Ref - https://getsling.com/blog/types-of-restaurants/

# In[5]:


# To create a column with a dummy variable for all the categories falling under the 'Restaurant' bracket
restaurant = ['Restaurant', 'Seafood', 'Ice Cream', 'Coffee Shop', 'Bakery', 'Bar/Tavern/Lounge', 'Cafeteria', 'Pizza', 'Delivery Only', 'Fast Food - Local', 'Buffet', 'Carry-out', 'Fast Food - Chain', 'Fast Food', 'Deli', '@Fast Food', 'Diner', '@Fast Food-Do Not Use']
dfFoodInspection['Restaurant'] = dfFoodInspection['Category'].apply(lambda x: 1 if x in restaurant else 0)


# In[6]:


dfFoodInspection.head()


# ### Case 2
# 1. Convert the Inspection_date column into a datetime column. 
# 2. Create a new column for the year of the inspection. Create a new column for the month of the inspection. Create a column for the year and month. 

# ### Steps for Case 2
# 1. We convert the date column from string to datetime object.
# 2. We slice the date into years, months and year-month.

# In[7]:


dfFoodInspection['Inspection_date'] = pd.to_datetime(dfFoodInspection['Inspection_date']) # To convert to datetime object
dfFoodInspection.head()


# In[8]:


dfFoodInspection['Inspection_year'], dfFoodInspection['Inspection_month'] = dfFoodInspection['Inspection_date'].dt.year, dfFoodInspection['Inspection_date'].dt.month # To create columns with year and month individually
dfFoodInspection.head()


# In[9]:


dfFoodInspection['Year-Month'] = dfFoodInspection['Inspection_date'].dt.to_period('M') # To slice till the date till the month
dfFoodInspection.head()


# ### Case 3
# 1. For each column with the type of compliance (e.g. "Proper Hand Washing"), create a dummy variable, that is, 1 if the establishment is out of compliance and 0 otherwise. Use a NaN value for not applicable. 
# 2. Drop the string columns (retain only the dummy variables). 

# ### Steps for Case 3
# 1. We replace the text into dummy variables for all the different types of compliances.

# In[10]:


# To see the unique categories to check whether any 'NaN' values are present
dfFoodInspection['Food_contact_surfaces_and_equipment'].unique()


# In[11]:


# To replace with dummy variables
dfFoodInspection = dfFoodInspection.replace('In Compliance', 0).replace('Out of Compliance', 1)
dfFoodInspection.head()


# ### Case 4
# 1. Create a new column that contains the number of violations for that inspection (the number of categories where the establishment was not in compliance). 
# 2. Create a dummy variable that is 1 if the establishment is out of compliance in any category.  

# ### Steps for Case 4
# 1. We sum the number of violations for each establishment.
# 2. For the establishments having violations, we identify these categories with a single dummy variable.

# In[12]:


noOfViolations = dfFoodInspection.iloc[:, 10:25].sum(axis = 1) # To sum through all the categories to count number of violations
noOfViolations


# In[13]:


noOfViolations.unique() # To see total number of violations an establishment could have made


# In[14]:


dfFoodInspection['Number_of_violations'] = noOfViolations
dfFoodInspection['No_compliance'] = dfFoodInspection['Number_of_violations'].apply(lambda x: 1 if x > 0 else 0)
dfFoodInspection.tail()


# ### Case 5
# 1. For establishments with multiple inspections, create a new DataFrame in wide format. Keep only the establishment ID, Category, Inspection_date, and number of violations. Make sure category is consistent within ID and resolve any discrepancies if necessary (i.e., each establishment has only one category). Reshape from long to wide (pivot) such that each establishment is a row and you have a column for the date and number of violations for inspection 1, inspection 2, inspection 3, etc. 
#  

# In[34]:


dfMulViolations = dfFoodInspection[['Establishment_id', 'Category', 'Inspection_date', 'Number_of_violations']]
dfMulViolations.sort_values(by = ['Establishment_id'])


# In[28]:


# To create a multilevel index dataframe in the long format
dfMulViolations = dfMulViolations.set_index(['Establishment_id', 'Category', 'Inspection_date']).sort_index(level=['Establishment_id', 'Category', 'Inspection_date'])
dfMulViolations.head(50)


# ## Statistics/Data Grouping

# ### Case 6
# 1. What is the most common type of violation? The compliance categories are not mutually exclusive because one restaurant can have multiple violations. 
# 2. Create a table with the number of violations by violation type. Sort the table from the most common to least common violations. 

# ### Steps for Case 6
# 1. We only filter the violation categories and sum the total number of violations made per category.

# In[64]:


# To sum the number of violations for each column
dfNoOfViolations = dfFoodInspection.iloc[:, 10:25].sum(axis = 0).sort_values(ascending = False)
dfNoOfViolations


# ### Observations
# 1. The most common type of violation is 'Cold_holding_temperature' having 7216 violations.

# ### Case 7
# 1. For establishments with multiple inspections, how many reinspections does it take for an establishment to become compliant? Create a table where each row is the number of inspections a restaurant has had, and the columns are the number of reinspections until the establishment becomes compliant. 
# 2. Write 2-4 sentences with your observations. 

# ### Steps for Case 7
# 1. We create a dummy variable to count the number of dates.
# 2. We create another variable which shows cumulative values of dates of every establishment.
# 3. We use the function transform('max') to use the maximum count of inspections for the given establishment.
# 4. Next we create a variable which sees which establishhment had how many violations.
# 5. Finally, we create a pivot table which has Max Number of Inspections as rows, Cumulative Inspections as columns, and values comprise of the establishments who have compliance.

# In[40]:


dfFoodInspection['Dummy_inspection'] = 1 # To create a dummy column to cumulative sum the Inspection Dates


# In[54]:


dfFoodInspection1 = dfFoodInspection.sort_values(['Inspection_date']).reset_index(drop = True)
dfFoodInspection1['Cumulative_inspection'] = dfFoodInspection1.groupby(['Establishment_id'])['Dummy_inspection'].cumsum(axis = 0)
dfFoodInspection1.head()


# In[48]:


dfFoodInspection1.groupby(by = ['Establishment_id', 'Inspection_date', 'Cumulative_inspection'])['Dummy_inspection'].count()


# In[55]:


dfFoodInspection1['Max_inspection'] = dfFoodInspection1.groupby(by = 'Establishment_id')['Cumulative_inspection'].transform('max')
dfFoodInspection1.head()


# In[50]:


dfFoodInspection1["Compliance"] = dfFoodInspection1['No_compliance'].map(lambda x: 1 if x == 0 else 0)
dfReinspection = dfFoodInspection1.groupby(by = ['Max_inspection', 'Cumulative_inspection'])['Compliance'].sum().to_frame()
dfReinspection.reset_index(inplace = True)
dfReinspection


# In[52]:


dfReinspectionPivot = dfReinspection.pivot_table(index = 'Max_inspection', columns = 'Cumulative_inspection', values = 'Compliance', aggfunc = np.sum)
dfReinspectionPivot


# ### Observations
# * We observe that the maximum number of violations made is usually in the first inspection. And then it drops as the number of inspections increase.

# ### Case 8
# 1. Create a bar graph showing the results of violations from #6. 

# In[65]:


# To create a bar graph which displays the total number of violations per category
sns.set(rc={'figure.figsize':(12,8)})
sns.set_style('white')
axes = sns.barplot(x = dfNoOfViolations.values, y = dfNoOfViolations.index, palette = 'pastel', orient = 'h')
axes.set_title('Number of Violations')
axes.set(ylabel = 'Violations')
for bar, percent in zip (axes.patches, dfNoOfViolations.values):
    text_x = bar.get_width() + 300
    text_y = bar.get_y() + bar.get_height()
    text = f'{percent}'
    axes.text(text_x, text_y, text, fontsize = 15, ha = 'center' , va = 'bottom')


# ### Case 9
# 1. Create a line graph that shows the percent of restaurant inspections that have at least one violation by month and year. 
# 2. Are inspections getting harder or easier over time? Is there a particular month where more restaurants pass? Write 2-4 sentences with your observations. 

# In[36]:


# To plot a line graph showing the percentage of restaurant inspections that have atleast one violation by month and year.
dfRestViolation = dfFoodInspection.loc[dfFoodInspection['Restaurant'] == 1, :]
dfRestViolation.head()


# In[51]:


dfRestViolationPlot = dfRestViolation.groupby(by = 'Year-Month')['No_compliance'].sum()/dfFoodInspection.groupby(by = 'Year-Month')['Restaurant'].sum()*100
dfRestViolationPlot.plot(figsize = (10,4))


# ### Observations
# * From the above graph, we see that the variation along the y-axis is increasing. For the years 2012-2014, The amount of restaurants that violated the rules was around 30% and the broken violations vary according to the different months.
# * During the period 2014-2019, we see that the number of violations made by restaurants is at an all time high, with an average of about 40-45% restaurants and the averages stay there. We see that the violations made are about the same percentage for the entire period with very less variance. Which means that the strictness of the inspections must have dropped, leading to more resturants committing violations.
# * We see that there is a steep drop after 2020, which means that the scrutiny of the restaurants must have gotten stricter on the account of some pressure. The fluctuations are also very high during the period 2020-2022.

# ### Case 10
# 1. Create a map that shows all restaurants. Color the restaurants with at least one violation in red. Are there particular areas with more violations? If there are clusters of violations, either through interactive visualization or by manually inspecting the data, look at the types of violations where there are clusters. Are there any trends? Write 2-4 sentences with your observations. If you did not use an interactive visualization, explain how you explored trends in violation type by area. You may also create a second map showing violation types.

# In[ ]:


# To get the Latitude and Longitude of establishments 
dfFoodInspection['Longitude'] = dfFoodInspection['Location'].str.split(' ').str[1].str.replace('(','', regex=True).astype(float)
dfFoodInspection['Latitude'] = dfFoodInspection['Location'].str.split(' ').str[2].str.replace(')','', regex=True).astype(float)

# To obtain a map that shows all restaurants given dataset. 
map_access_token = 'pk.eyJ1IjoicGtvZG5hbmkiLCJhIjoiY2t3OXZxMjZrMTA2dDJ2cDk0bHYxZG1nNCJ9.T-pTNj5Lz-0wqcVIPv0f_w'
restaurant_map_data = go.Scattermapbox(
        lat = dfFoodInspection.loc[dfFoodInspection['Restaurant'] == 1,'Latitude'],
        lon = dfFoodInspection.loc[dfFoodInspection['Restaurant'] == 1,'Longitude'],
        text = dfFoodInspection['Name'],
        hoverinfo = 'text',
        mode = 'markers',
        marker = dict(
                    color = 'blue',
                    symbol = 'circle',
                    opacity = 0.5
                )
)

# To spot the restaurants having atleast one violation in red color
violation_map_data = go.Scattermapbox(
        lat = dfFoodInspection.loc[((dfFoodInspection['Restaurant']==1) & (dfFoodInspection['Number_of_violations']>0)),'Latitude'],
        lon = dfFoodInspection.loc[((dfFoodInspection['Restaurant']==1) & (dfFoodInspection['Number_of_violations']>0)),'Longitude'],
        text = dfFoodInspection['Name'],
        hoverinfo ='text',
        mode = 'markers',
        marker = dict(
                    color = 'red',
                    symbol = 'circle',
                    opacity = .5
                )
)

restaurant_map_layout = go.Layout(
        title = 'Restaurants',
        mapbox = go.layout.Mapbox(
            accesstoken = map_access_token,
            zoom = 1
        )
    )

restaurant_map = go.Figure(data = [restaurant_map_data, violation_map_data], layout = restaurant_map_layout)
restaurant_map.show()


# ### Observations
# * Above we observe a plot for resturants which have atleast one violations and resturants with no violations.
# * Red dots indicate resturants having atleast one violation and blue indicates resturants with no violations.
# * But we cleary observe that red dots are way more than the blue dots stating there are more resturants with violations.

# "I pledge on my honor that I have not given nor received any unauthorized assistance on this assignment."
# #### --Parth Kodnani
