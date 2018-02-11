# Import the pandas package.
# Use the pandas.read_csv() function to read the thanksgiving.csv file in.
# Make sure to specify the keyword argument encoding="Latin-1", as the CSV file isn't encoded normally.
# Assign the result to the variable data.
# Display the first few rows of data to see what the columns and rows look like.
# In a separate notebook cell, display all of the column names to get a sense of what the data consists of.
# You can use the pandas.DataFrame.columns property to display the column names.
import pandas as pd
data = pd.read_csv('/Users/ardy/Documents/dataquest/Guided Project_ Analyzing Thanksgiving Dinner/thanksgiving.csv', encoding="Latin-1")
print(data.head())
print(data.columns)

# Use the pandas.Series.value_counts() method to display counts of how many times each category occurs in the Do you celebrate Thanksgiving? column.
# Filter out any rows in data where the response to Do you celebrate Thanksgiving? is not Yes. At the end, all of the values in the Do you celebrate Thanksgiving? column of data should be Yes.
do_you_celebrate = data['Do you celebrate Thanksgiving?']
print(do_you_celebrate.value_counts())
data = data[data['Do you celebrate Thanksgiving?'] == 'Yes']
print(data['Do you celebrate Thanksgiving?'].value_counts())

# Use the pandas.Series.value_counts() method to display counts of how many times each category occurs in the What is typically the main dish at your Thanksgiving dinner? column.
# Display the Do you typically have gravy? column for any rows from data where the What is typically the main dish at your Thanksgiving dinner? column equals Tofurkey.
# Create a filter that only selects rows from data where What is typically the main dish at your Thanksgiving dinner? equals Tofurkey.
# Select the Do you typically have gravy? column, and display it.
print(data['What is typically the main dish at your Thanksgiving dinner?'].value_counts())
main_dish_tofurkey = data[data['What is typically the main dish at your Thanksgiving dinner?'] == 'Tofurkey']
print(main_dish_tofurkey['Do you typically have gravy?'])

# Generate a Boolean Series indicating where the Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple column is null. Assign to the apple_isnull variable.
# Generate a Boolean Series indicating where the Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin column is null. Assign to the pumpkin_isnull variable.
# Generate a Boolean Series indicating where the Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan column is null. Assign to the pecan_isnull variable.
# Join all three Series using the & operator, and assign the result to ate_pies.
# Display the unique values and how many times each occurs in the ate_pies column.

apple_isnull = pd.isnull(data['Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Apple'])
pumpkin_isnull = pd.isnull(data['Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pumpkin'])
pecan_isnull = pd.isnull(data['Which type of pie is typically served at your Thanksgiving dinner? Please select all that apply. - Pecan'])
ate_pies = apple_isnull & pumpkin_isnull & pecan_isnull
print(ate_pies.value_counts())

# Write a function to convert a single string to an appropriate integer value. This will allow us to convert the values in the Age column to integers.
# Use the isnull() function to check if the value is null. If it is, return None.
# Split the string on the space character (), and extract the first item of the resulting list.
# Replace the + character in the result with an empty string to remove it.
# Use int() to convert the result to an integer.
# Return the result.
# Use the pandas.Series.apply() method to apply the function to each value in the Age column of data.
# Assign the result to the int_age column of data.
# Call the pandas.Series.describe() method on the int_age column of data, and display the result.
# In a separate markdown cell, write up your findings.
# Is there anything that we should be aware of about the results or our methodology?
## They are grossly inaccurate
# Is this a true depiction of the ages of survey participants?
## No, the values are all rounded down

def convert_age_str_to_int(age):
    if pd.isnull(age):
        return None
    int_age = int(age.split(' ')[0].replace('+', ''))
    return int_age

data['int_age'] = data['Age'].apply(convert_age_str_to_int)
data['int_age'].describe()

# Write a function to convert a single string to an appropriate integer income value.
# Use the isnull() function to check if the value is null. If it is, return None.
# Split the string on the space character (), and extract the first item of the resulting list.
# If the result equals Prefer, return None.
# Replace the $ and , characters in the result with empty strings to remove them.
# Use int() to convert the result to an integer.
# Return the result.
# Use the pandas.Series.apply() method to apply the function to each value in the How much total combined money did all members of your HOUSEHOLD earn last year? column of data.
# Assign the result to the int_income column of data.
# Call the pandas.Series.describe() method on the int_income column of data, and display the result.
# In a separate markdown cell, write up your findings.
# Is there anything that we should be aware of about the results or our methodology?
# They are very generalized and inaccurate.
# Is this a true depiction of the incomes of survey participants?
# No as it is rounded down.

def convert_income_str_to_int(income):
    if pd.isnull(income):
        return None
    first_char = income.split(' ')[0]
    if first_char == 'Prefer':
        return None
    stripped_dollar = income.split(' ')[0].replace('$', '')
    stripped_all = stripped_dollar.replace(',', '')
    return int(stripped_all)

data['int_income'] = data['How much total combined money did all members of your HOUSEHOLD earn last year?'].apply(convert_income_str_to_int)
data['int_income'].describe()

# See how far people earning under 150000 will travel.
# Filter data, and only select rows where int_income is less than 150000.
# Use indexing to select the How far will you travel for Thanksgiving? column.
# Use the value_counts() method to count up how many times each value occurs in the column.
# Display the results.
# See how far people earning over 150000 will travel.
# Filter data, and only select rows where int_income is greater than 150000.
# Use indexing to select the How far will you travel for Thanksgiving? column.
# Use the value_counts() method to count up how many times each value occurs in the column.
# Display the results
# Write up your findings in a markdown cell.
# The findings dictate that for the wealthier group, a larger proportion are hosting thanksgiving at their home.
income_less_than_150000 = data[data['int_income'] < 150000]
how_far_less_counts = income_less_than_150000['How far will you travel for Thanksgiving?'].value_counts()
print(how_far_less_counts)

income_over_150000 = data[data['int_income'] > 150000]
how_far_over_counts = income_over_150000['How far will you travel for Thanksgiving?'].value_counts()
print(how_far_over_counts)

# Generate a pivot table showing the average age of respondents for each category of Have you ever tried to meet up with hometown friends on Thanksgiving night? and Have you ever attended a "Friendsgiving?.
# Call the pivot_table() method on data.
# Pass in "Have you ever tried to meet up with hometown friends on Thanksgiving night?" to the index keyword argument.
# Pass in 'Have you ever attended a "Friendsgiving?"' to the columns keyword argument.
# Pass in "int_age" to the values keyword argument.
# Display the results.
# Generate a pivot table showing the average income of respondents for each category of Have you ever tried to meet up with hometown friends on Thanksgiving night? and Have you ever attended a "Friendsgiving?.
# Write up a markdown cell with your findings.
# The data shows that people who attend friendsgivings tend to be younger and make less money than those who don't
friends_data = data.pivot_table(index='Have you ever tried to meet up with hometown friends on Thanksgiving night?', columns='Have you ever attended a "Friendsgiving?"', values='int_age')
print(friends_data)
income_data = data.pivot_table(index='Have you ever tried to meet up with hometown friends on Thanksgiving night?', columns='Have you ever attended a "Friendsgiving?"', values='int_income')
print(income_data)
