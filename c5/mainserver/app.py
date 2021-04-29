''' webhook_api takes in a URI and makes a request to secretserver '''
from flask import Flask, request, render_template, make_response
from flask_restful import reqparse, Resource, Api
from base64 import urlsafe_b64encode as b64e
import subprocess
import requests
import json
from urllib import parse
import socket
import ipaddress

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('url')
#
SECRET_URL = "172.16.0.4"
SECRET_URL = "localhost:8080"
# safe domain list
SAFE_DOMAINS = []

class UrlReturnJson(Resource):
    def post(self):
        args = parser.parse_args()
        # make sure that url is there
        if 'url' not in args or not args['url']:
            return {'status': 'error', 'message': 'missing url'}, 400
        # parse the url
        try:
            parsed_url = parse.urlsplit(args['url'])
            if parsed_url.scheme not in ['http','https']:
                return {'status': 'error', 'message': 'Bad protocol'}, 400
        except Exception as e:
            return {'status': 'error', 'message': 'that url gave me heartburn'}, 500
        # do an nslookup on the domain if not cached
        try:
            if parsed_url.netloc not in SAFE_DOMAINS:
                ext_ip = socket.gethostbyname(parsed_url.netloc)
                ext_ip = ipaddress.ip_address(ext_ip)
                if ext_ip.is_private: 
                    return {'error': 'SSRF IS BAD!'}, 401
                else:
                    SAFE_DOMAINS.append(parsed_url.netloc)
        except:
            return {'status': 'error', 'message': 'that domain gave me gastrointestinal distress.'}, 500
        # do the request
        try:
            r = requests.get(args['url'])
            if r.status_code != 200:
                return {'error': f'Error calling url.\nStatus Code: {r.status_code}\nContent: {str(r.content)}'}, 500
            try:
                content = json.loads(r.content)
                if content:
                    return {'status': 'success', 'message': 'That url returns JSON', 'content': content}, 200
                else:
                    return {'status': 'failure', 'message': 'That url doesnt return JSON'}, 200
            except:
                return {'status': 'failure', 'message': 'That url doesnt return JSON'}, 200
        except:
            return {'error': 'something went terribly wrong doing that there request'}, 500

class Index(Resource):
    def __init__(self):
        pass
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('apidoc.html'),200,headers)

api.add_resource(UrlReturnJson, '/json')
api.add_resource(Index, '/')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
    #app.run(debug=True, port=8080)