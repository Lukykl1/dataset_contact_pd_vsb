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


# Check for Phase Completeness for each 'id_measurement'
# Verify that each 'id_measurement' has exactly 3 phases
phase_counts = data.groupby('id_measurement')['phase'].nunique()
if not all(phase_counts == 3):
    print("Warning: Some 'id_measurement' entries do not have exactly 3 phases.")
else:
    print("All measurements have exactly 3 phases.")


if not all(phase_counts == 3):
    incomplete_measurements = phase_counts[phase_counts != 3].index.tolist()
    print(f"'id_measurement' values without 3 phases: {incomplete_measurements}")

