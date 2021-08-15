from flask import Flask,request
from flask.wrappers import Request, Response
from flask_restful import Api,Resource, reqparse
app = Flask(__name__)
api= Api(app)

cpu_put_args = reqparse.RequestParser()
cpu_put_args.add_argument("cpuUsage",type=str,help="The Cpu Usage")
cpuu = {}
class home(Resource):
    def get(self):
        return "Test Ramy"
class cpu(Resource):
    def get (self,cpu_id):
        return cpu[cpu_id]
    def put(self,cpu_id):
        args=cpu_put_args.parse_args()
        cpuu[cpu_id]=args
        return cpuu[cpu_id],201


api.add_resource(home,"/")
api.add_resource(cpu,"/cpu/<int:cpu_id>")

#api.add_resource(cpu,"/cpu")
if __name__=="__main__":
    app.run(debug=True)
