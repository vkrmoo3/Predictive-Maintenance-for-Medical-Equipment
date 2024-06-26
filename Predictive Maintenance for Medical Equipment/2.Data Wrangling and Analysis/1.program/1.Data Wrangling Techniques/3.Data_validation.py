import pandas as pd

def data_validation(dataset_path):
    # Read the dataset
    df = pd.read_csv(dataset_path)

    # Check for unique values in each column
    for column in df.columns:
        unique_values = df[column].unique()
        print(f"Unique values in column '{column}':")
        print(unique_values)
        print()

if __name__ == "__main__":
    # Path to the dataset
    dataset_path = "/content/sample_data/pm-data set.csv"  # Update with your dataset filename

    # Perform data validation
    data_validation(dataset_path)
