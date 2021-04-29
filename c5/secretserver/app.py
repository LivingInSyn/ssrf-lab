from flask import Flask, request
from flask_restful import Resource, Api
import os
import base64

app = Flask(__name__)
api = Api(app)

class Flag(Resource):
    def get(self):
        calling_ip = request.remote_addr
        return {'flag1': 'c5flag_jeremy_is_awesome'}



api.add_resource(Flag, '/')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
    #app.run(debug=True)