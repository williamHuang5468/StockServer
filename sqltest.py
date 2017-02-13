import psycopg2

# try:
#     connect_str = "dbname=stockDb user=william host=localhost " + \
#                   "password=wflu"
#     conn = psycopg2.connect(connect_str)
#     cursor = conn.cursor()
#     cursor.execute("""CREATE TABLE useraccount (username char(40) PRIMARY KEY, password char(40), salt char(40));""")
#     cursor.execute("INSERT INTO useraccount (username, password, salt) VALUES (%s, %s, %s)", ("Ann", "hello", "asdfjlkj"))
#     cursor.execute("""SELECT * from useraccount""")
#     rows = cursor.fetchall()
#     print(rows)
# 
#     conn.commit()
#     cursor.close()
#     conn.close()
# except Exception as e:
#     print("Uh oh, can't connect. Invalid dbname, user or password?")
#     print(e)
#     cursor.close()
#     conn.close()

def create_table():
    try:
        conn = connect()
        cursor = conn.cursor()

	# user id PRMIARY KEY, username unike
        cursor.execute("CREATE TABLE useraccount (username char(40) PRIMARY KEY, password char(32), salt char(32));")

        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)
        cursor.close()
        conn.close()

def drop(db):
    try:
        conn = connect()
        cursor = conn.cursor()

        cursor.execute("Drop Table " + db + "")

        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)
        cursor.close()
        conn.close()


def create_user(username, password, salt):
    try:
        conn = connect()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO useraccount (username, password, salt) VALUES (%s, %s, %s)", (username, password, salt))

        cursor.execute("SELECT * from useraccount")
        row = cursor.fetchall()
        print(row)
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)
        cursor.close()
        conn.close()

def filter(username):
    try:
        conn = connect()
        cursor = conn.cursor()

        cursor.execute("SELECT password, salt from useraccount where username=%s", (username))
        row = cursor.fetchone()
        print(row)
        cursor.close()
        conn.close()
        return row
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)
        cursor.close()
        conn.close()


def connect():
    connect_str = "dbname=stockDb user=william host=localhost " + \
                  "password=wflu"
    conn = psycopg2.connect(connect_str)
    return conn

p, s = filter("a")
print(p, s)
print(p.strip() == "123")
