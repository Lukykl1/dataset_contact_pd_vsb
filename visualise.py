

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data
file_path = 'feature_vector.csv'  # Update this to your file's path
data = pd.read_csv(file_path, delimiter=';')

# Group by 'id_measurement' to find the total number of phases present
phase_presence = data.groupby('id_measurement')['phase'].nunique()

# Calculate missing phases for each 'id_measurement'
# Since each measurement should have 3 phases, subtract the count from 3
missing_phases = 3 - phase_presence

# Define bins for 'id_measurement'
min_id, max_id = data['id_measurement'].min(), data['id_measurement'].max()
bin_size = 10000  # Adjust this based on your dataset and preference
bins = np.linspace(min_id, max_id, num=int((max_id - min_id) / bin_size) + 1)

# Bin 'id_measurement' by assigning each measurement to a bin
data['bin'] = pd.cut(data['id_measurement'], bins=bins, labels=False)

# Calculate total missing phases per bin
# First, map each 'id_measurement' in the original data to its missing phases
data['missing_phases'] = data['id_measurement'].map(missing_phases)
# Then, sum up missing phases within each bin
binned_missing_phases = data.groupby('bin')['missing_phases'].sum()

# Plotting
fig, ax = plt.subplots(figsize=(12, 6))

# Create a bar plot for the total missing phases per bin
ax.bar(binned_missing_phases.index.astype(str), binned_missing_phases.values, color='blue')

ax.set_xlabel('Bin (Measurement ID Range)')
ax.set_ylabel('Total Missing Phases')
ax.set_title('Total Missing Phases by Measurement ID Bins')

# Set tick labels for bins
# Generate labels based on bin edges
tick_labels = [f"{int(bins[i])}-{int(bins[i+1])}" for i in range(len(bins)-1)]
# Reduce the number of tick labels to avoid clutter
tick_positions = np.arange(len(tick_labels))
ax.set_xticks(tick_positions[::int(len(tick_positions)/10)])
ax.set_xticklabels(tick_labels[::int(len(tick_labels)/10)], rotation=45, ha="right")


plt.tight_layout()
#save the plot
plt.savefig('missing_phases_by_measurement_id_bins.png')