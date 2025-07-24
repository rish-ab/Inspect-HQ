import pandas as pd
import os

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

# Load the cleaned dataset
df = pd.read_csv("data/cleaned_big4_risks.csv")

# 🚨 Feature 1: Create an overall risk score (simple composite metric)
df['risk_score'] = df['high_risk_cases'] + df['compliance_violations'] + df['fraud_cases_detected']

# 🚨 Feature 2: Normalize risk score per 100 audit engagements (to compare firms fairly)
df['risk_per_100_engagements'] = (df['risk_score'] / df['total_audit_engagements']) * 100

# 🚨 Feature 3: Categorize risk level based on normalized risk
def categorize_risk(value):
    if value > 10:
        return 'High'
    elif value > 5:
        return 'Medium'
    else:
        return 'Low'

df['risk_level'] = df['risk_per_100_engagements'].apply(categorize_risk)

# 🚨 Feature 4: Flag if AI was used for auditing
df['ai_used_flag'] = df['ai_used_for_auditing'].apply(lambda x: 1 if str(x).strip().lower() == 'yes' else 0)

# Save enriched data
df.to_csv("data/enriched_risks.csv", index=False)
print("✅ Enriched data saved to: data/enriched_risks.csv")

# Preview
print(df[['firm_name', 'year', 'risk_score', 'risk_per_100_engagements', 'risk_level', 'ai_used_flag']].head())
