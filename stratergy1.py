# 1. Price gain greater than 5%
# 2. Price of share is greater than 300
# 3. Volume = 10x of average daily volume
from numpy import true_divide


def stratergy1(df):
    df_last = df.tail(1)
    close = df_last.iloc[0]['close']
    volume = df_last.iloc[0]['volume']
    avgvolume = df_last.iloc[0]['avgvolume']
    percentchange = df_last.iloc[0]['percentchange']
   
    if (close > 300 and  volume > (avgvolume*5) and percentchange >= 0.05) :
        return True
    else : 
        return False
    