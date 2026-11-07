import pandas as pd

def logistics_delivery_operations(input_path):
    # Load data
    try:
        df = pd.read_csv(input_path)
        df.columns = df.columns.str.strip()
        df['State'] = df['State'].str.strip()
    except FileNotFoundError:
        print("Error: Please provide the input CSV file.")
        exit()

    # Operation: Assess logistics footprint, parcel volume, and revenue by destination State
    logistics_zones = df.groupby('State').agg(
        Total_Parcels_Shipped=('Unit', 'sum'),
        Total_Shipping_Value=('Sales', 'sum'),
        Unique_Delivery_Days=('Date', 'nunique')
    ).reset_index()

    # Sort by parcel volume to rank highest load distribution channels
    logistics_zones = logistics_zones.sort_values(by='Total_Parcels_Shipped', ascending=False)

    # Save logistics layout data
    logistics_zones.to_csv('./data/output/logistics_delivery_metrics.csv', index=False)
    print("Successfully generated: logistics_delivery_metrics.csv")
if __name__ == "__main__":
    input_path = "./data/input/AusApparalSales4thQrt2020.csv"
    logistics_delivery_operations(input_path)