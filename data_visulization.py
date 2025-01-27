# -*- coding: utf-8 -*-
"""Data_visulization.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hpyUnYNY6tS0kYpvoWgqYs6ZR4CO5ZPU
"""

#Matplotlib Assignments

#1. Create a scatter plot using Matplotlib to visualize the relationship between two arrays, x and y for the given data.
#x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#y = [2, 4, 5, 7, 6, 8, 9, 10, 12, 13]
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y= [2, 4, 5, 7, 6, 8, 9, 10, 12, 13]
plt.scatter(x,y)
plt.xlabel('x')
plt.ylabel('y')

#Generate a line plot to visualize the trend of values for the given data.
#data = np.array([3, 7, 9, 15, 22, 29, 35])

import numpy as np
# Data for the line plot
data = np.array([3, 7, 9, 15, 22, 29, 35])
x = np.arange(1, len(data) + 1)  # Generate x values based on the length of the data

# Generate line plot
plt.figure(figsize=(8, 6))
plt.plot(x, data, color='purple', marker='o', linestyle='-', label='Trend Line')
plt.title('Line Plot of Data', fontsize=14)
plt.xlabel('Index', fontsize=12)
plt.ylabel('Value', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.show()

# Display a bar chart to represent the frequency of each item in the given array categories.categories = ['A', 'B', 'C', 'D', 'E'] values = [25, 40, 30, 35, 20]
categories = ['A', 'B', 'C', 'D', 'E']
values = [25, 40, 30, 35, 20]
plt.bar(categories,values,color='skyblue',edgecolor='black')
plt.xlabel('categories')
plt.ylabel('values')
plt.title('Bar Plot')
plt.show()

#Create a histogram to visualize the distribution of values in the array data. data = np.random.normal(0, 1, 1000)
data = np.random.normal(0, 1, 1000)
plt.hist(data,bins=30,color='green',edgecolor='black')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram of Data')
plt.show()

# Show a pie chart to represent the percentage distribution of different sections in the array `sections`.
sections = ['Section A', 'Section B', 'Section C', 'Section D']
sizes = [25, 30, 15, 30]
plt.pie(sizes,labels=sections,colors=['red','green','skyblue','pink'])
plt.title('Pie Chart')
plt.show()

#Seaborn assignments

#Create a scatter plot to visualize the relationship between two variables, by generating a synthetic dataset.
import seaborn as sns
import pandas as pd
import numpy as np

data = pd.DataFrame({
    'x': np.random.rand(100),
    'y': np.random.rand(100)
})
sns.scatterplot(x='x', y='y', data=data)
plt.title('Scatter Plot of Synthetic Data')
plt.show()

# Generate a dataset of random numbers. Visualize the distribution of a numerical variable.
data = np.random.normal(loc=0, scale=1, size=1000)
sns.histplot(data, kde=True)
plt.title('Distribution of Random Numbers')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

#Create a dataset representing categories and their corresponding values. Compare different categories based on numerical values.
data = {'Category': ['A', 'B', 'C', 'D', 'E'],
        'Value': [25, 40, 30, 35, 20]}

df = pd.DataFrame(data)
sns.barplot(x='Category', y='Value', data=df)
plt.title('Comparison of Categories')
plt.xlabel('Category')
plt.ylabel('Value')
plt.show()

#Generate a dataset with categories and numerical values. Visualize the distribution of a numerical variable across different categories.
data = {'Category': ['A', 'B', 'C', 'D', 'E'],
        'Value': [25, 40, 30, 35, 20]}

df = pd.DataFrame(data)
sns.boxplot(x='Category', y='Value', data=df)
plt.title('Distribution of Numerical Variable Across Categories')
plt.xlabel('Category')
plt.ylabel('Value')
plt.show()

#Generate a synthetic dataset with correlated features. Visualize the correlation matrix of a dataset using a heatmap
num_points = 100


x1 = np.random.rand(num_points)
x2 = 0.5 * x1 + 0.5 * np.random.rand(num_points)
data = pd.DataFrame({'x1': x1, 'x2': x2})

correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Using the given dataset, to generate a 3D scatter plot to visualize the distribution of data points in a threedimensional space.
from mpl_toolkits.mplot3d import Axes3D
np.random.seed(30)
data = {
    'X': np.random.uniform(-10, 10, 300),
    'Y': np.random.uniform(-10, 10, 300),
    'Z': np.random.uniform(-10, 10, 300)
}
df = pd.DataFrame(data)

# Create a figure and an axes object for the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter plot
ax.scatter(df['X'], df['Y'], df['Z'], c='blue', marker='o')

# Set labels for the axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set the title of the plot
ax.set_title('3D Scatter Plot')

# Display the plot
plt.show()

# Using the Student Grades, create a violin plot to display the distribution of scores across different grade categories.
np.random.seed(15)
data = {
    'Grade': np.random.choice(['A', 'B', 'C', 'D', 'F'], 200),
    'Score': np.random.randint(50, 100, 200)
}
df = pd.DataFrame(data)
sns.violinplot(x='Grade',y='Score',data=df)
plt.title('Distribution of Scores across different grade categories')
plt.xlabel('Grade')
plt.ylabel('Score')
plt.show()

#Using the sales data, generate a heatmap to visualize the variation in sales across different months and days.

np.random.seed(20)
data = {
    'Month': np.random.choice(['Jan', 'Feb', 'Mar', 'Apr', 'May'], 100),
    'Day': np.random.choice(range(1, 31), 100),
    'Sales': np.random.randint(1000, 5000, 100)
}
df = pd.DataFrame(data)
sales_matrix = df.pivot_table(values='Sales', index='Month', columns='Day')
sns.heatmap(sales_matrix, cmap='coolwarm')
plt.title('Variation in Sales across different months and days')
plt.xlabel('Day')
plt.ylabel('Month')
plt.show()

#Using the sales data, generate a heatmap to visualize the variation in sales across different months and days.
np.random.seed(20)
data = {
    'Month': np.random.choice(['Jan', 'Feb', 'Mar', 'Apr', 'May'], 100),
    'Day': np.random.choice(range(1, 31), 100),
    'Sales': np.random.randint(1000, 5000, 100)
}
df = pd.DataFrame(data)
sales_matrix=df.pivot_table(values='Sales',index='Month',columns='Day')
sns.heatmap(sales_matrix,cmap='coolwarm')
plt.title('Variation in Sales across different months and days')
plt.xlabel('Day')
plt.ylabel('Month')
plt.show()

#. Using the given x and y data, generate a 3D surface plot to visualize the function z=sin(x^2+y^2)^1/2
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))
data = {
    'X': x.flatten(),
    'Y': y.flatten(),
    'Z': z.flatten()
}
df = pd.DataFrame(data)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(df['X'], df['Y'], df['Z'], cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Surface Plot')
plt.show()

# Using the given dataset, create a bubble chart to represent each country's population (y-axis), GDP (xaxis), and bubble size proportional to the population.
np.random.seed(25)
data = {
    'Country': ['USA', 'Canada', 'UK',
'Germany', 'France'],
    'Population':
np.random.randint(100, 1000, 5),
    'GDP': np.random.randint(500, 2000,
5)
}
df = pd.DataFrame(data)
plt.figure(figsize=(10, 6))
# Create the bubble chart
plt.scatter(df['GDP'], df['Population'], s=df['Population'], alpha=0.5)
# Set plot title and labels
plt.title('Population vs GDP')
plt.xlabel('GDP')
plt.ylabel('Population')

# Add country labels
for i, row in df.iterrows():
    plt.annotate(row['Country'], (row['GDP'], row['Population']))

# Display the plot
plt.show()

#.Create a Bokeh plot displaying a sine wave. Set x-values from 0 to 10 and y-values as the sine of x
from bokeh.plotting import figure, show
import numpy as np

# Generate x and y values
x = np.linspace(0, 10, 500)
y = np.sin(x)

# Create a Bokeh figure
p = figure(title="Sine Wave", x_axis_label="x", y_axis_label="sin(x)", width=800, height=400)

# Add a line renderer for the sine wave
p.line(x, y, legend_label="sin(x)", line_width=2, color="blue")

# Show the plot
show(p)

#Create a Bokeh scatter plot using randomly generated x and y values. Use different sizes and colors for the
#markers based on the 'sizes' and 'colors' columns.
from bokeh.models import ColumnDataSource

# Generate random data
np.random.seed(42)  # For reproducibility
data = {
    'x': np.random.rand(100),
    'y': np.random.rand(100),
    'sizes': np.random.randint(5, 20, 100),
    'colors': np.random.choice(['red', 'green', 'blue'], 100)
}
df = pd.DataFrame(data)

# Create a ColumnDataSource
source = ColumnDataSource(df)

# Create a Bokeh figure
p = figure(title="Scatter Plot with Varying Sizes and Colors")

# Plot the scatter plot
p.scatter(x='x', y='y', size='sizes', color='colors', source=source)

# Display the plot
show(p)

# Generate a Bokeh bar chart representing the counts of different fruits using the following dataset.
fruits = ['Apples', 'Oranges', 'Bananas', 'Pears']
counts = [20, 25, 30, 35]
p = figure(x_range=fruits,title="Fruit Counts")

# Create the bar chart
p.vbar(x=fruits, top=counts, width=0.9)

# Customize the plot
p.xgrid.grid_line_color = None
p.y_range.start = 0

# Display the plot
show(p)

# Create a Bokeh histogram to visualize the distribution of the given data.
data_hist = np.random.randn(1000)
hist, edges = np.histogram(data_hist, bins=30)
p = figure(title="Histogram", x_axis_label="Value", y_axis_label="Frequency")

# Create the histogram
p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],
       fill_color="navy", line_color="white", alpha=0.5)

# Display the plot
show(p)

#Create a Bokeh heatmap using the provided dataset.
from bokeh.models import LinearColorMapper, ColorBar
data_heatmap = np.random.rand(10, 10)
x = np.linspace(0, 1, 10)
y = np.linspace(0, 1, 10)
xx, yy = np.meshgrid(x, y)
color_mapper = LinearColorMapper(palette="Viridis256", low=data_heatmap.min(), high=data_heatmap.max())

# Create a figure
p = figure(title="Heatmap", x_axis_label="x", y_axis_label="y",
           x_range=(0, 1), y_range=(0, 1))

# Create the heatmap
p.image(image=[data_heatmap], x=0, y=0, dw=1, dh=1, color_mapper=color_mapper)