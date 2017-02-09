import psycopg2

try:
    connect_str = "dbname='stockDb' user='william' host='localhost' " + \
                  "password='wflu'"
    # use our connection values to establish a connection
    conn = psycopg2.connect(connect_str)
    # create a psycopg2 cursor that can execute queries
    cursor = conn.cursor()
    # create a new table with a single column called "name"
    cursor.execute("""CREATE TABLE user (name char(40));""")
    # run a SELECT statement - no data in there, but we can try it
    cursor.execute("""SELECT * from USER""")
    rows = cursor.fetchall()
    print(rows)
except Exception as e:
    print("Uh oh, can't connect. Invalid dbname, user or password?")
    print(e)
