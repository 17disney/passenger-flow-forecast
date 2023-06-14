import json
import time
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt


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
  return df


def getData():
  data = []
  df = readFile('attractions')
  dailyData = pd.json_normalize(readFile('dailies'))

  for item in df:
    if item.get('startTime'):
      startTime = item['startTime']
      startTimex = time.mktime(time.strptime(item['date'] + ' ' + item['startTime'], '%Y-%m-%d %H:%M:%S'))
      endTimex = time.mktime(time.strptime(item['date'] + ' ' + item['endTime'], '%Y-%m-%d %H:%M:%S'))
      countTimex = endTimex - startTimex
      date = item['date']

      dailyItem = dailyData.query("date=='" + date + "'")
      dailyItem = json.loads(dailyItem.to_json(orient="records"))
      if dailyItem[0]:
        parkValue = dailyItem[0]['value']
        for row in item['rows']:
          timex = (row[0] - startTimex)/countTimex
          data.append({"timex": timex, "value": row[1], "avg": parkValue, "date": item['date'], "name": item["name"]})
          # data.append({"timex": timex, "value": row[1], "avg": item['value'], "date": item['date'], "name": item["name"], "parkValue": parkValue})

  dataset = pd.json_normalize(data)
  dataset = dataset[['timex', 'value', 'avg', 'name']]
  dataset['avg'] = dataset['avg'] / 875
  dataset['value'] = dataset['value'] / 150

  return dataset[1:]

def generParkData(dataset):
  print(dataset.count())
  plot_cols = ['value']
  plot_features = dataset[plot_cols]
  plot_features.index = dataset['timex']
  _ = plot_features.plot()

  dataset = dataset[['timex', 'value', 'max']]
  dataset = dataset[1:]

  print(dataset.head())
  
  # 拆分训练数据集和测试数据集
  train_dataset = dataset.sample(frac=0.8,random_state=0)
  test_dataset = dataset.drop(train_dataset.index)
  dataset.drop(train_dataset.index)

  train_stats = train_dataset.describe()
  train_stats.pop("value")
  train_stats = train_stats.transpose()
  # train_stats

  # 从标签中分离特征
  train_labels = train_dataset.pop('value')
  test_labels = test_dataset.pop('value')

  normed_train_data = train_dataset
  normed_test_data = test_dataset

  return [normed_train_data, normed_test_data, train_dataset, train_labels, test_labels]


def generData(allData, name):
  dataset = allData.query("(name=='" + name + "')")
  dataset = dataset.query("(timex >= 0) & (timex <= 1)")
  dataset = dataset.query("value > 0")
  dataset = dataset.query("(avg > 0) & (avg < 1)")
  # dataset
  print(dataset.count())
  plot_cols = ['value']
  plot_features = dataset[plot_cols]
  plot_features.index = dataset['timex']
  _ = plot_features.plot()

  dataset = dataset[['timex', 'value', 'avg']]
  dataset = dataset[1:]

  print(dataset.head())
  
  # 拆分训练数据集和测试数据集
  train_dataset = dataset.sample(frac=0.8,random_state=0)
  test_dataset = dataset.drop(train_dataset.index)
  dataset.drop(train_dataset.index)

  train_stats = train_dataset.describe()
  train_stats.pop("value")
  train_stats = train_stats.transpose()
  # train_stats

  # 从标签中分离特征
  train_labels = train_dataset.pop('value')
  test_labels = test_dataset.pop('value')

  normed_train_data = train_dataset
  normed_test_data = test_dataset

  return [normed_train_data, normed_test_data, train_dataset, train_labels, test_labels]


def buildModel(train_dataset):
  model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=[len(train_dataset.keys())]),
    layers.Dense(64, activation='relu'),
    layers.Dense(1)
  ])

  optimizer = tf.keras.optimizers.RMSprop(0.001)

  model.compile(loss='mse', optimizer=optimizer, metrics=['mae', 'mse'])
  return model


class PrintDot(keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs):
    if epoch % 100 == 0: print('')
    print('.', end='')


def plot_history(history):
  hist = pd.DataFrame(history.history)
  hist['epoch'] = history.epoch

  plt.figure()
  plt.xlabel('Epoch')
  plt.ylabel('Mean Abs Error [Total]')
  plt.plot(hist['epoch'], hist['mae'],
           label='Train Error')
  plt.plot(hist['epoch'], hist['val_mae'],
           label = 'Val Error')
  plt.ylim([0,0.4])
  plt.legend()

  plt.figure()
  plt.xlabel('Epoch')
  plt.ylabel('Mean Square Error [$Total^2$]')
  plt.plot(hist['epoch'], hist['mse'],
           label='Train Error')
  plt.plot(hist['epoch'], hist['val_mse'],
           label = 'Val Error')
  plt.ylim([0,0.2])
  plt.legend()
  plt.show()



# hist = pd.DataFrame(history.history)
# hist['epoch'] = history.epoch
# hist.tail()