from flask import Flask,request
from flask.wrappers import Request, Response
from flask_restful import Api,Resource, reqparse
import requests
import sys
sys.path.insert(1,r'C:\Users\OmarQ\Desktop\PROJECT\Server')
import psutil
import logformat as lg
lg.formatlog('Clinet/log.log')
app = Flask(__name__)
api= Api(app)

cpuu = {}
ramm = {}
class cpu(Resource):
    def post (self,cpu_id):
        cpuu[cpu_id]={"cpuUsage":psutil.cpu_percent(4)}
        return cpuu[cpu_id],200
    
class ram(Resource):
    def post(self,ram_id):
        ramm[ram_id]={"Current_Ram_Usage":psutil.virtual_memory()[2]}
        return ramm[ram_id],200


api.add_resource(cpu,"/cpu/<int:cpu_id>")
api.add_resource(ram,"/ram/<int:ram_id>")
#api.add_resource(cpu,"/cpu")
if __name__=="__main__":
    app.run(debug=True)
  