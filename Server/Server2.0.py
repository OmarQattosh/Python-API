# Importing stuff
from sched import scheduler
import schedule
import time
import psutil
from flask.wrappers import Response
import requests
import psycopg2 
from psycopg2 import Error
import datetime
import sys
sys.path.insert(1,r'C:\Users\OmarQ\Desktop\PROJECT')
import connection as con
import logformat as lg 
lg.formatlog('desktop/PROJECT/Server/log.log')
lg.logwarn()

connection= con.connect()
cursor= connection.cursor()

Base="http://127.0.0.1:5000/"
global cpu_id,ram_id
cpu_id=1
ram_id=1
def insertFunction(val,id,database):
    insert=f'''INSERT INTO {database} VALUES ({val},{id})
    '''
    cursor.execute(insert)
    connection.commit()
    return
def getCpu(cpu_id):
    response= requests.post(Base+f"cpu/{cpu_id}")
    if response.status_code >= 400:
        lg.failRet()
    cpu_id+=1 
    print(response.json())
    insertFunction(response.json()['cpuUsage'],cpu_id,"cpu")
    lg.succRet()
    now = datetime.datetime.now()
    print(now.minute,now.second)
    return
def getRam(ram_id):
    response=requests.post(Base+f"ram/{ram_id}")
    if response.status_code == 404:
        lg.failRet()
    ram_id+=1
    print(response.json())
    insertFunction(response.json()['Current_Ram_Usage'],ram_id,"ram")
    lg.succRet()
    now = datetime.datetime.now()
    print(now.minute,now.second)
    return
schedule.every(16).seconds.do(getCpu,cpu_id)    
schedule.every(30).seconds.do(getRam,ram_id)
while True:
    schedule.run_pending()















""" try :
    connection= psycopg2.connect(user="postgres",
                                password="lama159852357",
                                host="127.0.0.1",
                                port="5432",
                                database="test.db")
    cursor= connection.cursor()
    create_table_query='''ALTER TABLE  cpu 
    ADD cpu_id REAL;
    '''
    cursor.execute(create_table_query)
    connection.commit()
except(Exception, Error) as error:
    print("error while connecting", error)
finally:
    if connection:
        cursor.close()
        connection.close()
 """

""" 

""" 

#response= requests.get(Base+"cpu/1")
#print(response.json())  
# Getting % usage of virtual_memory ( 3rd field)
#print('RAM memory % used:', psutil.virtual_memory()[2])

