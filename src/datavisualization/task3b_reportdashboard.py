#Task3-B Report Dashboard
#Task C - B - Daily, Weekly, Monthly, and quarterly dashboard
import io
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def main(input_path):
    # Set a professional visual style suited for executive presentation
    sns.set_theme(style="whitegrid")
    plt.rcParams.update({"font.size": 11, "axes.labelsize": 12, "axes.titlesize": 14})

    # ==========================================
    # 1. LOAD AND PREPROCESS DATA
    # ==========================================

    df = pd.read_csv(input_path)
    # Read the data and clean text trailing spaces
    df.columns = df.columns.str.strip()
    for col in ["Time", "State", "Group"]:
        df[col] = df[col].str.strip()

    # Convert Date strings to datetime objects safely
    df["Date"] = pd.to_datetime(df["Date"], format="%d-%b-%Y")

    # Create structural time periods for the executive dashboard horizons
    df["Day"] = df["Date"].dt.strftime("%Y-%m-%d")
    # Calculate week starting on Monday
    df["Week"] = df["Date"].dt.to_period("W").dt.start_time.dt.strftime("%Y-%m-%d")
    df["Month"] = df["Date"].dt.strftime("%Y-%m")
    df["Quarter"] = df["Date"].dt.to_period("Q").astype(str)

    # ==========================================
    # 2. GENERATE STRATEGIC DASHBOARD CHARTS
    # ==========================================

    # Configure grid canvas layout (2 Rows x 2 Columns)
    fig, axes = plt.subplots(2, 2, figsize=(18, 12))
    fig.suptitle(
        "AUSTRALIAN APPAREL CO. — STRATEGIC S&M PERFORMANCE",
        fontsize=18,
        weight="bold",
        y=0.96,
    )

    # ------------------------------------------
    # Chart 1: DAILY HORIZON — Unit Sales Trend by Group
    # ------------------------------------------
    daily_sales = df.groupby(["Day", "Group"])["Unit"].sum().reset_index()
    sns.boxplot(
        data=daily_sales,
        x="Day",
        y="Unit",
        hue="Group",
        ax=axes[0, 0]
    )
    axes[0, 0].set_title("Daily Unit Sales Distribution by Group")
    axes[0, 0].tick_params(axis='x', rotation=45)

    # ------------------------------------------
    # Chart 2: WEEKLY HORIZON — Revenue Generation by State
    # ------------------------------------------
    weekly_sales = df.groupby(["Week", "State"])["Sales"].sum().reset_index()
    sns.boxplot(
        data=weekly_sales,
        x="Week",
        y="Sales",
        hue="State",
        ax=axes[0, 1]
    )
    axes[0, 1].set_title("Weekly Sales Distribution by State")
    axes[0, 1].tick_params(axis='x', rotation=45)

    # ------------------------------------------
    # Chart 3: MONTHLY HORIZON — Revenue Mix by Shopping Time
    # ------------------------------------------
    monthly_sales = df.groupby(["Month", "Time"])["Sales"].sum().reset_index()
    sns.boxplot(
        data=monthly_sales,
        x="Month",
        y="Sales",
        hue="Time",
        ax=axes[1, 0]
    )
    axes[1, 0].set_title("Monthly Sales Distribution by Time")

    # ------------------------------------------
    # Chart 4: QUARTERLY HORIZON — Performance Deep-Dive
    # ------------------------------------------
    quarterly_group = df.groupby(["Quarter", "Group"])["Sales"].sum().reset_index()
    sns.boxplot(
        data=quarterly_group,
        x="Quarter",
        y="Sales",
        hue="Group",
        ax=axes[1, 1]
    )
    axes[1, 1].set_title("Quarterly Sales Distribution by Group")

    # Optimize spatial distribution to prevent sub-plot text overlapping
    plt.tight_layout(rect=[0, 0.03, 1, 0.93])

    # Save high-resolution copy for corporate board decks & display dashboard
    plt.savefig("dashboard.png", dpi=300)
    plt.show()

if __name__ == "__main__":
    csv_file = "./data/input/AusApparalSales4thQrt2020.csv"
    main(csv_file)
