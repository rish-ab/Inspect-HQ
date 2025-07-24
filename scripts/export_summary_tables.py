import pandas as pd
import os

# Ensure output directory exists
os.makedirs("data", exist_ok=True)

# Load enriched data
df = pd.read_csv("data/enriched_risks.csv")

# 🔹 Summary 1: Average risk per firm over time
risk_by_firm_year = df.groupby(['firm_name', 'year'])['risk_per_100_engagements'].mean().reset_index()
risk_by_firm_year.to_csv("data/risk_by_firm_year.csv", index=False)

# 🔹 Summary 2: Average audit effectiveness by year
effectiveness_trend = df.groupby('year')['audit_effectiveness_score'].mean().reset_index()
effectiveness_trend.to_csv("data/audit_effectiveness_trend.csv", index=False)

# 🔹 Summary 3: Count of high/medium/low risk levels by year
risk_level_counts = df.groupby(['year', 'risk_level']).size().reset_index(name='count')
risk_level_counts.to_csv("data/risk_level_counts.csv", index=False)

# 🔹 Summary 4: AI usage vs. audit score
ai_vs_score = df.groupby('ai_used_flag')['audit_effectiveness_score'].mean().reset_index()
ai_vs_score.to_csv("data/ai_vs_audit_score.csv", index=False)

print("✅ All summary tables exported for Power BI use.")
