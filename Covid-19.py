# Import the packages we need. 

import pandas as pd
import numpy as np
import statistics

# Reading the downloaded content and turning it into a pandas dataframe
data=pd.read_csv("https://raw.githubusercontent.com/nooraliraeeji/Siemens/main/input/covid_africa.csv")

# creating 2 rank columns and passing the returned rank series
data['Rank Total Cases/1 mil population']= data["Total Cases/1 mil population"].rank(ascending=False)
data['Rank Deaths/1 mil population']= data['Deaths/1 mil population '].rank(ascending=False)

data['severity index']=data['Rank Total Cases/1 mil population']*data['Rank Deaths/1 mil population']

data=data.sort_values(by='severity index')

result=data[['Country','severity index']]
result.to_excel("https://raw.githubusercontent.com/nooraliraeeji/Siemens/main/output/Table1.xlsx",index=False)


# ## Handling Missing value 

data.dropna(inplace=True)

#total recovered in the whole data set
whole_total_recovered=data['Total Recovered'].sum()

#median of total deaths from the whole data set.
median_total_deaths=statistics.median(data['Total Deaths'])

#standard deviation of the total tests from the whole data set.
std_total_tests=statistics.stdev(data['Total Tests'])

data2=data.head(3).copy()

data2['Total recovered/whole_total_recovered']=data2['Total Recovered']/whole_total_recovered
data2['Total Deaths/median_total_deaths']=data2['Total Deaths']/median_total_deaths
data2['Total Tests/std_total_tests']=data2['Total Tests']/std_total_tests

result2=data2[['Country','Total recovered/whole_total_recovered','Total Deaths/median_total_deaths','Total Tests/std_total_tests']]

result2.to_excel("https://raw.githubusercontent.com/nooraliraeeji/Siemens/main/output/Table2.xlsx",index=False)

