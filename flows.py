import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

model = tf.keras.models.load_model('model/flows.h5')

def predictFlows(data):
  # 数据清洗
  df = pd.json_normalize(data)
  dataset = df
  # dataset['memberDay'] = dataset['memberDay']*1.0
  # dataset['isWeekend'] = dataset['isWeekend']*1.0
  # dataset['day'] = dataset['day']*1.0

  predictions = model.predict(dataset).flatten()

  return predictions