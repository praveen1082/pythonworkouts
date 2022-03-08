import psycopg2 as database
import psycopg2.extras

DB_HOST = 'localhost'
DB_NAME = 'test'
DB_USER = 'postgres'
DB_PASS = 'praveen'

try:
    conn = database.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
    cur = conn.cursor()
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
# cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
# with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
#     cur.execute("SELECT * FROM dividend;", (1,))
#     # print(cur.fetchall())
#     print(cur.fetchone()['company'])
#     conn.commit()
#
# conn.close()



