#Task 2b - Highest and Lowest Sales

import pandas as pd

def find_highest_lowest_groups(file_path):
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()
    
    # Group by 'Group' and aggregate the Sales column
    group_sales = df.groupby('Group')['Sales'].sum().reset_index()
    
    # Sort values to explicitly see the ranking
    group_sales = group_sales.sort_values(by='Sales', ascending=False)
    
    print("="*50)
    print("         TOTAL SALES BY GROUP")
    print("="*50)
    for idx, row in group_sales.iterrows():
        print(f"Group: {row['Group']:<10} | Total Sales: ${row['Sales']:,}")
    print("="*50)
    
    # Identify highest and lowest using idxmax() and idxmin()
    highest_group = group_sales.loc[group_sales['Sales'].idxmax()]
    lowest_group = group_sales.loc[group_sales['Sales'].idxmin()]
    
    print(f"\n🏆 Highest Sales Group: {highest_group['Group']} (${highest_group['Sales']:,})")
    print(f"📉 Lowest Sales Group : {lowest_group['Group']} (${lowest_group['Sales']:,})")
    print("="*50)

if __name__ == "__main__":
    csv_file = "sales_data.csv"
    find_highest_lowest_groups("./data/input/AusApparalSales4thQrt2020.csv")
