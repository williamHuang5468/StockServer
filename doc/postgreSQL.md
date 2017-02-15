# postgreSQL

## purpose

a doc that record something action.

## use

enter the `db`

  $ psql -l # list all the db

    Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
  ----------+----------+----------+-------------+-------------+-----------------------
  postgres  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 |

  $ psql -d <dbname>

eg.

  $ psql -d postgres

enter the `postgres=#`

  \dt # list all `table`

  Schema |    Name    | Type  |  Owner  
 --------+------------+-------+---------
  public | puppytable | table | william

exit

  \q

## SQL Command

CRUD

### Create

  CREATE TABLE useraccount (
    user_id SERIAL PRIMARY KEY,
    username char(40) UNIQUE,
    password char(32) NOT NULL,
    salt char(32) NOT NULL
  );

SERIAL : autoincrement number, like `id`


### Select

  select * from <table> where <element> = '<value>'

### [Insert](https://www.tutorialspoint.com/postgresql/postgresql_insert_query.htm)

  INSERT INTO useraccount (username, password, salt) VALUES (%s, %s, %s)", (username, password, salt));

  or

  INSERT INTO useraccount VALUES (username, password, salt);

### Delete

  Drop Table <tableName>;


## ref

- [tut](http://www.postgresqltutorial.com/postgresql-show-tables/)
