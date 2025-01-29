# Project: Data Annotation and Validation Toolkit

## Overview
This project contains a set of Python scripts designed for processing, validating, and visualizing annotated data. The scripts check data existence, validity, and correctness while providing visual representations of the feature vectors.

## File Descriptions

### 1. `annotations.py`
Handles annotation-related functionalities, including processing and managing labeled data.

### 2. `annotation_in_time.py`
Performs time-based annotation analysis, ensuring proper chronological alignment of annotated events.

### 3. `data_existence_and_validity_check.py`
Checks if required data files exist and validates their content for consistency and correctness.

### 4. `feature_vector.csv`
A CSV file containing computed feature vectors used in analysis and validation.

### 5. `invalid_ids.py`
Identifies and flags invalid IDs found within the dataset, helping maintain data integrity.

### 6. `validate.py`
Runs validation checks on the data and annotations, ensuring compliance with predefined rules.

### 7. `visualise.py`
Provides general data visualization functionalities for analyzing trends and distributions.

### 8. `visualise_features.py`
Generates visualizations of extracted feature vectors to help understand data patterns.

### 9. `visualise_features_parallel.py`
Creates parallel coordinate plots for comparing multiple feature vectors simultaneously.

## Installation & Usage
### Prerequisites
- Python 3.x
- Required libraries: `pandas`, `matplotlib`, `seaborn`, `numpy`

### Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/your-repo.git
   cd your-repo
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Running Scripts
Each script can be run individually based on the required operation. For example:
```sh
python validate.py
```

## Contribution
Feel free to submit issues or pull requests to improve functionality or add new features.



