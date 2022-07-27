# 1. Price increased 20 percent in the past 30 days or 30 percent in the past 90 days or 50 percent in the past 120 days
# 2. Price of share is greater than 300
# 3. Currently in range of 10,20,50dma
# 4. Volume in terms of price is greater than 1 crore

from numpy import true_divide
import datetime
import pandas as pd

def getDataForDate(df,deltaDays,count):
    day = datetime.datetime.now() - datetime.timedelta(days=deltaDays)
    if day.strftime('%Y-%m-%d') in df.index:
 
        return df.loc[day.strftime('%Y-%m-%d')]['close']
    else :
      
        if count < 10:
            count = count + 1
            return getDataForDate(df,deltaDays-1,count)       

def stratergy3(df):
    
    price_30_days_ago = getDataForDate(df,30,0)
    price_90_days_ago = getDataForDate(df,90,0)
    price_120_days_ago = getDataForDate(df,120,0)
    close = df.iloc[-1]['close']
    avgvolume = df.iloc[-1]['avgvolume']
    percentchange = df.iloc[-1]['percentchange']


    thir_day_percent_change = (close - price_30_days_ago)/price_30_days_ago
    ninty_day_percent_change = (close - price_90_days_ago)/price_90_days_ago
    oneTwnety_day_percent_change = (close - price_120_days_ago)/price_120_days_ago
   
    if (close > 300 and (avgvolume*close > 10000000) and 
    ((thir_day_percent_change > 0.2) or (ninty_day_percent_change > 0.3) or (oneTwnety_day_percent_change > 0.50))) :
        return True
    else : 
        return False


if __name__ == "__main__":
    df = pd.read_csv('ASAHIINDIA.NS_data.csv', index_col='Date', parse_dates=True)
    print(stratergy3(df))
    