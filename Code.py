from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
    #top 10 cryptos
  'limit':'10',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'c27a7d7a-e9db-4834-8966-e531a4ccca53',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  #print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)



import pandas as pd

#enabling to see all the columns
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)



#Normalizing the data into more readable dataframe
dataF = pd.json_normalize(data['data'])
## adding timestamp column
dataF['timestamp'] = pd.to_datetime('now')
dataF




def api_auto_runner():
    global dataF
    #global variable, Enabling to run properly
    
    


    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
      'start':'1',
      'limit':'10',
      'convert':'USD'
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': 'c27a7d7a-e9db-4834-8966-e531a4ccca53',
    }

    session = Session()
    session.headers.update(headers)

    try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
      #print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)
    
    
    # Process and append JSON data with a current timestamp to the existing DataFrame.
    # Flatten JSON, add timestamp, and prepare for appending
    dataF2 = pd.json_normalize(data['data'])
    dataF2['Timestamp'] = pd.to_datetime('now')
    
    # Convert normalized data to a DataFrame for appending.
    dataF_append = pd.DataFrame(dataF2)
    
    # Append the new data to the existing DataFrame.
    dataF = pd.concat([dataF, dataF_append])
    
    
    #dataF = pd.json_normalize(data['data'])
    #dataF['Timestamp'] = pd.to_datetime('now')
    #dataF
    
    #automating the pull into csv file. If not the file doesnt exist create a new one
    if not os.path.isfile(r'C:\Users\Abir\Desktop\Coinmarket project\CoinPriceHistory.csv'):
        #creating new file & column headers based on the dataframe
        dataF.to_csv(r'C:\Users\Abir\Desktop\Coinmarket project\CoinPriceHistory.csv',header='column_names')
    else:
        #if api file already exists, append the data (mode='a'), not overwrite it
        dataF.to_csv(r'C:\Users\Abir\Desktop\Coinmarket project\CoinPriceHistory.csv',mode='a',header=False) 



import os
from time import time, sleep

#running the api for 2 times a day
for i in range(2):
    api_auto_runner()
    print('Completed the autorun')
    #the runner sleeps for 1 seconds before it starts again
    sleep(1)
exit()



import pandas as pd 

#reading the file & opening first 10.Changing also the number format 
pd.set_option('display.float_format', lambda x: '%.5f' % x) 
dftest=pd.read_csv(r"C:\Users\Abir\Desktop\Coinmarket project\CoinPriceHistory.csv") 
dftest




dftest2=dftest.groupby('name',sort=False)[['quote.USD.percent_change_1h','quote.USD.percent_change_24h','quote.USD.percent_change_7d']].mean()
dftest2


dftest3=dftest2.stack()
dftest3

type(dftest2)
type(dftest3)


dftest4=dftest3.to_frame(name='values')
dftest4
index = pd.Index(range(50))
dftest5 = dftest4.reset_index().rename(columns={'level_1':'data_change'})
dftest5



#new,updated csv file 
csv_file_path = r'C:\Users\Abir\Desktop\Coinmarket project\CoinPriceHistoryNEW.csv'
dftest5.to_csv(csv_file_path, index=False)



import seaborn as sns
import matplotlib.pyplot as plt
sns.catplot(x='data_change',y='values',hue='name',data=dftest5,kind='point')



import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
cat_plot = sns.catplot(x='data_change', y='values', hue='name', data=dftest5, kind='point', palette='muted')

plt.xlabel('Percent Change Timeframe')
plt.ylabel('Average Percent Change')
plt.title('Cryptocurrency Performance Over Time')


plt.legend(title='Cryptocurrency', fontsize='10')
plt.tight_layout()
plt.show()
