import configparser
import psycopg2
config = configparser.ConfigParser()
config.read(r"C:\Users\OmarQ\Desktop\PROJECT\DataBase\config.ini")
dbparam= config["postgressql"]
user =dbparam["user"] 
password=dbparam["password"]
host=dbparam["host"]
port=int(dbparam["port"])
dbase=dbparam["db"]


def connect():
        connection= psycopg2.connect(user=user,
                                    password=password,
                                    host=host,
                                    port=port,
                                    database=dbase)
        return connection


def insert(val,id,database):     
        insert=f'''INSERT INTO {database} VALUES ({val},{id})
        '''
        connection = connect()
        cursor=connection.cursor()
        cursor.execute(insert)
        connection.commit()
        return




