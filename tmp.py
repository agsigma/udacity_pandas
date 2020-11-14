import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_ENUM = {
    'january': 1,
    'february': 2,
    'march': 3,
    'april': 4,
    'may': 5,
    'june': 6,
    'july': 7,
    'august': 8,
    'september': 9,
    'october': 10,
    'november': 11,
    'december': 12,
    'all': None
}

DAY_ENUM = {
    'monday': 0, 
    'tuesday': 1,
    'wednesday': 2, 
    'thursday': 3, 
    'friday': 4,
    'saturday': 5,
    'sunday': 6,
    'all': None
}

def input_options(options):
  s = input().lower()
  while s not in options:
    s = input().lower()
  return s

# city = input_options(CITY_DATA.keys())
# month = input_options(MONTH_ENUM.keys())
# day = input_options(DAY_OPTIONS)

df = pd.read_csv('./chicago.csv')
datetime_series = pd.to_datetime(df['Start Time'])
df['Timestamp'] = datetime_series
df['Month'] = df['Timestamp'].dt.month
df['Day of week'] = df['Timestamp'].dt.dayofweek
