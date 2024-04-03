import psycopg2

conn = psycopg2.connect(dbname="the_joy_of_coding",
                        user="postgres",
                        password="peepeepoopoo",
                        host="localhost",
                        port="5432")

cur = conn.cursor()

with open('create_db_tables.sql', 'r') as file:
    create_table_queries = file.read()

cur.execute(create_table_queries)

conn.commit()

cur.close()
conn.close()
