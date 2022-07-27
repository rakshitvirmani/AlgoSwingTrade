import numpy as np
import pandas as pd
import getStockData 
import stratergy1
import stratergy2
import stratergy3
import stratergy4
import stratergy5
import deleteFile
import insideBar
import itertools
import top_20_stocks
import pywhatkit as pwt

if __name__ == "__main__":
    
    deleteFile.deleteFile()
    getStockData.getData()
    stratergy1List = []
    stratergy2List = []
    stratergy3List = []
    stratergy4List = []
    stratergy5List = []
    insideBarList = []
    commonList = []

    df_top_20 = pd.DataFrame()


    symbol = []
    with open('ST-50.txt') as f:  
        for line in f:
            symbol.append(line.strip())
    f.close

    for i in symbol:
        fileName = i + '.NS_data.csv'
        print(i)
        try:
            df = pd.read_csv(fileName)
            df_index_update = df.set_index('Date', inplace=False)

            if(stratergy1.stratergy1(df_index_update)) :
                stratergy1List.append(i)

            if(stratergy2.stratergy2(df_index_update)) :
                stratergy2List.append(i)

            if(stratergy3.stratergy3(df_index_update)) :
                stratergy3List.append(i)

            if(stratergy4.stratergy4(df_index_update)) :
                stratergy4List.append(i)

            if(stratergy5.stratergy5(df_index_update)) :
                stratergy5List.append(i)

            if(insideBar.insideBar(df_index_update)) :
                insideBarList.append(i)

            new_df = top_20_stocks.top_20(df_index_update,i)
            df_top_20 = pd.concat([df_top_20,new_df])
        except:
            print('Cannot open file for ' + fileName)

        
    
    df_top_20 = df_top_20.sort_values('Percent_Change', ascending=False)
    #df_top_20.to_csv('top_20.csv')
    df_top_20 = df_top_20.head(20)
    commonList = stratergy5List + stratergy3List + stratergy4List + stratergy2List + stratergy1List + insideBarList
    commonList.sort()
    #elements_in_all = list(set.intersection(*map(set, [stratergy5List,stratergy1List,stratergy2List,stratergy3List,stratergy4List])))

    
    print('Stratergy 1 list = ')
    print(stratergy1List)
    print('Stratergy 2 list = ')
    print(stratergy2List)
    print('Stratergy 3 list = ')
    print(stratergy3List)
    print('Stratergy 4 list = ')
    print(stratergy4List)
    print('Stratergy 5 list = ')
    print(stratergy5List)
    print('Inside Bar list = ')
    print(insideBarList)
    print('Top 20 = ')
    print(df_top_20)
    print('Common List =  ')
    print(commonList)



    
    

        