from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'My internal (ie: secured) Flask service!\nOnly accessible from 10.0.0.0/8!\nFlag: 6094266611falcon'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
