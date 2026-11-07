import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed for reproducibility
def finance_balance_sheet_dupont_analysis(input_path):
  np.random.seed(42)

  # Generate 1,000 rows of data
  num_rows = 1000

  # Generate base dates (spanning roughly 3-4 years)
  start_date = datetime(2023, 1, 1)
  dates = [start_date + timedelta(days=int(i * 1.3)) for i in range(num_rows)]

  # Define dimensions
  subsidiaries = ['North America Corp', 'EMEA Ltd', 'APAC Pty', 'LATAM SA']
  departments = ['Corporate', 'Retail', 'Wholesale', 'Digital Commerce']

  # Pre-allocate dictionary for performance
  data = {
      'Record_ID': [f'REC-{i:04d}' for i in range(1, num_rows + 1)],
      'Date': [d.strftime('%Y-%m-%d') for d in dates],
      'Subsidiary': np.random.choice(subsidiaries, size=num_rows),
      'Department': np.random.choice(departments, size=num_rows),
  }

  # Generate baseline Financial Metrics (simulated in USD)
  # Revenue and Net Income (Income Statement items for DuPont)
  data['Revenue'] = np.random.uniform(500000, 2500000, size=num_rows).round(2)
  # Net income is typically 5% to 15% of revenue
  data['Net_Income'] = (data['Revenue'] * np.random.uniform(0.05, 0.15, size=num_rows)).round(2)

  # Balance Sheet Items (Assets)
  data['Cash_Equivalents'] = np.random.uniform(50000, 300000, size=num_rows).round(2)
  data['Accounts_Receivable'] = np.random.uniform(80000, 400000, size=num_rows).round(2)
  data['Inventory'] = np.random.uniform(100000, 600000, size=num_rows).round(2)
  data['Property_Plant_Equipment'] = np.random.uniform(500000, 2000000, size=num_rows).round(2)

  # Calculate Total Assets
  data['Total_Assets'] = (
      data['Cash_Equivalents'] + 
      data['Accounts_Receivable'] + 
      data['Inventory'] + 
      data['Property_Plant_Equipment']
  ).round(2)

  # Balance Sheet Items (Liabilities & Equity)
  # Liabilities are generated to ensure accounting equation holds loosely before balancing out via Equity
  data['Accounts_Payable'] = np.random.uniform(40000, 250000, size=num_rows).round(2)
  data['Short_Term_Debt'] = np.random.uniform(20000, 150000, size=num_rows).round(2)
  data['Long_Term_Debt'] = np.random.uniform(300000, 1200000, size=num_rows).round(2)

  data['Total_Liabilities'] = (
      data['Accounts_Payable'] + 
      data['Short_Term_Debt'] + 
      data['Long_Term_Debt']
  ).round(2)

  # Total Equity defined strictly to satisfy: Assets = Liabilities + Equity
  data['Total_Shareholders_Equity'] = (data['Total_Assets'] - data['Total_Liabilities']).round(2)

  # Create DataFrame
  df = pd.DataFrame(data)

  # Save to CSV
  df.to_csv('./data/output/finance_balance_sheet_dupont.csv', index=False)
  print("Successfully generated 'finance_balance_sheet_dupont.csv' with 1,000 rows!")
if __name__ == "__main__":
    input_path = "./data/input/finance_balance_sheet_dupont.csv"
    finance_balance_sheet_dupont_analysis(input_path)