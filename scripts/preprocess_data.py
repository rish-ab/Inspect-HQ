import pandas as pd
import os

# Ensure output directory exists
os.makedirs("data", exist_ok=True)

# Load original file
df = pd.read_csv("data/big4_risk_insights.csv")

# Print initial structure
print("📋 Initial Columns:", df.columns.tolist())
print("📈 Initial rows:", len(df))

# Step 1: Drop rows with critical missing values
df.dropna(subset=["Year", "Firm_Name", "High_Risk_Cases", "Compliance_Violations"], inplace=True)

# Step 2: Standardize column names (optional)
df.columns = df.columns.str.strip().str.replace(" ", "_").str.lower()

# Step 3: Clean string columns
df['firm_name'] = df['firm_name'].str.strip()

# Optional: Convert Year to int (if needed)
df['year'] = df['year'].astype(int)

# Save cleaned data
df.to_csv("data/cleaned_big4_risks.csv", index=False)
print("✅ Cleaned data saved to: data/cleaned_big4_risks.csv")
print("📊 Cleaned Preview:")
print(df.head())
# Print final structure