from flask import Flask,request
from flask_cors import CORS
import service.hci_service as hs
app = Flask(__name__)
CORS(app)

s1 = hs.HCIService()

@app.route('/')
def hello_world():
    return 'Hello, 世界!'

@app.route('/start')
def start():
    s1.__init__()
    return 'OK'

@app.route('/ai')
def aiMove():
    return s1.black_play()

@app.route('/playerOnline',methods=['POST'])
def getPlayerInput():
    data = request.get_json()
    act = [data['x1'],data['y1'],data['x2'],data['y2']]
    s1.red_play(act)
    return 'OK'

if __name__ == '__main__':
   app.run()