import os

import matplotlib_inline
import numpy as np
import pandas as pd

# If certain fields need to be aggregated differently, we can do:
from pprint import pprint

import matplotlib.pyplot as plt

import seaborn as sns

path = r'C:\Users\tyyp-\Desktop\Repository\ML IBM\Explatory Data Analysis For ML\Week 1\Exercise 3\iris_data.csv'
data = pd.read_csv(path)
data.head()

### Q1 BEGIN SOLUTION
# Number of rows
print(data.shape[0])

# Column names
print(data.columns.tolist())

# Data types
print(data.dtypes)

### END SOLUTION
print("### END SOLUTION 1")

### Q2 BEGIN SOLUTION
data['species'] = data.species.str.replace('Iris-', '')
# alternatively
# data['species'] = data.species.apply(lambda r: r.replace('Iris-', ''))

data.head()

### END SOLUTION
print("### END SOLUTION 2")

### Q3 BEGIN SOLUTION
# The number of each species present.
species_counts = data['species'].value_counts()
print(species_counts)

# The mean, median, and quantiles and ranges (max-min) for each petal and sepal measurement.
stats_df = data.describe()
stats_df.loc['range'] = stats_df.loc['max'] - stats_df.loc['min']

out_fields = ['mean', '25%', '50%', '75%', 'range']
stats_df = stats_df.loc[out_fields]
stats_df.rename({'50%': 'median'}, inplace=True)
print(stats_df)
### END SOLUTION
print("### END SOLUTION 3")

### Q4 BEGIN SOLUTION

# The mean calculation
data.groupby('species').mean()
# The meadian calculation
data.groupby('species').median()

# applying multiple functions at once - 2 methods
data.groupby('species').agg(['mean', 'median'])  # passing a list of recognized strings
data.groupby('species').agg([np.mean, np.median])  # passing a list of explicit aggregation functions

agg_dict = {field: ['mean', 'median'] for field in data.columns
            if field != 'species'}
agg_dict['petal_length'] = 'max'
pprint(agg_dict)
data.groupby('species').agg(agg_dict)

### END SOLUTION
print("### END SOLUTION 4")

### Q5 BEGIN SOLUTION
# A simple scatter plot with Matplotlib
ax = plt.axes()
ax.scatter(data['sepal_length'], data['sepal_width'])

# Label the axes
ax.set(xlabel='Sepal Length (cm)',
       ylabel='Sepal Width (cm)',
       title='Sepal Length vs Width')
plt.show()
print("Scatter Plot Has Written")
### END SOLUTION
print("### END SOLUTION 5")

### Q6 BEGIN SOLUTION
# Using Matplotlib's plotting functionality

ax = plt.axes()
ax.hist(data['petal_length'], bins=25)

ax.set(xlabel='Petal Length (cm)',
       ylabel='Frequency',
       title='Distribution of Petal Lengths')

plt.show()
# Alternatively  using Pandas plotting functionality
ax = data['petal_length'].plot.hist(bins=25)

ax.set(xlabel='Petal Length (cm)',
       ylabel='Frequency',
       title='Distribution of Petal Lengths')
plt.show()

### END SOLUTION
print("### END SOLUTION 6")

### Q7 BEGIN SOLUTION
# This uses the '.plot.hist' method
ax = data.plot.hist(bins=25, alpha=0.5)
ax.set_xlabel('Size (cm)')

# To create four seperate plots, use Pandas '.hist' method
axList = data.hist(bins=25)
for ax in axList.flatten():
    if ax.get_subplotspec().is_last_row():
        ax.set_xlabel('Size (cm)')

    if ax.get_subplotspec().is_first_col():
        ax.set_ylabel('Frequency')
plt.show()
### END SOLUTION
print("### END SOLUTION 7")

### Q8 BEGIN SOLUTION
# Here we have four separate plots
data.boxplot(by='species')
plt.show()
### END SOLUTION
print("### END SOLUTION 8")

### Q9 BEGIN SOLUTION
# First we have to reshape the data so there is only
# a single measurement in each column
plot_data = (data.set_index('species')
             .stack()
             .to_frame()
             .reset_index()
             .rename(columns={0: 'size',
                              'level_1': 'measurement'})
             )

plot_data.head()

# Plot the dataframe from above using Seaborn

sns.set_style('white')
sns.set_context('notebook')
sns.set_palette('dark')

f = plt.figure(figsize=(6, 4))
sns.boxplot(x='measurement', y='size',
            hue='species', data=plot_data)
plt.show()
### END SOLUTION
print("### END SOLUTION 9")

### Q10 BEGIN SOLUTION
sns.set_context('talk')
sns.pairplot(data, hue='species')
plt.show()
### END SOLUTION
print("### END SOLUTION 10")
