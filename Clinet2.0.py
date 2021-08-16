from flask import Flask,request
from flask.wrappers import Request, Response
from flask_restful import Api,Resource, reqparse
import requests
import psutil
app = Flask(__name__)
api= Api(app)
#print('RAM memory % used:', psutil.virtual_memory()[2])
#cpu_put_args = reqparse.RequestParser()
#cpu_put_args.add_argument("CPU time",type=int,help="The Cpu Usage")

cpuu = {}
ramm = {}
class cpu(Resource):
    def get (self,cpu_id):
        cpuu[cpu_id]={"cpuUsage":psutil.cpu_percent(4)}
        return cpuu[cpu_id],200
    
class ram(Resource):
    def get(self,ram_id):
        ramm[ram_id]={"Current Ram Usage":psutil.virtual_memory()[2]}

        return ramm[ram_id],200


api.add_resource(cpu,"/cpu/<int:cpu_id>")
api.add_resource(ram,"/ram/<int:ram_id>")
#api.add_resource(cpu,"/cpu")
if __name__=="__main__":
    app.run(debug=True)
  