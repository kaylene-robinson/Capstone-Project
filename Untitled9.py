
# coding: utf-8

# # <center> Capstone Project Final Report <center/>
# ## <center> IBM Data Science Professional Certificate <center>
# ## <center> Kaylene Robinson <center/>
# ## <center> December 2019

# ### **1. Introduction**
# ***

# #### 1.1 Background
# Toronto, the capital of Ontario Province, is the most populated city on Canada, with a span of 2,731,571 citizens. Toronto also serves as one of the worlds most diverse place to live and is a primary destinations for Canadian immigrants. 
# 
# As a result, Toronto's geographical locations is split into different municiplaities. Each municipality has a an historical identity and are represented in their names. For example, East York, Etobicoke, Forest HIll, Mimico, and North York are few of hundred neighborhoods in Toronto.
# 
# #### 1.2 Problem
# In this project we examined Toronto neighbohoods to group them into similar clusters. Some factors we determined may influence these clusters were restaurants, events, parks and schools. 
# #### 1.3 Interest
# Those who would potentially intersested in the school may be people looking for new residency, emigrating from a different country, or tourists. This study may help those prospects make a decision on what attributes their new neighborhood have, and can help them make the best choice. 

# ### **2. Data Cleaning & Selection**
# ***
# #### 2.1 Data Sources
# Geographical data for the Toronto neighborhoods was obtained through this Wikipedia link: https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M. 
# 
# We also extracted geographical coordinates of post codes from the following CSV file: http://cocl.us/Geospatial_data. 
# 
# These links contain data that details the locations used to receive information for venues in the area. Following this data, we also requested venue data for each neighborhood using Foursquare API to cluster the neighborhoods. 
# #### 2.2 Data Cleaning
# The data downloaded from the aforementioned sources were combined into one table. Using pandas, the data was coded into a data frame and all rows labeled "Not Assigned" were ignores. Neighborhoods with the dame postal code were merged.
# #### 2.3 Feature Selection
# A table with the postal code, borough, neighborhood, latitude and longitude was created. The table shown below consisted of 103 rows and 5 columns.

# ![image 1](2.3.JPG)

# ### **3. Methodology**
# ***
# #### 3.1 Exploratory Data Analysis
# Using the exploratory data analysis approach, I was able to visualize the dataset and summarize their main characteristics. Once the data was cleaned, features from the data set were identified. To represent the data we used the BeautifulSoup python package to read the Wikipedia data and transform it into a data frame using pandas. 
# 
# We then extracted the CSV file for the geographical coordinates, cleaned this data, and combined it the data frames together.  

# #### 3.2 Data Exploration
# 
# Using the python folium library, we were able to generate a visual map of the Toronto neighborhoods. 
# 

# Using Foursquare API we were able to explore the venues in each neighborhood. We found the top 50 venues of each neighborhood and created a new data frame to display these venues.

# ![Image 2](3.2.JPG)

# ### **4. Results**
# ***
# Below the clusters of each neighborhood are illustrated following with a map pinpointing each neighborhood.

# ![Image 4](Capture.JPG)

# ### **5. Discussion & Observations**
# ***
# Based on the results of the most common venues in each neighborhood, we categorized similar neighborhoods into 6 clusters. Organizing the clusters can help those interested choose which area is best for them.  

# ![Image 3](4.0.JPG)

# ### **6. Conclusion**
# ***
# In this project, we analyzed and prepared data to explore neighborhoods in Toronto. Using K-mean clustering, a machine learning algorithm we were able to cluster each neighborhood. Also, we provided suggestions to those who would be interested in living or traveling in Toronto.
# Furthermore, one may be able to use other algorithms as a means to cluster neighborhood and may compare the different results of each algorithm.
