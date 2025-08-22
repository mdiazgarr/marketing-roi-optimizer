import pandas as pd
import joblib

# Load model and processed data
model = joblib.load('models/roi_predictor.pkl')
df = pd.read_csv('data/processed/engineered.csv')

# Predict ROI
features = ['Clicks', 'Impressions', 'Cost', 'Conversions', 'CPC', 'CTR', 'CPA']
df['Predicted_ROI'] = model.predict(df[features])

# Rank campaigns
df_sorted = df.sort_values(by='Predicted_ROI', ascending=False)

# Simulate reallocating total budget to top 25% of campaigns
top_25 = int(len(df_sorted) * 0.25)
top_campaigns = df_sorted.head(top_25)
budget = df['Cost'].sum()
total_predicted_return = (top_campaigns['Predicted_ROI'] * top_campaigns['Cost']).sum()

print(f"Original budget: ${budget:,.2f}")
print(f"Total predicted return if allocated to top 25%: ${total_predicted_return:,.2f}")
