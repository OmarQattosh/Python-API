from flask import Flask,request, jsonify
from flask.wrappers import Request, Response
from flask_restful import Api,Resource, reqparse
import requests
import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'Server'))

import psutil
import logformat as lg
lg.formatlog('Clinet/log.log')
app = Flask(__name__)
api= Api(app)

@app.route("/")
def home():
    return "HomePage"
@app.route("/cpu/",methods=['GET', 'POST'])
def cpu():
    if request.method == "GET":
        return {"cpuUsage":psutil.cpu_percent(4)}
    elif request.method =="POST":
        return jsonify({"cpuUsage":psutil.cpu_percent(4)})   
    return"hi"
@app.route("/ram/",methods=['GET','POST'])
def ram():
    if request.method == "GET":
        return {"Current_Ram_Usage":psutil.virtual_memory()[2]}
    elif request.method =="POST":
        return jsonify({"Current_Ram_Usage":psutil.virtual_memory()[2]})   
    return lg.loger()
    

if __name__=="__main__":
  
    app.run(debug=True)
 
 
 
 
 
