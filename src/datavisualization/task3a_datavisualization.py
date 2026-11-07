import io
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_total_sales_by_state(file_path):
    # 1. Load and clean the dataset
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()
    
    df['State'] = df['State'].astype(str).str.strip().str.upper()
    df['Time']=df.Time.str.strip()
    # 2. Derive the aggregated total sales grouped by State
    total_sales_by_state = df.groupby('State')['Sales'].sum().reset_index()
    total_sales_by_state = total_sales_by_state.sort_values(by='Sales', ascending=False)
    # Rename the column inside the summary so it does not conflict with the raw rows
    total_sales_by_state = total_sales_by_state.rename(columns={'Sales': 'Total_Sales'})

    # FIX: Merge the summary DataFrame back into your original DataFrame
    df = df.merge(total_sales_by_state, on='State', how='left')

    df['Total_Sales']=total_sales_by_state

    # 1. Calculate the totals as a separate DataFrame
    state_sales_dict = df.groupby('State')['Sales'].sum().to_dict()
    
    print("\n📦 Generated Python Mapping Dictionary:")
    #print(state_sales_dict)
    #print("-" * 60)
    
    # 3. MERGE THE NEW COLUMN: Use .map() to match the dictionary keys to the 'State' column
    df['Total_Sales_By_State'] = df['State'].map(state_sales_dict)
    
    print("\n--- Updated DataFrame with Merged Column (First 5 Rows) ---")
    print(df[['Date', 'State', 'Group', 'Sales', 'Total_Sales_By_State']].head(5))
    print("=" * 60)

    total_sales_by_state = df.groupby('State')['Sales'].sum().reset_index()

    # 2. Rename the column to avoid name clashing with the original data
    total_sales_by_state = total_sales_by_state.rename(columns={'Sales': 'Total_Sales'})
    #total_sales_by_state

    # 3. Merge it back cleanly based on the matching 'State' row value
    # This automatically calculates state sums and stretches them to match your original data rows
    df.merge(
        total_sales_by_state,
        on='State',
        how='left'
    )
    df['Total_Sales'] = df.groupby('State')['Sales'].transform('sum')
    
    # 3. Initialize the visualization layout
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))
    
    # 4. Construct the bar plot mapping the derived total_sales_by_state
    


    plt.figure(figsize=(8,5))
    sns.boxplot(data=df,x="Time", y="Total Sales")
    plt.xlabel("Time of Day")
    plt.ylabel("Total_Sales")
    plt.grid(axis='y', linestyle="--",alpha=0.7)
    plt.show()    

    # 5. Fine-tune executive readability and labels
        
    plt.tight_layout()

    sns.boxplot(data=df,x="Date", y="Total Sales")
    plt.xlabel("Date")
    plt.ylabel("Total_Sals")
    plt.grid(axis='y', linestyle="--",alpha=0.7)
    plt.show()    

    # 5. Fine-tune executive readability and labels
        
    plt.tight_layout(rect=[0, 0.03, 1, 0.93])
    
    # Save the polished chart to your working environment
    plt.savefig("total_sales_by_state.png", dpi=300)
    #plt.savefig('./data/output/total_sales_by_state.png', dpi=300)
    print("✔ Visualisation created and saved as 'total_sales_by_state.png'")
    #uploadoutput("total_sales_by_state.png")
    plt.show()
    

def merge_column_using_dictionary(file_path):
    # 1. Load the existing DataFrame
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()
    df['State'] = df['State'].astype(str).str.strip().str.upper()
    
    print("--- Original DataFrame Structure (First 5 Rows) ---")
    print(df[['Date', 'State', 'Group', 'Sales']].head(5))
    print("-" * 60)
    
    # 2. Generate an aggregated summary and convert it into a Python Dictionary
    # .to_dict() creates a mapping structure like: {'WA': 275000, 'NT': 250000, ...}
    state_sales_dict = df.groupby('State')['Sales'].sum().to_dict()
    
    print("\n📦 Generated Python Mapping Dictionary:")
    print(state_sales_dict)
    print("-" * 60)
    
    # 3. MERGE THE NEW COLUMN: Use .map() to match the dictionary keys to the 'State' column
    df['Total_Sales_By_State'] = df['State'].map(state_sales_dict)
    
    print("\n--- Updated DataFrame with Merged Column (First 5 Rows) ---")
    print(df[['Date', 'State', 'Group', 'Sales', 'Total_Sales_By_State']].head(5))
    print("=" * 60)
    
    # Optional: Save the updated DataFrame back to a CSV file
    # df.to_csv("updated_sales_data.csv", index=False)
        
    # 3. Initialize the visualization layout
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))
    
    # 4. Construct the bar plot mapping the derived total_sales_by_state
    


    plt.figure(figsize=(8,5))
    sns.boxplot(data=df,x="Time", y="Sales")
    plt.xlabel("Time of Day")
    plt.ylabel("Sales")
    plt.grid(axis='y', linestyle="--",alpha=0.7)
    plt.show()    

    # 5. Fine-tune executive readability and labels
        
    plt.tight_layout()

    sns.boxplot(data=df,x="Date", y="Sales")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.grid(axis='y', linestyle="--",alpha=0.7)
    plt.show()    

    # 5. Fine-tune executive readability and labels
        
    plt.tight_layout(rect=[0, 0.03, 1, 0.93])
    
    # Save the polished chart to your working environment
    plt.savefig("total_sales.png", dpi=300)
    print("✔ Visualisation created and saved as 'total_sales_by_state.png'")
    plt.show()

if __name__ == "__main__":
    csv_file = "./data/input/AusApparalSales4thQrt2020.csv"
    merge_column_using_dictionary(csv_file)

    #plot_total_sales_by_state(csv_file)
