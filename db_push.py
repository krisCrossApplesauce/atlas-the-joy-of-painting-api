import pandas as pd
import psycopg2

conn = psycopg2.connect(dbname="the_joy_of_coding",
                        user="postgres",
                        password="peepeepoopoo",
                        host="localhost",
                        port="5432")

cur = conn.cursor()


colors_df = pd.read_csv('colors.csv')
episode_colors_df = pd.read_csv('episode_colors.csv')
episode_dates_df = pd.read_csv('episode_dates.csv')
episode_subjects_df = pd.read_csv('episode_subjects.csv')
subjects_df = pd.read_csv('subjects.csv')

# Insert data into the 'colors' table
colors_table_insert = """
    INSERT INTO colors (color_id, color_name)
    VALUES (%i, %s)
"""
for row in colors_df.itertuples(index=False):
    cur.execute(colors_table_insert, row)

# Insert data into the 'subjects' table
subjects_table_insert = """
    INSERT INTO subjects (subject_id, subject_name)
    VALUES (%i, %s)
"""
for row in subjects_df.itertuples(index=False):
    cur.execute(subjects_table_insert, row)

# Insert data into the 'episodes' table
episodes_table_insert = """
    INSERT INTO episodes (episode_id, air_date, month_id)
    VALUES (%i, %s, %s)
"""
for row in episode_dates_df.itertuples(index=False):
    cur.execute(episodes_table_insert, row)

# Insert data into the 'episode_colors' table
episode_colors_table_insert = """
    INSERT INTO episodes (colors)
    VALUES (%s)
"""
for row in episode_colors_df.itertuples(index=False):
    cur.execute(episode_colors_table_insert, row)

# Insert data into the 'episode_subjects' table
episode_subjects_table_insert = """
    INSERT INTO episodes (subjects)
    VALUES (%s)
"""
for row in episode_subjects_df.itertuples(index=False):
    cur.execute(episode_subjects_table_insert, row)




conn.commit()

cur.close()
conn.close()

