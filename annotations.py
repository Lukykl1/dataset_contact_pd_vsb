import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data into a DataFrame
data = pd.read_csv('feature_vector.csv', delimiter=';')  # Adjust the file name as necessary

# Function to add value labels above bars
def add_value_labels(ax, spacing=5):
    """Add labels to the end of each bar in a bar chart."""
    for rect in ax.patches:
        y_value = rect.get_height()
        x_value = rect.get_x() + rect.get_width() / 2

        # Number of points between bar and label
        space = spacing
        # Vertical alignment for positive values
        va = 'bottom'

        # Use Y value as label and format number with one decimal
        label = "{:.1f}".format(y_value)

        # Create annotation
        ax.annotate(
            label,                      # Use `label` as label
            (x_value, y_value),         # Place label at end of the bar
            xytext=(0, space),          # Vertically shift label by `space`
            textcoords="offset points", # Interpret `xytext` as offset in points
            ha='center',                # Horizontally center label
            va=va)                      # Vertically align label differently for positive and negative values.

# Count the number of occurrences of each annotation including 0
annotation_counts_incl_zero = data['annotation'].value_counts().sort_index()

# Count the number of occurrences of each annotation excluding 0
annotation_counts_excl_zero = data[data['annotation'] != 0]['annotation'].value_counts().sort_index()

# Visualize including 0
plt.figure(figsize=(10, 6))
ax = annotation_counts_incl_zero.plot(kind='bar', color='skyblue')
plt.title('Annotation Counts Including 0')
plt.xlabel('Annotation')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--')
add_value_labels(ax)
plt.tight_layout()
#save the plot
plt.savefig('annotation_counts_incl_zero.png')

# Visualize excluding 0
plt.figure(figsize=(10, 6))
ax = annotation_counts_excl_zero.plot(kind='bar', color='coral')
plt.title('Annotation Counts Excluding 0')
plt.xlabel('Annotation')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--')
add_value_labels(ax)
plt.tight_layout()
#save the plot
plt.savefig('annotation_counts_excl_zero.png')
