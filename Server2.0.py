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


ramy= input("press 1 to get the CPU USAGE  and 2 for ram ")
Base="http://127.0.0.1:5000/"
def getCpu():
    response= requests.get(Base+"cpu/1")
    print(response.json())
    now = datetime.datetime.now()
    print(now.minute,now.second)
    return
def getRam():
    response=requests.get(Base+"ram/1")
    print(response.json())
    now = datetime.datetime.now()
    print(now.minute,now.second)
    return
schedule.every(16).seconds.do(getCpu)    
schedule.every(30).seconds.do(getRam)
print(ramy)
while True:
    if ramy=="1":        
       
        schedule.run_pending()
        time.sleep(1)
    elif ramy=="2":
        print("hi")
        
    else:
        print("пошел на хуй")














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

