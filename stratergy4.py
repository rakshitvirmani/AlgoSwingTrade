#Moving Average Crossover
#20 DMA crosses 50DMA
#50DMA crosses 200DMA
#10DMA cross 20DMA
import pandas as pd

def stratergy4(df):
    #50 cross 200
    condition1 = df.iloc[-2]['ma50'] < df.iloc[-2]['ma200']
    condition2 = df.iloc[-1]['ma50'] > df.iloc[-1]['ma200']

    #10 cross 20
    condition3 = df.iloc[-2]['ma10'] < df.iloc[-2]['ma20']
    condition4 = df.iloc[-1]['ma10'] > df.iloc[-1]['ma20']

    #20 cross 50
    condition5 = df.iloc[-2]['ma20'] < df.iloc[-2]['ma50']
    condition6 = df.iloc[-1]['ma20'] > df.iloc[-1]['ma50']

    if (condition1 and condition2) or (condition3 and condition4) or (condition5 and condition6):
        return True
    else : 
        return False