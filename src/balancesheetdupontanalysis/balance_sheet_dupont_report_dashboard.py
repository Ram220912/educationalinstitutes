import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def finance_balance_sheet_dupont_analysis_report_dashboard(input_path):
    # Set professional plotting aesthetics
    sns.set_theme(style="whitegrid")
    plt.rcParams['font.sans-serif'] = 'Arial'
    plt.rcParams['font.family'] = 'sans-serif'
    
    # 1. Load Data
    try:
        df = pd.read_csv(f'{input_path}')
    except FileNotFoundError:
        print(f"❌ '{input_path}.csv' not found. Please check your data file path.")
        return

    # 2. Global Aggregated Metrics (Simulating full dataset evaluation)
    total_revenue = df['Revenue'].sum()
    total_net_income = df['Net_Income'].sum()
    total_assets = df['Total_Assets'].sum()
    total_equity = df['Total_Shareholders_Equity'].sum()

    # DuPont Calculations
    net_profit_margin = total_net_income / total_revenue if total_revenue > 0 else 0
    asset_turnover = total_revenue / total_assets if total_assets > 0 else 0
    equity_multiplier = total_assets / total_equity if total_equity > 0 else 0
    return_on_equity = net_profit_margin * asset_turnover * equity_multiplier

    # 3. Print Core KPI Cards & Tree Breakdown to Console
    print("=" * 60)
    print(" 📊 DUPONT ANALYSIS & FINANCIAL PERFORMANCE SUMMARY")
    print("=" * 60)
    print(f"🏆 Return on Equity (ROE)     : {return_on_equity:.2%}")
    print(f"📈 Net Profit Margin          : {net_profit_margin:.2%}")
    print(f"🔄 Asset Turnover             : {asset_turnover:.2f}x")
    print(f"⚖️  Equity Multiplier           : {equity_multiplier:.2f}x")
    print("-" * 60)
    print("🌲 DuPont Framework Drivers Breakdown:")
    print(f"🏃‍♂️ Operational Drivers:")
    print(f"   - Total Revenue Generated  : ${total_revenue:,.2f}")
    print(f"   - Bottom-line Net Income   : ${total_net_income:,.2f}")
    print(f"🏦 Structural Leverage Drivers:")
    print(f"   - Total Asset Base         : ${total_assets:,.2f}")
    print(f"   - Shareholder Equity       : ${total_equity:,.2f}")
    print("=" * 60)

    # 4. Prepare Aggregate Comparison Data
    sub_summary = df.groupby('Subsidiary').sum().reset_index()
    sub_summary['ROE (%)'] = (sub_summary['Net_Income'] / sub_summary['Total_Shareholders_Equity']) * 100
    sub_summary['Net Profit Margin (%)'] = (sub_summary['Net_Income'] / sub_summary['Revenue']) * 100

    # 5. Visualizations Section (Creating a combined dashboard figure)
    fig, axes = plt.subplots(1, 2, figsize=(16, 7))
    fig.suptitle("Entity Performance Comparisons (DuPont Decomposition)", fontsize=16, fontweight='bold', y=0.98)

    # Plot 1: Return on Equity (ROE %) by Corporate Entity (Bar Chart)
    sns.barplot(
        data=sub_summary, 
        x='Subsidiary', 
        y='ROE (%)', 
        hue='Subsidiary',
        palette='pastel', 
        ax=axes[0],
        legend=False
    )
    axes[0].set_title("Return on Equity (ROE %) by Corporate Entity", fontsize=13, pad=10)
    axes[0].set_xlabel("Subsidiary", fontsize=11)
    axes[0].set_ylabel("ROE (%)", fontsize=11)
    
    # Add text labels on top of the bars
    for container in axes[0].containers:
        axes[0].bar_label(container, fmt='%.2f%%', label_type='edge', padding=3, fontsize=10)

    # Plot 2: Scale vs Efficiency (Bubble/Scatter Chart)
    # Scale total asset sizing for visible presentation bubble weights
    sizes = (sub_summary['Total_Assets'] / sub_summary['Total_Assets'].min()) * 400
    
    scatter = sns.scatterplot(
        data=sub_summary, 
        x='Revenue', 
        y='Net Profit Margin (%)', 
        hue='Subsidiary', 
        size=sizes,
        sizes=(200, 800),
        palette='Set2', 
        ax=axes[1],
        alpha=0.8
    )
    axes[1].set_title("Scale vs Efficiency: Revenue vs Net Profit Margin\n(Size represents Asset Volume)", fontsize=13, pad=10)
    axes[1].set_xlabel("Total Revenue ($)", fontsize=11)
    axes[1].set_ylabel("Net Profit Margin (%)", fontsize=11)
    
    # Format X-axis with currency format
    axes[1].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"${x:,.0f}"))
    
    # Clean up legend to only show Subsidiaries, filter out bubble sizing handles
    handles, labels = axes[1].get_legend_handles_labels()
    # Filter to only keep unique Subsidiary labels (first 4 items)
    axes[1].legend(handles[0:4], labels[0:4], title="Subsidiaries", loc="best")

    # Final adjustments and layout rendering
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Point directly to the base name of your CSV file
    input_filename_base = "./data/input/finance_balance_sheet_dupont.csv"
    finance_balance_sheet_dupont_analysis_report_dashboard(input_filename_base)
