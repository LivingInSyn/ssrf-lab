from flask import Flask, request
from flask_restful import Resource, Api
import os
import base64

app = Flask(__name__)
api = Api(app)

class Flag(Resource):
    def get(self):
        calling_ip = request.remote_addr
        return {'flag1': 'final_flag_1337'}

class List(Resource):
    def get(self):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'icons')
        ifiles = os.listdir(filename)
        append_str = "/icons-png/"
        ifiles = pre_res = [append_str + sub for sub in ifiles]
        return {'icons': ifiles}, 200

class Icon(Resource):
    def get(self,icon_id):
        icon_id = icon_id.replace("..",'')
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'icons', icon_id)
        try:
            with open(filename, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            return {'image': encoded_string}, 200
        except Exception as e:
            return {}, 500



api.add_resource(Flag, '/')
api.add_resource(List, '/list-icons')
api.add_resource(Icon, '/icons-png/<string:icon_id>')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    #app.run(debug=True)