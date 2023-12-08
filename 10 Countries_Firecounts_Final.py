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

# Set the style for the plot
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6), dpi=300)  # Set the dpi parameter for increased resolution

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

        # Plot the time series data for each country with a different color, line style, and without markers
        sns.lineplot(x='datetime', y='co2_emission_estimate', data=df, label=country, color=custom_colors[country], marker=None, linestyle='-')

# Set labels and title
plt.xlabel('Time')
plt.ylabel('CO2 emission estimate')
plt.title('Time Series of CO2 Emission Estimate in Different Countries')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show legend
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# Display the plot
plt.tight_layout()
plt.show()
