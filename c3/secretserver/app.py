from flask import Flask, request
from flask_restful import Resource, Api
import subprocess

app = Flask(__name__)
api = Api(app)

class Flag(Resource):
    def get(self):
        calling_ip = request.remote_addr
        return {'flag1': 'final_flag_1337'}


api.add_resource(Flag, '/')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
    #app.run(debug=True)