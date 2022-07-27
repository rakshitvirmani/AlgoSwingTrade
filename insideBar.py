import pandas as pd

def insideBar(df):
    #get last 3 days data 
    df_3_days = df.tail(3)

    close_day1 = df_3_days.iloc[0]['close']
    high_day1 = df_3_days.iloc[0]['high']
    low_day1 = df_3_days.iloc[0]['low']
    open_day1 = df_3_days.iloc[0]['open']
    
    close_day2 = df_3_days.iloc[1]['close']
    high_day2 = df_3_days.iloc[1]['high']
    low_day2 = df_3_days.iloc[1]['low']
    open_day2 = df_3_days.iloc[1]['open']

    close_day3 = df_3_days.iloc[2]['close']
    high_day3 = df_3_days.iloc[2]['high']
    low_day3 = df_3_days.iloc[2]['low']
    open_day3 = df_3_days.iloc[2]['open']

    
    positive_candle1 = close_day1 > open_day1
    negative_candle1 = close_day1 < open_day1
    positive_candle2 = close_day2 > open_day2
    negative_candle2 = close_day2 < open_day2

    #inside candlle
    condition1 = low_day1 < low_day2 and high_day1 > high_day2 
    condition2 = (positive_candle1 and negative_candle2) or (positive_candle2 and negative_candle1)
    
    if(positive_candle1 and negative_candle2):
        condition3 = close_day3 > high_day1
    elif(positive_candle2 and negative_candle1) :
        condition3 = close_day3 < low_day1

    if(condition1 and condition2 and condition3):
        return True
    else: 
        return False


if __name__ == "__main__":
    df = pd.read_csv('TATAELXSI.NS_data.csv', index_col='Date', parse_dates=True)
    print(insideBar(df))