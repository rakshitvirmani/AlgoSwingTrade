

#settings for importing built-in datetime and date libraries
#and external pandas_datareader libraries
 
from webbrowser import get
import pandas_datareader.data as web
import datetime
import os
 
def getData():
    #read ticker symbols from a file to python symbol list
    symbol = []
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname('ST-50.txt')))

    with open('ST-50.txt') as f:  
        for line in f:
            symbol.append(line.strip())
    f.close
    
    
    #datetime is a Python module
    
    #datetime.datetime is a data type within the datetime module
    #which allows access to Gregorian dates and today function
    
    #datetime.date is another data type within the datetime module
    #which permits arithmetic with Gregorian date components
    
    #definition of end with datetime.datetime type must precede
    #definition of start with datetime.date type
    
    #the start expression collects data that are up to five years old
    
    end = datetime.datetime.today()
    
    start = datetime.datetime.now() - datetime.timedelta(days=365)
    
    
    #loop through 50 tickers in symbol list with i values of 0 through 49
    
    #if no historical data returned on any pass, try to get the ticker data again
    
    #for first ticker symbol write a fresh copy of csv file for historical data
    #on remaining ticker symbols append historical data to the file written for
    #the first ticker symbol and do not include a header row

    for i in symbol:
        i = i + '.NS'
        print(len(symbol), i)
        fileName = i + '_data.csv'
        try : 
            df = web.DataReader(i, 'yahoo', start, end)
            df.columns = ['high', 'low','open', 'close', 'volume', 'adjustedclose']
            df['ma10'] = round(df['adjustedclose'].rolling(10).mean(),2)
            df['ma20'] = round(df['adjustedclose'].rolling(20).mean(),2)
            df['ma50'] = round(df['adjustedclose'].rolling(50).mean(),2)
            df['ma200'] = round(df['adjustedclose'].rolling(200).mean(),2)
            df['avgvolume'] = round(df['volume'].mean(),2)
            df['percentchange'] = round((df['adjustedclose']/df['adjustedclose'].shift(1)) -1 ,2)
            df.to_csv(fileName)      
        except : 
            print('Cannot download data for ' + i)
            continue  
        # if i == 0:
            
        #     print (i,'has data stored to csv file')
        # else:
        #     df.to_csv(fileName,mode = 'a',header=False)
        #     print (i,'has data stored to csv file')

if __name__ == "__main__":
    getData()