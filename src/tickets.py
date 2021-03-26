import pathlib
import pandas as pd
import seaborn as sns
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

model = tf.keras.models.load_model('model/tickets.h5')

def predictTickets(data):
  # 数据清洗
  df = pd.json_normalize(data)
  dataset = df
  dataset['memberDay'] = dataset['memberDay']*1.0
  dataset['isWeekend'] = dataset['isWeekend']*1.0
  dataset['day'] = dataset['day']*1.0

  predictions = model.predict(dataset).flatten()

  return predictions