#Task2-Data Analysis
import pandas as pd
import numpy as np
from scipy import stats

def perform_descriptive_analysis(file_path):
    print("Loading dataset...")
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: Could not find the file at {file_path}. Please check your path.")
        return
    
    # Strip any whitespace from column names to prevent indexing errors
    df.columns = df.columns.str.strip()
    
    # Capitalizing to match your target columns array
    target_columns = ['Sales', 'Unit']
    
    print("\n" + "="*50)
    print("        DESCRIPTIVE STATISTICAL ANALYSIS")
    print("="*50)
    
    for col in target_columns:
        if col in df.columns:
            # Ensure the column data is numeric for proper calculations
            numeric_col = pd.to_numeric(df[col], errors='coerce')
            
            # Calculate metrics using Pandas
            mean_val = numeric_col.mean()
            median_val = numeric_col.median()
            std_val = numeric_col.std()
            
            # Calculate mode using SciPy (dropping NaN values first)
            clean_data = numeric_col.dropna()
            if not clean_data.empty:
                mode_result = stats.mode(clean_data, keepdims=True)
                mode_val = mode_result.mode[0]
                mode_count = mode_result.count[0]
            else:
                mode_val, mode_count = np.nan, 0
            
            print(f"\n--- Metrics for [{col}] Column ---")
            
            # FIXED PRINT STATEMENT: Combined into a single formatted string block
            metrics_string = (
                f"Mean: {mean_val:.2f} | "
                f"Median: {median_val:.2f} | "
                f"Standard Deviation: {std_val:.2f} | "
                f"Mode: {mode_val:.2f} (appeared {mode_count} times)"
            )
            print(metrics_string)
            
        else:
            print(f"\nColumn '{col}' not found in the dataset.")
            print(f"Available columns are: {df.columns.tolist()}")
            
    print("="*50)

# FIXED ENTRY POINT: Calls the correct function name
if __name__ == "__main__":
    perform_descriptive_analysis("./data/input/AusApparalSales4thQrt2020.csv")
