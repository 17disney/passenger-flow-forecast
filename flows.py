import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

model = tf.keras.models.load_model('model/flows.h5')
usbModel = tf.keras.models.load_model('model/usb_flows.h5')
shdrModel = tf.keras.models.load_model('model/shdr_flows.h5')
attractionModel = tf.keras.models.load_model('model/attraction.h5')

def predictFlows(data):
  df = pd.json_normalize(data)
  dataset = df
  dataset['memberDay'] = dataset['memberDay']*10000
  # dataset['isWeekend'] = dataset['isWeekend']*1.0
  # dataset['day'] = dataset['day']*1.0

  predictions = model.predict(dataset).flatten()

  return predictions

def predictUsbFlows(data):
  df = pd.json_normalize(data)
  dataset = df
  predictions = usbModel.predict(dataset).flatten()

  return predictions

def predictShdrFlows(data):
  df = pd.json_normalize(data)
  dataset = df
  predictions = shdrModel.predict(dataset).flatten()

  return predictions

def predictAttraction(data):
  df = pd.json_normalize(data)
  dataset = df
  predictions = attractionModel.predict(dataset).flatten()

  return predictions