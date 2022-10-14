"""File list by size

Python script to find large files (150 MB used as the cap) in specific folders and save the list to a CSV file.

Requirement:
    os
    pandas
    time
    datetime

Author:
    Adnan Yoztyurk
"""

import os
import pandas as pd
import time
import datetime as dt

# Folder to find the list of files
search_dir = # Please enter a valid folder path

# os.walk function to find the subfolders of given search_dir
sub_folders = [x[0] for x in os.walk(search_dir)]

file_name = []
full_path = []
time_list = []
size_list = []
for y in sub_folders:
    for i in (os.listdir(y)):
        if os.path.isfile(os.path.join(y, i)):
            file_name.extend([i])
            full_path.extend([os.path.join(y, i)])
            time_list.extend([dt.datetime.fromtimestamp(os.path.getmtime(os.path.join(y, i))).strftime("%Y")])
            size_list.extend([int(os.path.getsize(os.path.join(y, i)) / (1024 ** 2))])

# Convert to dataframe
file_dataframe = pd.DataFrame(
    {'File Name': file_name, 'Full Path': full_path, 'Year (Modified)': time_list, 'Size (MB)': size_list})

file_dataframe_sorted = file_dataframe.sort_values('Size (MB)', ascending=False)
file_dataframe_sorted_filtered = file_dataframe_sorted.loc[file_dataframe_sorted['Size (MB)'] > 150]

# Save the dataframe as a CSV file
file_dataframe_sorted_filtered.to_csv('''Please provide a valid path to output folder''' + ".csv",
                                      index=False, header=True)
