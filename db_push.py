import pandas as pd
import psycopg2

conn = psycopg2.connect(dbname="the_joy_of_coding",
                        user="postgres",
                        password="peepeepoopoo",
                        host="localhost",
                        port="5432")

cur = conn.cursor()


colors_df = pd.read_csv('clean_data/colors.csv')
episode_colors_df = pd.read_csv('clean_data/episode_colors.csv')
episode_dates_df = pd.read_csv('clean_data/episode_dates.csv')
episode_subjects_df = pd.read_csv('clean_data/episode_subjects.csv')
months_df = pd.read_csv('clean_data/months.csv')
subjects_df = pd.read_csv('clean_data/subjects.csv')


# Insert date/month data into the 'episodes' table
episodes_table_insert = """
    INSERT INTO episodes (episode_id, title, air_date, month_name)
    VALUES (%s, %s, %s, %s);
"""
for row in episode_dates_df.itertuples(index=False):
    cur.execute(episodes_table_insert, row)

# Insert color data into the 'episode' table
episode_colors_table_insert = """
    UPDATE episodes
    SET color_id = (%s)
    WHERE episode_id = (%s);
"""
for row in episode_colors_df.itertuples(index=False):
    cur.execute(episode_colors_table_insert, [row[1], row[0]])

# Insert subject data into the 'subjects' table
episode_subjects_table_insert = """
    UPDATE episodes
    SET subject_id = (%s)
    WHERE episode_id = (%s);
"""
for row in episode_subjects_df.itertuples(index=False):
    cur.execute(episode_subjects_table_insert, [row[1], row[0]])


# Insert color data into the 'colors' table
colors_table_insert = """
    INSERT INTO colors (color_id, color_name, episode_id)
    VALUES (%s, %s, %s);
"""
for row in colors_df.itertuples(index=False):
    cur.execute(colors_table_insert, row)

# Insert subject data into the 'subjects' table
subjects_table_insert = """
    INSERT INTO subjects (subject_id, subject_name, episode_id)
    VALUES (%s, %s, %s);
"""
for row in subjects_df.itertuples(index=False):
    cur.execute(subjects_table_insert, row)

# Insert month data into the 'months' table
months_table_insert = """
    INSERT INTO months (month_name, episode_id)
    VALUES (%s, %s);
"""
for row in months_df.itertuples(index=False):
    cur.execute(months_table_insert, row)


conn.commit()

cur.close()
conn.close()

