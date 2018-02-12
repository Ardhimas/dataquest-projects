# %%
# Let's setup the environment by importing the libraries we need and running the necessary Jupyter magic so that plots are displayed inline.
#
# Import pandas and matplotlib into the environment.
# Run the Jupyter magic %matplotlib inline so that plots are displayed inline.
# Read the dataset into a DataFrame and start exploring the data.

import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

# Read recent-grads.csv into pandas and assign the resulting DataFrame to recent_grads.
# Use DataFrame.iloc[] to return the first row formatted as a table.
# Use DataFrame.head() and DataFrame.tail() to become familiar with how the data is structured.
# Use DataFrame.describe() to generate summary statistics for all of the numeric columns.

recent_grads = pd.read_csv('/Users/ardy/Documents/dataquest/Guided Project_ Visualizing Earnings Based On College Majors/recent-grads.csv')
print(recent_grads.iloc[0])
print(recent_grads.head())
print(recent_grads.tail())
print(recent_grads.describe())

# Drop rows with missing values. Matplotlib expects that columns of values we pass in have matching lengths and missing values will cause matplotlib to throw errors.
# Look up the number of rows in recent_grads and assign the value to raw_data_count.
# Use DataFrame.dropna() to drop rows containing missing values and assign the resulting DataFrame back to recent_grads.
# Look up the number of rows in recent_grads now and assign the value to cleaned_data_count. If you compare cleaned_data_count and raw_data_count, you'll notice that only one row contained missing values and was dropped.
raw_data_count = recent_grads.shape
recent_grads = recent_grads.dropna()
cleaned_data_count = recent_grads.shape
print(raw_data_count)
print(cleaned_data_count)

# %%
# Generate scatter plots in separate jupyter notebook cells to explore the following relations:
# Sample_size and Median
ax1 = recent_grads.plot(x='Sample_size', y='Median', kind='scatter')
ax1.set_title('Median vs. Sample_size')
# Sample_size and Unemployment_rate
# Full_time and Median
ax3 = recent_grads.plot(x='Full_time', y='Median', kind='scatter')
ax3.set_title('Median vs. Full_time')
# ShareWomen and Median
ax4 = recent_grads.plot(x='ShareWomen', y='Median', kind='scatter')
ax4.set_title('Median vs. ShareWomen')
# Men and Median
ax5 = recent_grads.plot(x='Men', y='Median', kind='scatter')
ax5.set_title('Median vs. Men')
# Women and Median
ax6 = recent_grads.plot(x='Women', y='Median', kind='scatter')
ax6.set_title('Median vs. Women')
# Use the plots to explore the following questions:
# Do students in more popular majors make more money?
# No
# Do students that majored in subjects that were majority female make more money?
# No, they actually make less
# Is there any link between the number of full-time employees and median salary?
# No conclusive link

# %%
# Generate histograms in separate jupyter notebook cells to explore the distributions of the following columns:
# Sample_size
# Median
# Employed
# Full_time
# ShareWomen
# Unemployment_rate
# Men
# Women
# We encourage you to experiment with different bin sizes and ranges when generating these histograms.

cols = ["Sample_size", "Median", "Employed", "Full_time", "ShareWomen", "Unemployment_rate", "Men", "Women"]
fig = plt.figure(figsize=(8,24))
for r in range(8):
    ax = fig.add_subplot(8,1, r+1)
    ax = recent_grads[cols[r]].plot(kind='hist')
    ax.set_title(cols[r])

# Use the plots to explore the following questions:
# What percent of majors are predominantly male? Predominantly female?
# What's the most common median salary range?

# %%
# Import scatter_matrix from pandas.tools.plotting
from pandas.plotting import scatter_matrix
# Create a 2 by 2 scatter matrix plot using the Sample_size and Median columns.
scatter_matrix(recent_grads[['Sample_size', 'Median']])
# Create a 3 by 3 scatter matrix plot using the Sample_size, Median, and Unemployment_rate columns.
scatter_matrix(recent_grads[['Sample_size', 'Median', 'Unemployment_rate']])
# Explore the questions from the last few steps using these scatter matrix plots. You may need to create more scatter matrix plots.

# %%
# Use bar plots to compare the percentages of women (ShareWomen) from the 10 highest paying majors and from the 10 lowest paying majors.
# Trend shows that the percentages of women are higher in the lowest paying majors
recent_grads.head(10).plot.bar(x='Major', y='ShareWomen')
recent_grads.tail(10).plot.bar(x='Major', y='ShareWomen')
# Use bar plots to compare the unemployment rate (Unemployment_rate) from the 10 highest paying majors and from the 10 lowest paying majors.
recent_grads.head(10).plot.bar(x='Major', y='Unemployment_rate')
recent_grads.tail(10).plot.bar(x='Major', y='Unemployment_rate')
# Trend shows that the percentages of unemployment is higher in the lowest paying majors
