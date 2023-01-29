from flask import Flask,request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return '<h1>Hello, 世界!</h1>'

@app.route('/msg',methods=['POST'])
def msg():
    data = request.get_json()
    print(data)
    return 'data has been received'


if __name__ == '__main__':
   app.run(host='192.168.43.117',port=5000)
