import requests

def getCurrencyRate(from_currency, to_currency, api_key='FO3EX9RBHX6ZA858'):
    baseURL = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE'
# from documentation https://www.alphavantage.co/documentation/
    URL = baseURL + '&from_currency=' + from_currency + '&to_currency=' + to_currency + '&apikey=' + api_key
    r = requests.get(URL)
    data = r.json()
    rate =(data["Realtime Currency Exchange Rate"]
         ['5. Exchange Rate'])
    return rate

def convertCurrency(amountToConvert):
    fromCurrency = input('From: ').upper()
    toCurrency = input('To: ').upper()
    if isinstance(fromCurrency, str) or isinstance(toCurrency,str):
        return None
    rate = float(getCurrencyRate(fromCurrency, toCurrency))
    converted = amountToConvert * rate
    return converted



amount = 100
print(convertCurrency(amount))