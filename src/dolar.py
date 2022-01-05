import requests
#from requests.models import Response
#from help_msgs import img_coins

"""
Aparentemente la api que utilizo para el valor de el dolar en sus diferentes versiones no esta funcionando,
no se si es algo momentanio o algo mas serio
"""
"""
def dolar_blue():
    url = 'https://api-dolar-argentina.herokuapp.com/api/dolarblue'
    r = requests.get(url)
    diccio = r.json()
    return diccio


def dolar_oficial():
    url = 'https://api-dolar-argentina.herokuapp.com/api/dolaroficial'
    r = requests.get(url)
    diccio = r.json()
    return diccio


def dolar_turista():
    url = 'https://api-dolar-argentina.herokuapp.com/api/dolarturista'
    r = requests.get(url)
    diccio = r.json()
    return diccio
    """
def dolar_blue():
    url = 'https://api-dolar-argentina.herokuapp.com/api/dolarblue'
    r = requests.get(url)
    data = r.json()
    compra = data.get('compra')
    venta = data.get('venta')
    fecha = data.get('fecha')
    return compra, venta, fecha

def dolar_oficial():
    url = 'https://api-dolar-argentina.herokuapp.com/api/dolaroficial'
    r = requests.get(url)
    data = r.json()
    compra = data.get('compra')
    venta = data.get('venta')
    fecha = data.get('fecha')
    return compra, venta, fecha

def dolar_turista():
    url = 'https://api-dolar-argentina.herokuapp.com/api/dolarturista'
    r = requests.get(url)
    data = r.json()
    venta = data.get('venta')
    fecha = data.get('fecha')
    return venta, fecha
