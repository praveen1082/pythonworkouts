import psycopg2 as database
import psycopg2.extras

DB_HOST = 'localhost'
DB_NAME = 'test'
DB_USER = 'postgres'
DB_PASS = 'praveen'
conn = None

try:
    with database.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST) as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            create_script = '''CREATE TABLE IF NOT EXISTS employee(
                            id int PRIMARY KEY,
                            name varchar(40) NOT NULL,
                            salary int,
                            dept_id varchar(30)
            )'''
            cur.execute(create_script)
            # insert_script = 'INSERT INTO employee (id,name,salary,dept_id) VALUES (%s,%s,%s,%s)'
            # insert_values = [(1, 'praveen', 20000, 'd2'), (2, 'nabin', 50000, 'd1'), (3, 'sawbeen', 10000, 'd1')]
            # for record in insert_values:
            #     cur.execute(insert_script, record)
            update_script = 'UPDATE employee SET salary = salary + (salary * 0.5)'
            cur.execute(update_script)
            cur.execute('Select * from employee')
            for record in cur.fetchall():
                print(record['name'], record['salary'])
            # update_script = 'UPDATE employee SET salary = salary + (salary * 0.5)'
            # cur.execute(update_script)
            # conn.commit()
except Exception as error:
    print(error)
finally:
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



