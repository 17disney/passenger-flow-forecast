import json
import time
import pandas as pd

def readFile(name):
  file_object = open("../data/" + name + '.json', 'r')
  df = []
  try:
    while True:
      line = file_object.readline()
      if line:
        df.append(json.loads(line))
      else:
        break
  finally:
    file_object.close()

  # for item in df:
  #   pptTotal = 0
  #   for wea in item['weathers']['pptHours']:
  #     pptTotal += wea[1]
  #   item['pptTotal'] = pptTotal

  df = pd.json_normalize(df)
  df['dateIndex'] = pd.to_datetime(df['date'])
  df = df.set_index('dateIndex', drop=True)
  
  return df

