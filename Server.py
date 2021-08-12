from flask import Flask,request
from flask.wrappers import Request
from flask_restful import Api,Resource, reqparse
app = Flask(__name__)
api= Api(app)

cpu_put_args = reqparse.RequestParser()
cpu_put_args.add_argument("cpuUsage",type=str,help="The Cpu Usage",)
class cpu(Resource):
    def put(self,cpu_use):
        return 






@app.route('/', methods=['GET'])
def home():
    return '''<h1>test if this api works or not</h1>
<p>Testing</p>'''

api.add_resource(cpu,"/cpu")
if __name__=="__main__":
    app.run(debug=True)
