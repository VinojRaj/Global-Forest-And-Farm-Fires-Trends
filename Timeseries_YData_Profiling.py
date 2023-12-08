# -*- coding: utf-8 -*-
"""
@author: Vinoj
"""

import pandas as pd

from ydata_profiling import ProfileReport

file_name = (r"C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\Assignments\Assignment 7.2\Data_2018-2023\USA_fires_data_2018_2023.csv")

df = pd.read_csv(file_name, index_col=[0])

# Filtering time-series to profile a single site
# site = df[df["Site Num"] == 3003]

#Enable tsmode to True to automatically identify time-series variables
#Provide the column name that provides the chronological order of your time-series
profile = ProfileReport(df, tsmode=True, sortby="datetime", title="USA Fire_Data EDA")

profile.to_file(r"C:\Users\Vinoj\OneDrive\Desktop\Ashoka_PEDP\Assignments\Assignment 7.2\Data_2018-2023\EDA\USA Fire_Data EDA_timeseries.html")
