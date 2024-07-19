import re
import os

# Define the source and destination folders
source_folder = 'l1'
destination_folder = 'l1_redundancy'

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