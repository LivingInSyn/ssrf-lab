from flask import Flask, request
from flask_restful import Resource, Api
import subprocess

app = Flask(__name__)
api = Api(app)
# for TODOs
todos = {}

class Flag(Resource):
    def get(self):
        calling_ip = request.remote_addr
        if calling_ip == "127.0.0.1":
            return {'flag1': 'G4sZkDjp3iI'}
        else:
            return {}, 401


api.add_resource(Flag, '/flag')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
    #app.run(debug=True)