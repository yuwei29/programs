from flask import Flask,request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, 世界!'

@app.route('/sum')
def sumN():
    num = int(request.args.get('num'))
    sum=0
    for i in range(1,num+1):
        sum+=i
    return str(sum)

if __name__ == '__main__':
   app.run()