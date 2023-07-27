import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

# plot to display data from the API's
def displayData(dataframe):
        color=['firebrick','blue']
        ETF=['FNGU', 'FNGD']
        plt.figure(figsize=(16,8))
        sns.set_style("ticks")        
        for df, clr, name in zip(dataframe,color,ETF):
            plt.plot(df['Close'])        
        plt.xlabel('Date', fontsize=18)
        plt.ylabel('Close Price', fontsize=18)
        plt.title("The Stock Price of FNGU and FNGD",size='x-large',color='blue')        
        plt.show()

#plot for Moving Average stratergy for FNGU and FNGD
def movingAveragesPlot(name,dataFrame):
        plt.figure(figsize=(16,8))
        plt.title("Moving Average Stratergy Implemented with Buy and Sell Signals of "+name,fontsize=18)
        plt.plot(dataFrame['Close'],alpha=0.5, label='Close')
        plt.plot(dataFrame['SMA20'],alpha=0.5, label='SMA20')
        plt.plot(dataFrame['SMA50'],alpha=0.5, label='SMA50')
        plt.scatter(dataFrame.index,dataFrame['Buy'], alpha=1, label='Buy Signal',marker='^', color='green')
        plt.scatter(dataFrame.index,dataFrame['Sell'], alpha=1, label='Sell Signal',marker='v', color='red')
        plt.xlabel('Date',fontsize=18)
        plt.ylabel('Close Price',fontsize=18)
        plt.legend()
        plt.show()

#plot for Bollinger Bands+ RSI stratergy for FNGU and FNGD
def bollingerRSI_Plot(name, data):
         fig, ax = plt.subplots(figsize=(16,8))
         plt.title("Bollinger Band & RSI Trading Stratergy of "+name)
         plt.ylabel('Price')
         plt.xlabel('Dates')
         ax.plot(data['Close'],label='Close Price', alpha=0.25, color='blue')
         ax.plot(data['UpperBand'],label='Upper Band', alpha=0.25, color='yellow')
         ax.plot(data['LowerBand'],label='Lower Band', alpha=0.25, color='purple')
         ax.fill_between(data.index, data['UpperBand'], data['LowerBand'], color='grey')
         ax.scatter(data.index, data['Buy'], label='Buy', alpha=1, marker='^', color='green')
         ax.scatter(data.index, data['Sell'], label='Sell', alpha=1, marker='v', color='red')
         plt.legend()
         plt.show()