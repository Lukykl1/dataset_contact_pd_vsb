import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from multiprocessing import Pool

# Assuming data is already loaded and preprocessed
data_path = 'feature_vector.csv'  # Change this to your CSV file path
data = pd.read_csv(data_path, delimiter=';')
data = data.drop(columns=['id_measurement', 'phase', 'annotation'])

# Define a function to plot a single feature
def plot_feature(column):
    plt.figure(figsize=(10, 6))
    sns.histplot(data[column], kde=True, color='skyblue')
    plt.title(column)
    # Save plot to file
    plt.savefig(f'{column}_hist.png')
    plt.close()  # Close the plot to free up memory

# Define a function to plot a boxplot for all features
def plot_boxplot():
    plt.figure(figsize=(25, 10))
    sns.boxplot(data=data, palette="coolwarm")
    plt.xticks(rotation=90)
    plt.title('Feature Boxplots')
    plt.savefig('all_features_boxplot.png')
    plt.close()

# Use multiprocessing to generate plots for each feature
if __name__ == '__main__':
    with Pool(processes=4) as pool:  # Adjust number of processes based on your system
        pool.map(plot_feature, data.columns)
    
    # Plotting the boxplot (since it's a single plot, no need to parallelize)
    plot_boxplot()
