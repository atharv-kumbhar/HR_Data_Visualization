import pandas as pd
from matplotlib.pyplot import legend
from werkzeug.debug.repr import missing
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)



file_path = "D:/BI19/HR_Data_Visualization/data/HumanResources.csv"
data = pd.read_csv(file_path,delimiter=';')



print("Data Headers\n",data.head())
print(data.info())
print("columns\n",data.columns)
missing_values = data.isnull().sum()
print("null value data info\n",missing_values)

data['Termdate'] = data['Termdate'].fillna('N/A')
data['Hiredate'] = pd.to_datetime(data['Hiredate'], format='%d/%m/%Y', errors='coerce')
data['Birthdate'] = pd.to_datetime(data['Birthdate'], format='%d/%m/%Y', errors='coerce')
data['Termdate'] = pd.to_datetime(data['Termdate'], format='%d/%m/%Y', errors='coerce')
data['Salary'] = pd.to_numeric(data['Salary'], errors='coerce')

print("summary statistics for numerical columns\n",data.describe())
print("duplicate data info\n",data.duplicated().sum())

#visualization1
# Bar plot for department distribution
plt.figure(figsize=(12,12))
sns.countplot(data=data, x='Department', hue='Department', palette='Set1', legend=True)
plt.title('Number of Employees per Department')
plt.xticks(rotation=90)# Rotate labels for better readability
plt.xlabel('Department')
plt.ylabel('Employee Count')
plt.savefig(r'D:\BI19\HR_Data_Visualization\visualization\ department_distribution.png')
plt.show()
print("visualization 1 printed")

#visualization2
#Histogram for salary distribution
plt.figure(figsize=(10, 6))
sns.histplot(data['Salary'], bins=5, kde=True, color="Green")
plt.title('Salary Distribution')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.savefig(r'D:\BI19\HR_Data_Visualization\visualization\ Histogram for salary distribution.png')
plt.show()
print("visualization 2 printed")

#visualization3
# Scatter plot for Salary vs. Performance Rating
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='Salary', y='Performance Rating', hue='Department', palette='Set1')
plt.title('Salary vs. Performance Rating')
plt.xlabel('Salary')
plt.ylabel('Performance Rating')
plt.savefig(r'D:\BI19\HR_Data_Visualization\visualization\ Scatter plot for Salary vs. Performance Rating.png')
plt.show()
print("visualization 3 printed")

#visualization4
# Pie chart for gender distribution
sns.set_theme(style="whitegrid")
gender_counts = data['Gender'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', colors=['#ff9999','#66b3ff','#000000'])
plt.title('Gender Distribution')
plt.savefig(r'D:\BI19\HR_Data_Visualization\visualization\ Pie chart for gender distribution.png')
plt.show()
print("visualization 4 printed")

#visualization5
#Box Plot Salary Distribution by Department
plt.figure(figsize=(10, 6))
sns.boxplot(data=data, x='Department', y='Salary', palette='Set2')
plt.title('Salary Distribution by Department')
plt.xlabel('Department')
plt.ylabel('Salary')
plt.xticks(rotation=45)
plt.savefig(r'D:\BI19\HR_Data_Visualization\visualization\ Box Plot Salary Distribution by Department.png')
plt.show()
print("visualization 5 printed")

# visualization6
# Bar Plot Average Salary by Gender
plt.figure(figsize=(8, 6))
sns.barplot(data=data, x='Gender', y='Salary', palette='Set1')
plt.title('Average Salary by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Salary')
plt.savefig(r'D:\BI19\HR_Data_Visualization\visualization\ Bar Plot Average Salary by Gender.png')
plt.show()
print("visualization 6 printed")

# visualization7
# Violin Plot Salary Distribution by Gender
plt.figure(figsize=(8, 6))
sns.violinplot(data=data, x='Gender', y='Salary', palette='Set1')
plt.title('Salary Distribution by Gender')
plt.xlabel('Gender')
plt.ylabel('Salary')
plt.savefig(r'D:\BI19\HR_Data_Visualization\visualization\ Violin Plot Salary Distribution by Gender.png')
plt.show()
print("visualization 7 printed")

# visualization8
# Facet Grid Comparing Multiple Distributions
g = sns.FacetGrid(data, col='Department', height=4, col_wrap=4)
g.map(sns.histplot, 'Salary', kde=True, color='blue')
plt.savefig(r'D:\BI19\HR_Data_Visualization\visualization\ Facet Grid Comparing Multiple Distributions.png')
plt.show()
print("visualization 8 printed")

# visualization9
# Strip Plot Salary by Department with Jitter
plt.figure(figsize=(10, 6))
sns.stripplot(data=data, x='Department', y='Salary', jitter=True, palette='Set2', dodge=True)
plt.title('Salary Distribution by Department (Strip Plot)')
plt.xlabel('Department')
plt.ylabel('Salary')
plt.xticks(rotation=45)
plt.savefig(r'D:\BI19\HR_Data_Visualization\visualization\ Strip Plot Salary by Department with Jitter.png')
plt.show()
print("visualization 9 printed")
