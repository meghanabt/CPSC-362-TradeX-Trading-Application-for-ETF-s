import View.StockView as StockView
import Model.StockModel as StockModel
import Controller.StockController as StockController


if __name__ == "__main__":
        model = StockModel
        view = StockView
        controller = StockController

        tickers = ['FNGU','FNGD']
        API_Endpoint=[]    

        # access API's to fetch datat and display on the CLI        
        API_Endpoint=controller.dataFetch(tickers)
        data= controller.dataDownload(API_Endpoint, tickers)

        # Display historical graph 
        controller.display_historical_graph(data)

        #Plot for Moving Average Stratergy for Both FNGU and FNGD
        controller.movingAveragesPlot('FNGU',controller.movingAverageSignals(controller.moving_Average(data[0])))
        controller.movingAveragesPlot('FNGD',controller.movingAverageSignals(controller.moving_Average(data[1])))

        #define and get bollinger bands
        controller.bollingerBands(data[0],30)
        controller.bollingerBands(data[1],30)

        #determine RSI for FNGU and FNGD
        controller.RSI(data[0],30)
        controller.RSI(data[1],30)

        #buy and sell signals for FNGU using Bollinger-RSI stratergy
        buy_Price_FNGU,sell_Price_FNGU= controller.stratergy(data[0])
        data[0]['Buy']=buy_Price_FNGU
        data[0]['Sell']=sell_Price_FNGU

        #buy and sell signals for FNGD using Bollinger-RSI stratergy
        buy_Price_FNGD,sell_Price_FNGD= controller.stratergy(data[1])
        data[1]['Buy']=buy_Price_FNGD
        data[1]['Sell']=sell_Price_FNGD

        #plots for Bollinger Band Stratergy + RSI for FNGU and FNGD
        controller.bollingerPlot('FNGU', data[0])
        controller.bollingerPlot('FNGD', data[1])