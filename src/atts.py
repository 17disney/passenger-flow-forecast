import pandas as pd
import tensorflow as tf

def predictAtts(id, data):
  df = pd.json_normalize(data)
  dataset = df
  model = tf.keras.models.load_model('./model/' + id + '.h5')

  predictions = model.predict(dataset).flatten()
  return predictions
