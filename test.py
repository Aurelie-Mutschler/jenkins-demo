import pandas as pd

# Step 1: Extract
def extract_data(file_path):
    """Extracts data from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        print("Data extraction successful.")
        return data
    except Exception as e:
        print(f"Error in data extraction: {e}")
        return None


# Main test function
def compare(df1, df2):
    pd.testing.assert_frame_equal(df1, df2)

if __name__ == "__main__":
    file1= 'output_data.csv'
    file2 = 'output_data_example.csv'
    compare(file1, file2)