import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from concurrent.futures import ThreadPoolExecutor

# Function to load and preprocess data
def load_and_preprocess_data(path):
    data = pd.read_csv(path, delimiter=';')
    data = data.drop(columns=['id_measurement', 'phase', 'annotation'])
    return data

# Function to calculate descriptive statistics for one column
def calculate_statistics(column, data):
    return data[column].describe()

# Load the data
data_path = 'feature_vector.csv'  # Change this to your CSV file path
data = load_and_preprocess_data(data_path)

# Use ThreadPoolExecutor to parallelize the calculation of descriptive statistics
with ThreadPoolExecutor(max_workers=8) as executor:  # Adjust max_workers as needed
    futures = {executor.submit(calculate_statistics, column, data): column for column in data.columns}
    stats = {future.result().name: future.result() for future in futures}

# Print or process descriptive statistics here
# For demonstration, just print one example
print(stats['a0_StrikeCount'])

# Visualization (This part remains sequential)
plt.figure(figsize=(25, 20))
for i, column in enumerate(data.columns, 1):
    plt.subplot(8, 4, i)
    sns.histplot(data[column], kde=True, color='skyblue')
    plt.tight_layout()
    plt.title(column)
#save the plot
plt.savefig('feature_histograms.png')

plt.figure(figsize=(30, 20))
sns.boxplot(data=data, palette="coolwarm")
plt.xticks(rotation=90)
plt.title('Feature Boxplots')
#save the plot
plt.savefig('feature_boxplots.png')