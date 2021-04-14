''' webhook_api takes in a URI and makes a request to secretserver '''
from flask import Flask, request
from flask_restful import reqparse, Resource, Api
from base64 import urlsafe_b64encode as b64e
import subprocess
import requests

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('icon_path')
# for users
users = {}

class UserIcon(Resource):
    def get(self, user_id):
        if user_id in users:
            if 'icon_path' in users[user_id]:
                return {'user_id': user_id, 'icon_path': users[user_id]['icon_path']}, 200
            else:
                return {'user_id': user_id, 'icon_path': ''}, 200
        else:
            return {'error': 'user not found'}, 404

    def put(self, user_id):
        args = parser.parse_args()
        if 'icon_path' not in args or not args['icon_path']:
            return {'error': 'missing icon_path'}, 400
        if user_id not in users:
            users[user_id] = {'icon_path': args['icon_path']}
        else:
            users[user_id]['icon_path'] = args['icon_path']
        # make a request to giphy
        url = f"http://livinginsyn.com{args['icon_path']}"
        r = requests.get(url)
        if r.status_code != 200:
            return {'error': f'Error calling url.\nStatus Code: {r.status_code}\nContent: {str(r.conent)}'}, 500
        c = b64e(r.content).decode('utf-8')
        return {'user_id': user_id, 'image': c}, 200

api.add_resource(UserIcon, '/icon/<string:user_id>')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
    #app.run(debug=True)