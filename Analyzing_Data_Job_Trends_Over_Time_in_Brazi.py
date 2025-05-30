import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datasets import load_dataset

dataset = load_dataset("lukebarousse/data_jobs")
df = pd.DataFrame(dataset['train'])

df_brazil = df[df['country'] == 'Brazil'].copy()

df_brazil['job_post_month'] = pd.to_datetime(df_brazil['posted_at']).dt.to_period('M').astype(str)

job_month_counts = df_brazil.groupby('job_title')['job_post_month'].nunique()

top5_jobs = job_month_counts.sort_values(ascending=False).head(5)

plt.figure(figsize=(10,6))
sns.barplot(x=top5_jobs.values, y=top5_jobs.index, palette='viridis')
plt.xlabel('Number of Distinct Months Posted')
plt.ylabel('Job Title')
plt.title('Top 5 Most Spread Job Titles Across Months in Brazil')
plt.show()
