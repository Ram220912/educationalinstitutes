#Task 2C
import pandas as pd

def analyze_broader_categories(file_path):
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()
    
    categories = ['State', 'Time']
    
    print("="*50)
    print("    HIGHEST & LOWEST SALES BY OTHER ENTITIES")
    print("="*50)
    
    for category in categories:
        if category in df.columns:
            summary = df.groupby(category)['Sales'].sum()
            highest = summary.idxmax()
            lowest = summary.idxmin()
            
            print(f"--- Analysis by [{category}] ---")
            print(f"Highest Performance: {highest:<8} (${summary[highest]:,})")
            print(f"Lowest Performance : {lowest:<8} (${summary[lowest]:,})\n")
    print("="*50)

if __name__ == "__main__":
    csv_file = "./data/input/AusApparalSales4thQrt2020.csv"
    analyze_broader_categories(csv_file)
