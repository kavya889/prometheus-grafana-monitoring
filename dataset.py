import pandas as pd
import os

# Check if file exists
if os.path.exists('ai_job_trends_dataset.csv'):
    print("Dataset found!")
else:
    print("Dataset not found!")

# Load CSV
df = pd.read_csv('ai_job_trends_dataset.csv')
print(df.head())  # Show first 5 rows
