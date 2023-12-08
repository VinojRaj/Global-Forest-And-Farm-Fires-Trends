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

# Initialize a dictionary to store total fire counts for each country by year
total_fire_counts_by_year = {}

# Iterate through each country
for country in countries:
    # Construct the file path
    file_path = f'C:\\Users\\Vinoj\\OneDrive\\Desktop\\Ashoka_PEDP\\Assignments\\Assignment 7.2\\Data_2018-2023\\{country}_fires_data_2018_2023.csv'

    # Check if the file exists
    if os.path.exists(file_path):
        # Load data from CSV file
        df = pd.read_csv(file_path)

        # Convert the 'datetime' column to datetime format with the correct format
        df['datetime'] = pd.to_datetime(df['datetime'], format='%d-%m-%Y')

        # Group data by year and sum the fire counts
        yearly_totals = df.groupby(df['datetime'].dt.year)['co2_emission_estimate'].sum()

        # Store the yearly totals in the dictionary
        total_fire_counts_by_year[country] = yearly_totals

# Create a DataFrame from the dictionary
total_fire_counts_by_year_df = pd.DataFrame(total_fire_counts_by_year)

# Set the style for the plot
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6), dpi=600)  # Set the dpi parameter for increased resolution

# Plot the line chart
total_fire_counts_by_year_df.plot(kind='line', marker='o', color=[custom_colors[country] for country in total_fire_counts_by_year_df.columns])

# Set labels and title
plt.xlabel('Year')
plt.ylabel('Total CO2 Emission Estimate')
plt.title('Yearly Trend of Total CO2 Emission Estimate in Different Countries')

# Show legend
plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')

# Display the plot
plt.tight_layout()
plt.show()
