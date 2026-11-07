import pandas as pd

def inventory_order_management(input_path):
# Load data
    try:
        df = pd.read_csv(input_path)
        df.columns = df.columns.str.strip()
        df['Time'] = df['Time'].str.strip()
    except FileNotFoundError:
        print("Error: Please provide the input CSV file.")
        exit()

    # Operation: Measure picking throughput and processing requirements by Time of Day
    warehouse_throughput = df.groupby('Time').agg(
        Total_Garments_Processed=('Unit', 'sum'),
        Total_Invoiced_Value=('Sales', 'sum'),
        Fulfillment_Runs_Triggered=('Date', 'count')
    ).reset_index()

    # Calculate an intensity index for shift allocation
    total_units = warehouse_throughput['Total_Garments_Processed'].sum()
    warehouse_throughput['Shift_Workload_Percentage'] = (
        (warehouse_throughput['Total_Garments_Processed'] / total_units) * 100
    ).round(2)

    # Save operational dataset
    warehouse_throughput.to_csv('./data/output/inventory_order_management.csv', index=False)
    print("Successfully generated: warehouse_fulfillment_metrics.csv")

if __name__ == "__main__":
    input_path = "./data/input/AusApparalSales4thQrt2020.csv"
    inventory_order_management(input_path)