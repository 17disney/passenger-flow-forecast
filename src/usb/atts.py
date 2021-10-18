import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import requests
import tensorflow as tf
import time
from datetime import datetime
from tensorflow import keras
from tensorflow.keras import layers

def fetchData():
  res = requests.post("http://localhost:7001/api/etl/usb")
  return res.json()

df = fetchData()
df = pd.json_normalize(df)

def generAttModel():
  dataset = df[['5fa22624dcb5e53c6c72ab42', 'attsMark', 'isMon', 'isFri', 'isSaturday', 'isSunday', 'isHoliday']]

  # 拆分训练数据集和测试数据集
  train_dataset = dataset.sample(frac=0.8,random_state=0)
  dataset.drop(train_dataset.index)

  train_stats = train_dataset.describe()
  train_stats.pop("attsMark")
  train_stats = train_stats.transpose()

  # 从标签中分离特征
  train_labels = train_dataset.pop('5fa22624dcb5e53c6c72ab42')
  normed_train_data = train_dataset

  def build_model():
    model = keras.Sequential([
      layers.Dense(64, activation='relu', input_shape=[len(train_dataset.keys())]),
      layers.Dense(64, activation='relu'),
      layers.Dense(1)
    ])

    optimizer = tf.keras.optimizers.RMSprop(0.001)

    model.compile(loss='mse', optimizer=optimizer, metrics=['mae', 'mse'])
    return model
    
  model = build_model()
  model.summary()

  example_batch = normed_train_data[:3]
  example_result = model.predict(example_batch)

  EPOCHS = 500

  history = model.fit(
    normed_train_data, train_labels,
    epochs=EPOCHS, validation_split = 0.2, verbose=0)

  hist = pd.DataFrame(history.history)
  hist['epoch'] = history.epoch
  hist.tail()

  model = build_model()

  # patience 值用来检查改进 epochs 的数量
  early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=10)
  history = model.fit(normed_train_data, train_labels, epochs=EPOCHS, validation_split = 0.2, verbose=0)

  model.save('../model/usb_5fa22624dcb5e53c6c72ab42.h5')

generAttModel()