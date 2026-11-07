import os
from pathlib import Path
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def task1a1b_datacleaning(input_path):
    # Dynamically locate paths relative to this script so it runs anywhere
    #base_dir = Path(__file__).resolve().parent.parent
    #print (f"Base Directory {base_dir}")
    #input_path = base_dir / "data" / "input" / "AusApparalSales4thQrt2020.csv"
    #output_dir = base_dir / "data" / "output"
    
    print(f"🔄 Searching for file at: {input_path}")
    
    try:
        df = pd.read_csv(input_path)
    except FileNotFoundError:
        # Fallback for Google Colab environment local directory root
        try:
            df = pd.read_csv(input_path)
        except FileNotFoundError:
            raise FileNotFoundError(
                f"Could not find 'AusApparalSales4thQrt2020.csv'. "
                f"Expected workspace location: {input_path}"
            )

    # Standardize column names: Date -> date, Sales -> sales, etc.
    df.columns = df.columns.str.strip().str.lower()

    print("\n✅ Data Successfully Loaded!")
    print("Original dataset shape:", df.shape)
    print("Available columns:", df.columns.tolist())

    # Check that required columns exist
    essential = ["date", "state", "group", "sales"]
    missing_columns = [col for col in essential if col not in df.columns]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}. "
            f"Available columns: {df.columns.tolist()}"
        )

    original_rows = len(df)

    # Remove rows missing essential values
    cleaned = df.dropna(subset=essential).copy()

    # Fill missing Unit values with the median, if the column exists
    if "unit" in cleaned.columns and cleaned["unit"].isna().any():
        unit_median = cleaned["unit"].median()
        cleaned["unit"] = cleaned["unit"].fillna(unit_median)
        print(f"\nFilled missing Unit values with median: {unit_median}")

    # Remove duplicate rows
    rows_before_duplicates = len(cleaned)
    cleaned = cleaned.drop_duplicates().copy()
    duplicates_removed = rows_before_duplicates - len(cleaned)

    # Standardize category formatting
    cleaned["state"] = cleaned["state"].astype(str).str.strip().str.title()
    cleaned["group"] = cleaned["group"].astype(str).str.strip().str.title()
    
    # Convert date column to official datetime format
    cleaned["date"] = pd.to_datetime(cleaned["date"], errors="coerce")

    
    #cleaned.to_csv(destination_file, index=False)
    # Also save a secondary copy to the current directory for absolute safety
    cleaned.to_csv("cleaned.csv", index=False)
    output_path = "./data/output/cleaned.csv"
    pd.DataFrame.to_csv(cleaned, output_path, index=False)
    # Display results
    print("\n--- Data Cleaning Summary ---")
    print("Original rows:", original_rows)
    print("Cleaned rows:", len(cleaned))
    print("Rows removed due to missing essential values:", original_rows - rows_before_duplicates)
    print("Duplicate rows removed:", duplicates_removed)
    
    print("\n--- First 5 Rows of Cleaned Data ---")
    print(cleaned.head())

    print(f"\n🎉 Cleaned dataset saved to: {cleaned}")


# FIX 1: Essential entry block to tell Python to actually run the program
if __name__ == "__main__":
    input_path = "./data/input/AusApparalSales4thQrt2020.csv"
    task1a1b_datacleaning(input_path)
