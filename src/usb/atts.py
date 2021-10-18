import pandas as pd
import requests
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

def fetchData():
  res = requests.post("http://localhost:7001/api/etl/usb")
  return res.json()

df = fetchData()
df = pd.json_normalize(df)

def generAttModel(id):
  dataset = df[[id, 'attsMark', 'isMon', 'isFri', 'isSaturday', 'isSunday', 'isHoliday']]

  # 拆分训练数据集和测试数据集
  train_dataset = dataset.sample(frac=0.8,random_state=0)
  dataset.drop(train_dataset.index)

  train_stats = train_dataset.describe()
  train_stats.pop("attsMark")
  train_stats = train_stats.transpose()

  # 从标签中分离特征
  train_labels = train_dataset.pop(id)
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

  EPOCHS = 500

  history = model.fit(
    normed_train_data, train_labels,
    epochs=EPOCHS, validation_split = 0.2, verbose=0)

  hist = pd.DataFrame(history.history)
  hist['epoch'] = history.epoch
  hist.tail()

  model = build_model()
  history = model.fit(normed_train_data, train_labels, epochs=EPOCHS, validation_split = 0.2, verbose=0)

  model.save('../model/' + id + '.h5')

list = [
  "5fa22624dcb5e53c6c72ab42",
  "5fa247615ba7f1491f6289a2",
  "5f913de126509774c642cf36",
  "5f912fd8d72a471ef6359d02",
  "5f91438e16d92d317523b6a4",
  "6121b15723ccd253665b6822",
  "60f97e7286449732e736681c",
  "5fa22dab40a74131c80b8a72",
  "60f976da05482c2ea6737a9c",
  "5f8812ec14ae8a2d80450794",
  "5fa23cdcbbdbd416ae43dc05",
  "611e57d62f02d506f768dec8",
  "5f914afc26509774c642cf42",
  "60f97dfceb33e120fe66fc3e",
  "5f9161f64b89d447253b02c5",
  "611f0913e291ec2b16214a88",
  "5f91526a68ff66780876eaaf",
]

for id in list:
  generAttModel(id)