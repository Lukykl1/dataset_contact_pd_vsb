import pandas as pd

# Load the CSV file
file_path = 'feature_vector.csv'  # Update this to your file's path
data = pd.read_csv(file_path, delimiter=';')

# Basic Data Validation

# Check for missing values
if data.isnull().values.any():
    print("Warning: There are missing values in the dataset.")
else:
    print("No missing values found.")

# Ensure numeric columns contain only numbers
# Assuming all columns except 'id_measurement' and 'phase' should be numeric
numeric_columns = [col for col in data.columns if col not in ['id_measurement', 'phase']]
for col in numeric_columns:
    if not pd.to_numeric(data[col], errors='coerce').notnull().all():
        print(f"Warning: Non-numeric values found in {col}.")

# Validate ranges or specific conditions for certain columns
# Example: Check if 'phase' column contains only 1, 2, or 3
if not data['phase'].isin([1, 2, 3]).all():
    print("Warning: Invalid values found in 'phase' column.")

# Check for duplicate rows based on 'id_measurement' and 'phase'
if data.duplicated(subset=['id_measurement', 'phase']).any():
    print("Warning: Duplicate rows found based on 'id_measurement' and 'phase'.")
# Sort the data by 'id_measurement' and 'phase' to ensure proper ordering
data.sort_values(by=['id_measurement', 'phase'], inplace=True)

# Check for Successiveness of 'id_measurement'
# Assuming 'id_measurement' should be unique and consecutive
unique_measurements = data['id_measurement'].unique()
gaps = len(unique_measurements) != (unique_measurements[-1] - unique_measurements[0] + 1)
if gaps:
    print("Warning: 'id_measurement' values are not successive. There may be gaps.")
else:
    print("All 'id_measurement' values are successive.")

# Check for Phase Completeness for each 'id_measurement'
# Verify that each 'id_measurement' has exactly 3 phases
phase_counts = data.groupby('id_measurement')['phase'].nunique()
if not all(phase_counts == 3):
    print("Warning: Some 'id_measurement' entries do not have exactly 3 phases.")
else:
    print("All measurements have exactly 3 phases.")

# Optional: Identify specific 'id_measurement' values with issues
# This helps in debugging or correcting the data
if gaps or not all(phase_counts == 3):
    if gaps:
        expected_set = set(range(unique_measurements[0], unique_measurements[-1] + 1))
        actual_set = set(unique_measurements)
        missing_measurements = expected_set - actual_set
        print(f"Missing 'id_measurement' values: {len(sorted(list(missing_measurements)))}")

    if not all(phase_counts == 3):
        incomplete_measurements = phase_counts[phase_counts != 3].index.tolist()
        print(f"'id_measurement' values without 3 phases: {len(incomplete_measurements)}")

print("Validation complete.")