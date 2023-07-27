import View.StockView as StockView
import Model.StockModel as StockModel

model=StockModel
view=StockView

#access data from the model 
def dataFetch(tickers): 
    return model.getData(tickers)
    
#download data from the model
def dataDownload(endPoints,tickers):
    data = model.downloadData(endPoints,tickers)
    return data

#display the graph of both ETF's 
def display_historical_graph(data):
    view.displayData(data)

#determine short-term and long-term moving averages
def moving_Average(data):
    data['SMA20']=model.SMA(data,20,'Close')
    data['SMA50']=model.SMA(data,50,'Close')
    return data

#determine buy and sell signals using moving average cross over stratergy
def movingAverageSignals(data):
    return model.stockPurchase(data)   

#plot the resultant of buy and sell signals according to averages
def movingAveragesPlot(name, data):
    view.movingAveragesPlot(name,data)

#determine the upper and lower bands for bollinger stratergy
def bollingerBands(data, window_Size):
    model.bollingerBands(data,window_Size)

#determine RSI for the ETF's   
def RSI(data,window_Size):
    model.RSI(data, window_Size)

#determine the buy and sell signals using Bollinger Band + RSI Stratergy
def stratergy(data):
    return model.stratergy(data)

#plot the signals using the buy and sell signals using Bollinger Band + RSI Stratergy
def bollingerPlot(name, data):
    view.bollingerRSI_Plot(name,data) 