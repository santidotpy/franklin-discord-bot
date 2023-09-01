import requests


def dolar_oficial():
    url = 'https://api.bluelytics.com.ar/v2/latest'
    try:
        r = requests.get(url)
        data = r.json()
        compra = data.get('oficial').get('value_buy')
        venta = data.get('oficial').get('value_sell')
        fecha = data.get('last_update')[:10]
        return compra, venta, fecha
    except:
        return 'Error al obtener el valor del dolar oficial'


def dolar_bolsa():
    url = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'
    try:
        r = requests.get(url)
        data = r.json()
        compra = float(data[4].get('casa').get('compra').replace(',', '.'))
        venta = float(data[4].get('casa').get('venta').replace(',', '.'))
        return compra, venta
    except:
        return 'Error al obtener el valor del dolar bolsa'


def dolar_blue():
    url = 'https://api.bluelytics.com.ar/v2/latest'
    try:
        r = requests.get(url)
        data = r.json()
        compra = data.get('blue').get('value_buy')
        venta = data.get('blue').get('value_sell')
        fecha = data.get('last_update')[:10]
        return compra, venta, fecha
    except:
        return 'Error al obtener el valor del dolar blue'


def dolar_tarjeta():
    compra, venta, fecha = dolar_oficial()
    compra = round(compra * 1.75, 2)
    venta = round(venta * 1.75, 2)
    return compra, venta, fecha

# si te pasas de los 300 te afanan mas


def dolar_turista():
    compra, venta, fecha = dolar_oficial()
    compra = round(compra * 2, 2)
    venta = round(venta * 2, 2)
    return compra, venta, fecha
