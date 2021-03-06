import requests
from json import JSONDecodeError
from help_msgs import img_coins, projects


def get_coin_img(from_crypto):
    from_crypto = from_crypto.upper()
    if from_crypto in img_coins.keys():
        fotito = img_coins[from_crypto]
        return fotito
    else:
        fotito = img_coins['BINANCE_LOGO']
        return fotito


def get_url_project(from_crypto):
    from_crypto = from_crypto.upper()
    if from_crypto in projects.keys():
        url = projects[from_crypto]
        return url
    else:
        url = projects['PROJECTS']
        return url


def crypto_name(from_crypto: str):
    if from_crypto in img_coins.keys():
        coin_name = img_coins[from_crypto].split("/")[-2]
        coin_name = (coin_name.replace('-', ' ')).upper()
        return coin_name
    else:
        return from_crypto
    

def crypto_binancio(from_coin:str, to_coin='USDT'):
    from_coin = from_coin.upper()
    to_coin = to_coin.upper()
    
    url = f'https://www.binance.com/api/v3/ticker/24hr?symbol={from_coin}{to_coin}'
    r = requests.get(url)
    diccio = r.json()
    try:
        last_price = diccio['lastPrice']
    except KeyError:
        raise KeyError('Invalid Symbol')

    if last_price.startswith('0'):
        return last_price
    else:
        return last_price[:-5]

    
def usdt_arg_exchange():
    exchanges = [   'argenbtc', 'belo', 'bitex', 'bitmonedero', 'bitso',
                    'buenbit', 'copter', 'criptofacil', 'cryptomkt', 'decrypto',
                    'ftx','lemoncash', 'ripioexchange', 'satoshitango', 'tiendacrypto']

    sorted_prices = {}
    for exchange in exchanges:
        try:
            url = f'https://criptoya.com/api/{exchange}/usdt/ars'
            price = requests.get(url).json()['ask']
            #sorted_prices = dict.fromkeys(exchange, price)
            sorted_prices[exchange] = price
        except JSONDecodeError:
            url = f'https://criptoya.com/api/{exchange}/dai/ars'
            price = requests.get(url).json()['ask']
            sorted_prices[exchange] = price

    sorted_prices = dict(sorted(sorted_prices.items(), key=lambda item: item[1]))
    # Capitalize exchange names
    sorted_prices = dict((k.capitalize(), '$ '+ str(round(v, 2))) for k, v in sorted_prices .items())
    
    return sorted_prices
