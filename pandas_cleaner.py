import pandas as pd

df = pd.read_csv('dirty_data/episode_dates.csv')

df.insert(0, 'episode_id', range(1, len(df) + 1))

df['month'] = df['air_date'].str.split().str[0]

df.to_csv('clean_data/episode_dates.csv', index=False)

