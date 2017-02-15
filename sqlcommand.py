import psycopg2

def create_table():
    try:
        conn = connect()
        cursor = conn.cursor()

	# user id PRMIARY KEY, username unike
        create_command = "\
            create table useraccount ( \
                user_id SERIAL PRIMARY KEY, \
                username char(40) UNIQUE NOT NULL, \
                password char(32) NOT NULL, \
                salt char(32) NOT NULL \
            ); \
        "
        cursor.execute(create_command)

        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
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
        print(e)
        cursor.close()
        conn.close()


def read():
    try:
        conn = connect()
        cursor = conn.cursor()

        cursor.execute("SELECT * from useraccount;")
        row = cursor.fetchall()
        print(row)
        cursor.close()
        conn.close()
        return row
    except Exception as e:
        print(e)
        cursor.close()
        conn.close()

def filter(username):
    try:
        conn = connect()
        cursor = conn.cursor()
        command = "SELECT password, salt from useraccount where username='{0}'".format(username)
        cursor.execute(command)
        print(command)
        row = cursor.fetchone()
        print(row)
        cursor.close()
        conn.close()
        return row
    except Exception as e:
        print(e)
        cursor.close()
        conn.close()

def connect():
    connect_str = "dbname=stockDb user=william host=localhost " + \
                  "password=wflu"
    conn = psycopg2.connect(connect_str)
    return conn
