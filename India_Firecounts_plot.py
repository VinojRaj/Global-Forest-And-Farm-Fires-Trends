# -*- coding: utf-8 -*-
"""
@author: Vinoj
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from Excel file
excel_file = r"C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\Assignments\Assignment 7.2\Data_2018-2023\India_fires_data_2018_2023.csv"
df = pd.read_csv(excel_file)

# Convert the 'datetime' column to datetime format with the correct format
df['datetime'] = pd.to_datetime(df['datetime'], format='%d-%m-%Y')

# Set the style for the plot
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6), dpi=300)

# Plot the time series data
sns.lineplot(x='datetime', y='fires', data=df, marker='o', color='orange', label='Fire Counts')

# Set labels and title
plt.xlabel('Time')
plt.ylabel('Fire Counts')
plt.title('Time Series of Fire Counts in India')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show legend
plt.legend()

# Display the plot
plt.tight_layout()
plt.show()