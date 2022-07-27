# 1. Price gain greater than 3%
# 2. Price of share is greater than 300
from numpy import true_divide


def stratergy2(df):
    df_last = df.tail(20)
    close = df_last.iloc[-1]['close']
    avgvolume = df_last.iloc[-1]['avgvolume']
    percentchange = df_last.iloc[-1]['percentchange']
    high20Day = df_last['close'].max()

   
    if (close > 300 and (avgvolume*close > 10000000)  and percentchange >= 0.03 and high20Day < close) :
        return True
    else : 
        return False