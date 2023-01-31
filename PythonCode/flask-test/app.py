from flask import Flask,request
from flask_cors import CORS
from service import Service
app = Flask(__name__)
CORS(app)

s1 = Service()
@app.route('/')
def hello_world():
    return 'Hello, 世界!'

@app.route('/init')
def init():
    return {'p1':s1.中,'p2':s1.a}

@app.route('/change',methods=['POST'])
def change():
    data = request.get_json()
    s1.changeCn(data['content'])
    return s1.中

if __name__ == '__main__':
   app.run()