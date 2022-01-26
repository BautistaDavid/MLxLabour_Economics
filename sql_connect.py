# import os
# import pandas as pd
# import psycopg2

# datos=pd.read_csv("datos.csv")
# datos

# conn = psycopg2.connect("dbname=modelo_web user=postgres password=america2015 port=5432")
# cur = conn.cursor()

# cur.execute('SELECT * FROM try;')

# cur.execute("CREATE TABLE datos_elca (empleado int);")
# cur.execute("\dt")

# all = cur.fetchall()
# all

datos=pd.read_csv("datos.csv")
for i in datos.index:
    print(datos["edad"])



import pandas as pd 
import psycopg2
import config


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE emissions (
            column1 bit NOT NULL,
            column2 bit NOT NULL,
            column3 bit NOT NULL
        )
        """,
        )
        
    conn = None
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect("dbname=modelo_web user=postgres password=america2015 port=5432")
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()



if __name__ == '__main__':
    create_tables()





import psycopg2
import pandas as pd
# Here you want to change your database, username & password according to your own values
param_dic = {
    "host"      : "localhost",
    "database"  : "modelo_web",
    "user"      : "postgres",
    "password"  : "america2015"
}
def connect(params_dic):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error) 
    return conn
def single_insert(conn, insert_req):
    """ Execute a single INSERT request """
    cursor = conn.cursor()
    try:
        cursor.execute(insert_req)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    cursor.close()
# Connecting to the database
conn = connect(param_dic)
# Inserting each row
for i in datos.index:
    query = """
    INSERT into emissions(column1, column2, column3) values('%s',%s,%s);
    """ % (datos['edad'], datos['sexo'], datos['etnia'])
    single_insert(conn, query)
# Close the connection
conn.close()

datos.columns