import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import io

def task1d_groupbynormalizeddata(input_path):
  # Load the cleaned dataset
  #df = pd.read_csv("input_path")
  df = pd.read_csv(input_path, sep=None, engine='python')

  # Standardize column names
  df.columns = df.columns.str.strip().str.lower()

  # Convert date column
  df["date"] = pd.to_datetime(df["date"], errors="coerce")

  # 1. Total sales by state
  state_sales = (
      df.groupby("state")["sales"]
        .sum()
        .sort_values(ascending=False)
  )

  print("1. Total Sales by State")
  print(state_sales.reset_index(name="total_sales"))

  # 2. Sales by product group
  group_sales = (
      df.groupby("group")["sales"]
        .agg(["sum", "mean", "count"])
        .sort_values("sum", ascending=False)
  )

  print("2. Sales by Product Group")
  print(group_sales)

  # 3. Sales by state and product group
  state_group_sales = (
      df.groupby(["state", "group"])["sales"]
        .sum()
        .reset_index(name="total_sales")
  )
  # Save the DataFrame to a CSV file
  state_group_sales.to_csv("./data/output/state_group_sales.csv", index=False)

  print("3. Sales by State and Product Group")
  print("State_Group_Sales",state_group_sales)
  print ("State_Group_Sales", state_group_sales)
  # Step 11: Download the output CSV file
  ##files.download(output_file)
if __name__ == "__main__":
    task1d_groupbynormalizeddata("./data/output/normalized_numeric.csv")
