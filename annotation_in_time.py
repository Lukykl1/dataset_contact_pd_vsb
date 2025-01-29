import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = 'feature_vector.csv'
df = pd.read_csv(file_path, delimiter=';')

# Filter out annotations with value 0
df_filtered = df[df['annotation'] != 0]

# Assuming 'id_measurement' is sorted and represents time steps linearly,
# we'll create bins. Bin for each 10000 'id_measurement' values.
number_of_bins = int(df_filtered['id_measurement'].max() / 50000)

# Create a new column for the binned data
df_filtered['binned'] = pd.cut(df_filtered['id_measurement'], bins=number_of_bins, labels=False)

# Aggregate data in bins, for simplicity we count occurrences, but you can adjust aggregation based on your needs
binned_data = df_filtered.groupby('binned')['annotation'].value_counts().unstack(fill_value=0)
# Retitle the x-axis
binned_data.index = [f'{i*50000}-{(i+1)*50000}' for i in binned_data.index]

# Plot
plt.figure(figsize=(35, 20))
binned_data.plot(kind='bar', stacked=False, figsize=(35, 20))
plt.title('Annotations Over ID Measurement (Binned)')
plt.xlabel('Binned ID Measurement')
plt.ylabel('Count of Annotations')
plt.legend(title='Annotation')
#save the plot
plt.savefig('annotations_over_time_binned.png')