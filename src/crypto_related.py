import requests
from json import JSONDecodeError
from help_msgs import img_coins, projects
# import concurrent.futures


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


def crypto_binancio(from_coin: str, to_coin='USDT'):
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
    exchanges = ['argenbtc', 'belo', 'bitmonedero',
                 'buenbit', 'copter', 'cryptomkt', 'decrypto',
                 'lemoncash', 'ripioexchange', 'satoshitango', 'tiendacrypto']

    sorted_prices = {}
    for exchange in exchanges:
        url = f'https://criptoya.com/api/{exchange}/usdt/ars'
        try:
            price = requests.get(url).json()['ask']
            sorted_prices[exchange] = price
        except (requests.exceptions.HTTPError, requests.exceptions.RequestException, ValueError, KeyError) as e:
            sorted_prices[exchange] = f'Error: {str(e)}'

    sorted_prices = dict(sorted(sorted_prices.items(), key=lambda x: x[1]))

    return sorted_prices
