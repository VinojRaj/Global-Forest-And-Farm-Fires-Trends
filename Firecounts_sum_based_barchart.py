# -*- coding: utf-8 -*-
"""
@author: Vinoj
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define the list of countries including India
countries = ['Brazil', 'Canada', 'China', 'France', 'Germany', 'India', 'Italy', 'Mexico', 'Russia', 'USA']

# Define custom colors for each country
custom_colors = {
    'Brazil': 'green',
    'Canada': 'red',
    'China': 'gold',
    'France': 'blue',
    'Germany': 'black',
    'India': '#FF9933',  # Saffron
    'Italy': '#7FFF7F',  # Light green
    'Mexico': 'teal',
    'Russia': 'silver',
    'USA': '#800020'  # HEX color code for burgundy
}

# Initialize a dictionary to store total fire counts for each country
total_fire_counts = {}

# Iterate through each country
for country in countries:
    # Construct the file path
    file_path = f'C:\\Users\\Vinoj\\OneDrive\\Desktop\\Ashoka_PEDP\\Assignments\\Assignment 7.2\\Data_2018-2023\\{country}_fires_data_2018_2023.csv'

    # Check if the file exists
    if os.path.exists(file_path):
        # Load data from CSV file
        df = pd.read_csv(file_path)

        # Sum the total fire counts for each country
        total_fire_counts[country] = df['fires'].sum()

# Create a DataFrame from the total fire counts dictionary
total_fire_counts_df = pd.DataFrame(list(total_fire_counts.items()), columns=['Country', 'Total Fire Counts'])

# Sort the DataFrame in decreasing order of total fire counts
total_fire_counts_df = total_fire_counts_df.sort_values(by='Total Fire Counts', ascending=False)

# Set the style for the plot
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6), dpi=300)  # Set the dpi parameter for increased resolution

# Plot the bar chart
sns.barplot(x='Country', y='Total Fire Counts', data=total_fire_counts_df, palette=[custom_colors[country] for country in total_fire_counts_df['Country']])

# Set labels and title
plt.xlabel('Country')
plt.ylabel('Total Fire Counts')
plt.title('Total Fire Counts in Different Countries')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Display the plot
plt.tight_layout()
plt.show()
