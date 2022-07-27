import datetime
import pandas as pd
import stratergy3


def top_20(df, symbol):
    price_30_days_ago = stratergy3.getDataForDate(df,30,0)
    if price_30_days_ago != None:
        close = df.iloc[-1]['close']
        thir_day_percent_change = (close - price_30_days_ago)/price_30_days_ago
        df_new = pd.DataFrame({'Name' : symbol,
        'Percent_Change':thir_day_percent_change}, index=[0])
        return df_new
    else :
        df_new = pd.DataFrame({'Name' : symbol,
        'Percent_Change':0}, index=[0])
        print ('None came in')
        return df_new

if __name__ == "__main__":
    df = pd.read_csv('3MINDIA.NS_data.csv', index_col='Date', parse_dates=True)
    print(top_20(df,'3MINDIA'))