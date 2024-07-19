"""
import requests
import csv

# Function to make GET request and save response to a markdown file
def get_and_save(url):
    try:
        response = requests.get(f'https://r.jina.ai/{url}', headers=headers)
        if response.status_code == 200:
            filename = f'./l2/{url.replace("/", "_")}.md'  # Create a filename based on URL
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(response.text)
                print(f'Successfully saved response for {url}')
        else:
            print(f'Failed to fetch {url}: Status code {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error fetching {url}: {e}')

# CSV file path (change this to your actual CSV file)
csv_file = "./l2.csv"
with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header if exists
    for row in reader:
        if len(row) >= 2:
            url = row[1]  # Assuming URL is in the second column (index 1)
            get_and_save(url)
        else:
            print(f'Skipping row {reader.line_num} as it does not contain 2 columns')

print('All URLs processed.')
"""

"""
import os

# Path to the directory containing files
directory = '/Users/subhashinichirunomula/MSS/PythonProjects/B.TechProjects/Llama3Hackathon/l2_redundancy'

# Function to rename files in a directory
def rename_files(directory):
    try:
        # Iterate over all files in the directory
        for filename in os.listdir(directory):
            if filename.endswith('md'):
                # Construct new filename by appending '.md' to the existing filename
                new_filename = filename[:-3] + '.md'
                
                # Rename file
                os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
                print(f'Renamed {filename} to {new_filename}')
    except OSError as e:
        print(f'Error: {e}')

# Call the function to rename files in the directory
rename_files(directory)
"""

import re
import os

# Define the source and destination folders
source_folder = '/Users/subhashinichirunomula/MSS/PythonProjects/B.TechProjects/Llama3Hackathon/l2'
destination_folder = '/Users/subhashinichirunomula/MSS/PythonProjects/B.TechProjects/Llama3Hackathon/l2'

# Ensure the destination folder exists
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Iterate over each file in the source folder
for source_file_name in os.listdir(source_folder):
    # Construct the full path for the source and destination files
    source_file_path = os.path.join(source_folder, source_file_name)
    destination_file_path = os.path.join(destination_folder, source_file_name)

    # Check if it's a file before processing
    if os.path.isfile(source_file_path):
        # Read the content from the source file
        with open(source_file_path, 'r') as file:
            content = file.read()

        # Remove redundant data between and including lines with consecutive "========"
        cleaned_content = re.sub(r'={2,}.*?={2,}', '', content, flags=re.DOTALL)

        # Save the cleaned content to the destination file
        with open(destination_file_path, 'w') as file:
            file.write(cleaned_content)