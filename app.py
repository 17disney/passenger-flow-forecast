import json
from tickets import predictTickets
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
