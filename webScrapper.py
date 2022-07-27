import requests
from bs4 import BeautifulSoup

# Make a request to https://www.screener.in/company/{tickr}/consolidated/#ratios
# Store the result in 'page' variable

def getFinancialData(ticker):
    url = 'https://www.screener.in/company/'+ticker+'/consolidated/#ratios'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    fin_data = {}
    fin_data['Ticker'] = ticker
    status = page.status_code

    if (status == '200'):
        numbers = soup.select('div.company-ratios > ul#top-ratios >li')
        for num in numbers:
            name = num.select('span.name')[0].text.strip()
            value = num.select('span.value > span')[0].text.strip()
            fin_data[name] = value        
        return fin_data
    else :
        fin_data['error'] = 'Error : Status code not equal to 200'
        return fin_data
    
if __name__ == "__main__":
    print(getFinancialData('PGEL'))