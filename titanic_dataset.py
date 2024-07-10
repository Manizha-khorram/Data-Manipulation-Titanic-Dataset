import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Titanic dataset from a CSV file
titanic_csv_dataset = pd.read_csv('titanicdata.csv')
print('First few rows of Titanic CSV dataset:')
print(titanic_csv_dataset.head())


# Check for missing values
null_data = titanic_csv_dataset.isnull().sum()
print('null values: \n',null_data)


#  Fill missing values (example age)
titanic_csv_dataset['age'] = titanic_csv_dataset['age'].fillna(titanic_csv_dataset['age'].mean())

summery_stat = titanic_csv_dataset.describe()
print(summery_stat)

# # Data types
# data_types = titanic_csv_dataset.dtypes
# print('Data types:\n',data_types)

# Set the style of the visualization
sns.set(style="whitegrid")

# Create a figure and axis
plt.figure(figsize=(10, 6))

# Plot the age distribution
sns.histplot(titanic_csv_dataset['age'], bins=30, kde=True, color='blue')

# Set the title and labels
plt.title('Age Distribution of Titanic Passengers', fontsize=16)
plt.xlabel('Age', fontsize=14)
plt.ylabel('Frequency', fontsize=14)

# Show the plot
plt.show()





