import pandas as pd

def generate_periodic_reports(file_path):
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()
    
    # Convert string date column to official datetime structures
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%Y')
    
    # Generate explicit grouping tracking variables
    df['Weekly'] = df['Date'].dt.to_period('W').astype(str)
    df['Monthly'] = df['Date'].dt.to_period('M').astype(str)
    df['Quarterly'] = df['Date'].dt.to_period('Q').astype(str)
    
    print("="*60)
    print("                PERIODIC PREVIEW AND GENERATION")
    print("="*60)

    # 1. Weekly Report
    weekly_report = df.groupby('Weekly').agg(
        Units_Sold_Sum=('Unit', 'sum'),
        Total_Sales=('Sales', 'sum')
    ).reset_index()
    
    print("\n📊 TOP 5 ROWS: WEEKLY SALES REPORT")
    print(weekly_report.head(5))
    print("-" * 45)
    #weekly_report.to_csv("/content/weekly_sales_report.csv", index=False)
    weekly_report.to_csv("./data/output/weekly_report.csv", index=False)
    # 2. Monthly Report
    monthly_report = df.groupby('Monthly').agg(
        Units_Sold_Sum=('Unit', 'sum'),
        Total_Sales=('Sales', 'sum')
    ).reset_index()
    
    print("\n📊 TOP 5 ROWS: MONTHLY SALES REPORT")
    print(monthly_report.head(5))
    print("-" * 45)
    #monthly_report.to_csv("/content/monthly_sales_report.csv", index=False)
    monthly_report.to_csv("./data/output/monthly_report.csv", index=False)
    # 3. Quarterly Report
    quarterly_report = df.groupby('Quarterly').agg(
        Units_Sold_Sum=('Unit', 'sum'),
        Total_Sales=('Sales', 'sum')
    ).reset_index()
    
    print("\n📊 TOP 5 ROWS: QUARTERLY SALES REPORT")
    print(quarterly_report.head(5))
    print("-" * 45)
    #quarterly_report.to_csv("/content/quarterly_sales_report.csv", index=False)
    quarterly_report.to_csv("./data/output/quarterly_report.csv", index=False)
    print("\n" + "="*60)
    print("REPORT SAVING PROCESS COMPLETE")
    print("="*60)

  
    print("="*50)
    print("        PERIODIC REPORT GENERATION COMPLETE")
    print("="*50)
    print("The following report files have been successfully saved:")
    print(" ✔ weekly_sales_report.csv")
    print(" ✔ monthly_sales_report.csv")
    print(" ✔ quarterly_sales_report.csv")
    print("="*50)

if __name__ == "__main__":
    csv_file = "./data/input/AusApparalSales4thQrt2020.csv"
    generate_periodic_reports(csv_file)
