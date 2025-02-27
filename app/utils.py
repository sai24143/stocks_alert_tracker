# import requests

# def get_stock_price(symbol):
#     API_KEY = '94NZU87B1LR8VOXK'
    
#     url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}'
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()
#         print(data)
#     else:
#         print('Error fetching data')
    
    
    
    
    # data = response.json()
    # if 'Global Quote' in data:
    #     return float(data['Global Quote'] ['05. price'])
    # return None








import yfinance as yf

def get_stock_price(symbol):
    try:
        ticker = yf.Ticker(symbol)
        historical_data = ticker.history(period="1d")
        
        if not historical_data.empty:
            return float(historical_data['Close'].iloc[-1]) 
        
    except Exception as e:
        print(f"Error fetching price for {symbol}: {e}")
    
    return None  
