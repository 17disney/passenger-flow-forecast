import json
from tickets import predictTickets
from flows import predictFlows
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
