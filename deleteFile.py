import os

def deleteFile():
    symbol = []

    with open('ST-50.txt') as f:  
        for line in f:
            symbol.append(line.strip())
    f.close
    for i in symbol:
        print(len(symbol), i)
        fileName = i + '.NS_data.csv'
        if os.path.exists(fileName):
            os.remove(fileName)
        else:
            print("The file does not exist")
        
    


if __name__ == "__main__":
    deleteFile()