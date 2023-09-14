from holiday import holidays
import pandas as pd
from prophet import Prophet

# badweathers = pd.DataFrame({
#   'holiday': 'badweathers',
#   'ds': pd.to_datetime(dataset.query('pptTotal>15')['date']),
#   'lower_window': -1,
#   'upper_window': 0,
# })
# dataset
# df = dataset[['date', 'max']]

def generByPark(park, dataset):
  # park = 'flhs'
  # df = dataset.query('name=shdr')
  # df.dropna(how='any')
  df = dataset.query("park=='" + park  + "'")
  df = dataset.query('mark>0')
  df['max'] = df['mark'] # df['max'].max() * 10 # * 35
  data = pd.DataFrame()
  data['ds'] = df['date']
  data['y'] = df['max']

  df.head()


  # df = dataset[['date', 'max']]
  # cf = dataset[['date', 'pptTotal']]
  # df.loc['2017Q1'].plot(title='2017 Flow')
  # cf.loc['2017'].plot(title='2017 Flow')
  # df.loc['2018'].plot(title='2018 Flow')
  # cf.loc['2018'].plot(title='2018 Flow')
  # df.loc['2019'].plot(title='2019 Flow')
  # df
  # ydata = df.resample('Y').mean()
  # ydata['date'] = ydata['date']
  # ydata.plot(title='Shanghai Disneyland Daily Mean Flow (by year)', ylabel='Mean Flow', xlabel='Year', legend=None)

  # df.plot(title='Shanghai Disneyland Daily Flow', ylabel='Flow', xlabel='Date', legend=None)

  data = pd.DataFrame()
  data['ds'] = df['date']
  data['y'] = df['max']


  # allholidays = [] # holidays() 
  m = Prophet(
    yearly_seasonality = True,
    weekly_seasonality = True,
    daily_seasonality = True,
    seasonality_prior_scale = 20,
    holidays_prior_scale = 20,
    interval_width = 0.9
  )

  if (park == 'shdr' or park == 'usb'):
    m.add_country_holidays(country_name='CN')
  elif (park == 'hkdl'):
    m.add_country_holidays(country_name='HK')
  elif (park == 'tkydl' or park == 'tkys' or park == 'usj'):
    m.add_country_holidays(country_name='JP')
  elif (park == 'pardl' or park == 'pardsl'):
    m.add_country_holidays(country_name='FR')
  else:
    m.add_country_holidays(country_name='US')

  m.fit(data)
  future = m.make_future_dataframe(periods=365)
  forecast = m.predict(future)
  forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

  fig1 = m.plot(forecast)

  forecast.to_csv('forecast-flow/' + park + '.csv')