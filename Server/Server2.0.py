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
import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'DataBase'))
import connection as con
import logformat as lg 
lg.formatlog('desktop/PROJECT/Server/log.log')


connection= con.connect()
cursor= connection.cursor()

BASE="http://127.0.0.1:5000/"
global cpu_id,ram_id
cpu_id=1
ram_id=1

class Server():
    def __init__(self) :
        
        pass 
        
    def getCpu(cpu_id):
        response= requests.post(BASE+f"/cpu/")
        if response.status_code >= 400:
            lg.failRet()
        cpu_id+=1 
        print(response.json())
        con.insert(response.json()['cpuUsage'],cpu_id,"cpu")
        lg.succRet()
        now = datetime.datetime.now()
        print(now.minute,now.second)
        return
    def getRam(ram_id):
        response=requests.post(BASE+f"ram/")
        if response.status_code == 404:
            lg.failRet()
        ram_id+=1
        print(response.json())
        con.insert(response.json()['Current_Ram_Usage'],ram_id,"ram")
        lg.succRet()
        now = datetime.datetime.now()
        print(now.minute,now.second)
        return
    def sch():
        schedule.every(16).seconds.do(Server.getCpu,cpu_id)    
        schedule.every(30).seconds.do(Server.getRam,ram_id)
        while True:
            schedule.run_pending()


if __name__=="__main__":
    Server.sch()
    
  












