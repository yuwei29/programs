from flask import Flask,request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, 世界!'

@app.route('/ai')
def aiMove():
    return [1,2,4,2] //

@app.route('/playerOnline',methods=['POST'])
def getPlayerInput():
    data = request.get_json()
    print(data)
    return 'OK'

if __name__ == '__main__':
   app.run()