import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import time
import datetime
import pandas as pd
import numpy as np

#function to fetch data from API
def getData(tickers):
        API_Endpoint=[]
        period1 = int(time.mktime(datetime.datetime(2020, 1, 1, 12, 00).timetuple()))
        period2 = int(time.mktime(datetime.datetime(2023, 7, 20, 12, 00).timetuple()))
        interval='1d'
        for ticker in tickers:
            API_Endpoint.append(f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true')
        return API_Endpoint
    
#function to download the data as CSV from the API
def downloadData(endPoints,tickers):      
            dataFrame=[]
            df_FNGU=pd.read_csv(endPoints[0])            
            df_FNGU= df_FNGU.set_index(pd.DatetimeIndex(df_FNGU['Date'].values))
            dataFrame.append(df_FNGU)
            df_FNGU.to_csv(f"C:/Users/megha/OneDrive/Desktop/TradeX/Model/FNGU.csv")
            df_FNGD=pd.read_csv(endPoints[1])
            df_FNGD= df_FNGD.set_index(pd.DatetimeIndex(df_FNGD['Date'].values))
            dataFrame.append(df_FNGD)
            df_FNGD.to_csv(f"C:/Users/megha/OneDrive/Desktop/TradeX/Model/FNGD.csv")
            return dataFrame
    
#Moving Average Cross-Over Stratergy
    
# calculate simple moving average
def SMA(data, framePeriod=30, column='Close'):
         return data[column].rolling(window=framePeriod).mean()    
    
#generate buy and sell signals
def stockPurchase(data):
         data['Signal']=np.where(data['SMA20']>data['SMA50'],1,0)
         data['Position']= data['Signal'].diff()    
         data['Buy']=np.where(data['Position']==1,data['Close'],np.NAN)
         data['Sell']=np.where(data['Position']==-1,data['Close'],np.NAN)
         return data
    
#Bollinger Band + RSI Stratergy

#generate  bands
def bollingerBands(data, window_Size):
         rolling_mean=data['Close'].rolling(window=window_Size).mean() #Simple Moving Average
         rolling_std= data['Close'].rolling(window=window_Size).std()
         data['UpperBand']=rolling_mean+(2*rolling_std)
         data['LowerBand']=rolling_mean-(2*rolling_std)
         return data
    
#determine RSI
def RSI(data, window_Size):
         delta=data['Close'].diff()
         gain=delta.where(delta>0,0)
         loss=delta.where(delta<0,0)
         avg_gain= gain.rolling(window_Size).mean()
         avg_loss= loss.rolling(window_Size).mean()
         RS=avg_gain/avg_loss
         RSI = 100 -(100/(1+RS))
         data['RSI']=RSI
         data['Overbought']= 70
         data['Oversold']= 30
         return data
    

#function to generate buy or sell signal using Bollinger Band and RSI
#Buy when close price goes below lower band and RSI is less than 30
#Sell when close price goes above upper band and RSI is greater than 70

def stratergy(data):
         position=0
         buy_price=[]
         sell_price=[]
         for i in range(len(data)):
              if data['Close'][i] < data['LowerBand'][i] and data['RSI'][i] < data['Oversold'][i] and position==0:
                   position=1
                   buy_price.append(data['Close'][i])
                   sell_price.append(np.nan)

              elif data['Close'][i] > data['UpperBand'][i] and data['RSI'][i] > data['Overbought'][i] and position==1:
                   position=0
                   sell_price.append(data['Close'][i])
                   buy_price.append(np.nan)
              else:
                   buy_price.append(np.nan)
                   sell_price.append(np.nan)

         return (buy_price,sell_price)         
      







