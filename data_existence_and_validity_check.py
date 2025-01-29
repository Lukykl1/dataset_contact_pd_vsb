import csv
import os
import gzip
import sys
import numpy as np

def check_file_content(file_content):
    # Convert the byte content to a numpy array of signed bytes (int8)
    data = np.frombuffer(file_content, dtype=np.int8)
    
    # Check if all elements are the same or all are zero
    if np.all(data == data[0]) or np.all(data == 0):
        return False
    return True

def check_measurements_file(csv_file_path, measurements_dir):
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            id_measurement = row['id_measurement']
            phase = row['phase']
            filename = f"{id_measurement}_{phase}.bin.gz"
            file_path = os.path.join(measurements_dir, filename)
            
            if not os.path.exists(file_path):
                print(f"File {filename} does not exist.")
                continue
            
            with gzip.open(file_path, 'rb') as f:
                content = f.read()
                if len(content) != 800000:
                    print(f"File {filename} does not have the correct size (800000 bytes).")
                else:
                    print(f"File {filename} meets the criteria.")
                # Check if the file content is valid according to the criteria
                if not check_file_content(content):
                    print(f"File {filename} contains invalid byte data (all bytes are the same or zero).")
                else:
                    print(f"File {filename} meets all criteria.")
                    
print("Checking for missing and invalid measurements...")
# Helps to run the script from the command line
print("Usage: python data_existence_and_validity_check.py <csv_file_path> <measurements_dir>")
# Update the paths according to your file structure
csv_file_path = sys.argv[1]
measurements_dir = sys.argv[2]

check_measurements_file(csv_file_path, measurements_dir)
