import psycopg2 as database

DB_HOST = 'localhost'
DB_NAME = 'test'
DB_USER = 'postgres'
DB_PASS = 'praveen'

conn = database.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

cur = conn.cursor()
cur.execute("SELECT * FROM dividend;", (1,))
# print(cur.fetchall())
print(cur.fetchone())
conn.close()


