# Stock moved 3-5 percent in the past 50 days three times
# Volume should be 50% higher than the previous days
# Trading above 50 DMA
# Price > 300
# Average daily volume > Rs 1 crore

import pandas as pd

def stratergy5(df):
    #get last 50 days data 
    df_50_days = df.tail(50)
    df_5_percent_increase = len(df_50_days.loc[(df_50_days['percentchange']>=0.05) & (df_50_days['volume'] > df_50_days['volume'].shift(1)*1.5)])
    
    condition1 = df_5_percent_increase > 3
    condition2 = df_50_days.iloc[-1]['close'] > df_50_days.iloc[-1]['ma50']
    condition3 = df_50_days.iloc[-1]['close'] > 300
    condition4 = df_50_days.iloc[-1]['close'] * df_50_days.iloc[-1]['avgvolume'] > 10000000

    if(condition1 and condition2 and condition3 and condition4):
        return True
    else: 
        return False


if __name__ == "__main__":
    df = pd.read_csv('TATAELXSI.NS_data.csv', index_col='Date', parse_dates=True)
    print(stratergy5(df))

