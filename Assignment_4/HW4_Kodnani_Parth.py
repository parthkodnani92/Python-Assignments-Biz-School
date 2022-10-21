#!/usr/bin/env python
# coding: utf-8

# * Name: Parth Kodnani 
# * Course: BUDT704 
# * Section: 0502
# * Date: 09/22/2021

# # Inc. 5000 Analysis

# In[1]:


# Importing the necessary libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ## Case 1
# 1. Load the data from the file into a data frame with rank denoted as the index.
# 2. Print the total number of companies on the list.
# 3. Print a data frame containing companies ranked within the top 25.

# ### Steps for Case 1
# 1. Using pd.read_excel to import the data file and setting the 'RANK' column as the index.
# 2. Counting the number of companies by using the len() function.
# 3. Displaying the first 25 rows by using loc function.

# In[2]:


dfCompany = pd.read_excel(r'D:\MSIS\Data Processing and Analysis in Python\Homeworks\HW4\HW4_inc5000-2018.xlsx', index_col = 1)
dfCompany.head() # To check whether the dataframe has loaded correctly


# In[3]:


numberCompany = len(dfCompany) # Counting number of companies
print(f'Total Number of Companies: {numberCompany}')


# In[4]:


top25 = dfCompany.loc[:25] # Printing the first 25 companies
top25


# ## Case 2
# 1. Describe and complete two different modifications to achieve tidy data.

# ### Dropping and Renaming Columns
# 1. Checking for columns which have no use in the dataset, we find that column 14 and 15 are useless and hence we drop them.
# 2. Checking for column names which have errors and changing them.

# In[5]:


dropCol = dfCompany.drop(['Unnamed: 14', 'Unnamed: 15'], axis = 1) # To drop columns
dropCol


# In[6]:


renameCol = dropCol.rename(columns={"CITY.1" : "STATE", "STATE" : "STATECODE", "REVENUW" : "REVENUE"}) # To rename columns for better access
renameCol


# ### Dealing with Missing Values
# 1. To find the missing values, we first search the dataset for missing values and sum the missing values for all columns.
# 2. After checking the number and types of missing values, we come to a conclusion that dropping these values wouldn't make such a difference to the dataset.

# In[7]:


renameCol.isna().sum() # To check the total null values present in each column


# In[8]:


null = renameCol.isnull() # To recognize null values
nullAny = null.any(axis = 1) # To check for any null values
nullPrint = renameCol[nullAny] # To put these null values in a dataframe
nullPrint


# In[9]:


# Filling up Null values with the respective values from 'CITY, STATE'
renameCol["STATE"] = renameCol["STATE"].fillna("Colorado")
renameCol["STATECODE"] = renameCol["STATECODE"].fillna("CO")
renameCol["CITY"] = renameCol["CITY"].fillna("Sioux Falls")
renameCol["FOUNDED"] = renameCol["FOUNDED"].fillna("2009")


# In[10]:


dfCleanCompany = renameCol.drop(['CITY, STATE'], axis = 1)
dfCleanCompany


# ## Case 3
# 1. Load the data, HW4_states_by_region.csv into a data frame
# 2. Within the data frame containing companies, create and populate a REGION column using the data from the new data frame just created.

# ### Steps for Case 3
# 1. Importing the dataset first, we rename the columns to keep all column naming conventions same.
# 2. We then merge the two dataframes, via left join, on two columns.
# 3. We check for null values, and eliminate the null values which are present.

# In[11]:


dfRegion = pd.read_csv(r'D:\MSIS\Data Processing and Analysis in Python\Homeworks\HW4\HW4_states_by_region.csv')
dfCleanRegion = dfRegion.rename(columns = {"State" : "STATE", "State Code" : "STATECODE", "Region" : "REGION", "Division" : "DIVISION"})
dfCleanRegion.drop(['DIVISION'], axis = 1, inplace = True)
dfCleanRegion


# In[12]:


dfMerge = pd.merge(left = dfCleanCompany, right = dfCleanRegion, how = "left", left_on = ["STATECODE", "STATE"], right_on = ["STATECODE", "STATE"]) # To join the two datasets using left join
dfMerge


# ## Case 4
# 1. Provide Descriptive Statistics of Revenue.
# 2. What percentage of companies founded prior to 2015 have achieved revenue of at least $50 million?
# 3. Identify one inference you can make based on your observations.

# ### Steps for Case 4
# 1. Filtering the two columns needed. 
# 2. After calculating the descriptive statistics of 'REVENUE', calculating the percentage of companies which achieved atleast 50 million

# In[13]:


revFound = dfMerge[["REVENUE", "FOUNDED","REGION", "INDUSTRY"]] # To filter the two columns that are needed
revFound


# In[14]:


print("------Descriptive Statistics------\n")

print(f'Minimum Revenue:               \t${np.amin(revFound["REVENUE"])}')
print(f'Maximum Revenue:               \t${np.amax(revFound["REVENUE"])}')
print(f'Average Revenue:               \t${np.mean(revFound["REVENUE"]):.2f}')
print(f'Median Revenue:                \t${np.median(revFound["REVENUE"])}')
print(f'Standard Deviation of Revenue: \t${np.std(revFound["REVENUE"]):.2f}\n')


# In[15]:


mil50 = revFound[revFound["REVENUE"] >= 50000000] # To filter out revenues greater than 50million
noOfCompanies = len(mil50)
noOfCompaniesT = len(revFound)

perOfCompanies = (len(mil50) / len(revFound)) * 100 # To find percentage of companies having revenue more than 50million
print(f'Percentage of companies founded prior to 2015 that have achieved revenue of at least $50 million: {perOfCompanies:.2f}%')


# In[16]:


mil50.groupby("INDUSTRY").count().sort_values(by = "REVENUE")


# ### Inferences
# 1. We see that only 13.62% companies have a revenue of $50 million who were found before 2015. Most of these companies were present in the South Region.
# 2. We also see that the top 3 industries are Health, Financial Services and Logistics Transportation, Business and Construction all tied at the 3rd spot.
# 3. We conclude that companies in these domains have the fastest growth and the Southern Region has had the maximum growth in terms of revenue.

# ## Case 5 & 6
# 1. Write a Python function with parameters of data frame, category, value, and a number that specifies the number of rows to display in the result. The function should return a data frame containing the top n rows of companies, based on revenues for a specific value in the category.
# 2. Create data frames for each of the following:
#     a. The top fifteen overall companies
#     b. The top ten companies in the food and beverage industry 
#     c. The top three companies located in New York City 
#     d. The top five companies in Maryland 

# ### Steps for Case 5 & 6
# 1. Creating a function which will return a dataframe with the given conditions.
# 2. When 'category' and 'value', both, are present, creating a dataframe of the value from that category only.
# 2. Otherwise, original dataframe continues.

# In[17]:


def dfTopN(df, category = None, value = None, noRows = 10):
    if category != None and value != None: # Condition to create dataframe only when category and value are present
        topN = df[df[category] == value]

    else:
        topN = df
          
    topN.sort_values(by = ['REVENUE'], ascending = False, inplace = True) # To sort by descending revenues
    
    return topN.iloc[:noRows, :]


# In[18]:


dfTopN(df = dfMerge, noRows = 15)


# In[19]:


dfTopN(df = dfMerge, category = "INDUSTRY", value = "Food & Beverage")


# In[20]:


dfTopN(df = dfMerge, category = "CITY", value = "New York City", noRows = 3)


# In[21]:


dfTopN(df = dfMerge, category = "STATE", value = "Maryland", noRows = 5)


# ## Case 7
# 1. Awards will be given to companies in service industries based on their revenue. This includes any company who is in an industry with a "Services" name included as part of its industry. The top quarter of these companies will be given a Trailblazer award, while companies who didn't make the top quarter, but made the top half will be given a Pioneer award.
# 2. For each company earning an award, provide a data frame showing the company, its rank, its revenue, and which award it will earn, sorted by revenue in descending order.

# In[22]:


# Counting number of Industry types which contain 'Services'
service = dfMerge[dfMerge["INDUSTRY"].str.contains("Services")]
service.sort_values(by = ["REVENUE"], ascending = False)
noService = len(service)
print(noService)


# In[23]:


service = service.reset_index() # Resetting the index to avoid setting the value according to 'Rank'
service["AWARDS"] = pd.Series(["TrailBlazer"] * (len(service)//4)) # Adding a column to the dataframe and adding 'Trailblazer' to first quarter
service


# In[24]:


service.columns = ['RANK', 'URL', 'CITY', 'GROWTH', 'EMPLOYEES', 'COMPANY NAME',
       'WEBSITE', 'STATE', 'STATECODE', 'REVENUE', 'ZIP CODE', 'FOUNDED',
       'INDUSTRY', 'REGION', 'AWARDS']
service.index = service['RANK'] # Setting index back to 'RANK'
service.drop("RANK", axis = 1, inplace =True)


# In[25]:


service = service.iloc[:(len(service)//2), :] # Filtering values upto half of the original dataframe
service = service.fillna({'AWARDS':'Pioneer'}) # Replacing the null values with 'Pioneer'


# In[26]:


service


# ## Case 8
# 1. Doing your own Analysis

# In[27]:


dfStat = dfMerge[["GROWTH", "EMPLOYEES", "STATE", "REVENUE", "INDUSTRY", "REGION"]]
dfStat


# In[28]:


dfStat1 = dfStat.copy()
dfStat1.head(2)


# In[29]:


# Making scatterplot to see the correlation between the two variables
sns.relplot(y = "REVENUE", x = "EMPLOYEES", col = "REGION", data = dfStat1, kind = "scatter")


# In[30]:


plt.ylim([0, 17500000000])
plt.xlim([0, 160000])
sns.regplot(y = "REVENUE", x = "EMPLOYEES", data = dfStat[dfStat1["REGION"] == "Midwest"])


# In[31]:


plt.ylim([0, 17500000000])
plt.xlim([0, 160000])
sns.regplot(y = "REVENUE", x = "EMPLOYEES", data = dfStat[dfStat1["REGION"] == "West"])


# In[32]:


plt.ylim([0, 17500000000])
plt.xlim([0, 160000])
sns.regplot(y = "REVENUE", x = "EMPLOYEES", data = dfStat[dfStat1["REGION"] == "South"])


# In[33]:


plt.ylim([0, 17500000000])
plt.xlim([0, 160000])
sns.regplot(y = "REVENUE", x = "EMPLOYEES", data = dfStat[dfStat1["REGION"] == "Northeast"])


# ### Inferences
# 1. From the first scatterplot, we can see that the employees and revenue are all cluttered in the corner. There are a few outliers present in all of the regions with Revenue and Employees.
# 2. The next 4 plots depict the correlation between the Revenue and Employees. It contains the confidence interval which is depicted by the funnel. The plots have been scaled to the same scale.
# 3. In the Midwest plot, we can that the two variables are correlated. We can also see that the number of employees as compared to the other regions is the lowest. The Revenue consists of one outlier. We can say that the growth of the companies in the Midwest Region is relatively fast. We can be confident that the company will definitely grow.
# 4. The West plot's line is relatively flat. This is because the number of people working in West region is very high. We can observe that the Confidence Interval for the West region is very wide. This is also because of the larger number of employees. We can say that the growth of the companies is slow but we can be confident that the company will definitely grow.
# 5. The South plot has a relatively scattered plot. But the trend line is relatively flat. This indicates that even with more number of employees, the revenue is not as high.
# 6. The Northeast plot has a good growth as depicted in the graph. It consists f=of a few outliers towards the revenue side. This is because the Northeast Region is a business hub and consists of companies with higher revenues.

# I pledge on my honor that I have not given nor received any unauthorized assistance on this assignment."
# #### --Parth Kodnani
