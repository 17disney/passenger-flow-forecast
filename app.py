import json
from tickets import predictTickets
# from tickets import 
from flows import predictFlows, predictUsbFlows
from atts import predictAtts
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/predictions/tickets', methods=['POST'])
def predictionsTickets():
  print(request.json)
  data = request.json

  predictions = predictTickets(data)
  predictions = predictions.tolist()
  return json.dumps(predictions, ensure_ascii=False)

@app.route('/predictions/flows', methods=['POST'])
def predictionsFlows():
  print(request.json)
  data = request.json

  predictions = predictFlows(data)
  predictions = predictions.tolist()
  return json.dumps(predictions, ensure_ascii=False)

@app.route('/predictions/usb/flows', methods=['POST'])
def predictionsUsbFlows():
  print(request.json)
  data = request.json

  predictions = predictUsbFlows(data)
  predictions = predictions.tolist()
  return json.dumps(predictions, ensure_ascii=False)

@app.route('/predictions/usb/atts', methods=['POST'])
def predictionsUsbFlows():
  print(request.json)
  data = request.json.id
  data = request.json.data

  predictions = predictAtts(id, data)
  predictions = predictions.tolist()
  return json.dumps(predictions, ensure_ascii=False)
