# NEIN

import requests
import datetime


class Moneda():
    
    #def __init__(self, compra, venta, fecha):
    #    self.compra = compra
    #    self.venta = venta
    #    self.fecha = fecha

    def __init__(self, venta, fecha):
        self.venta = venta
        self.fecha = fecha
        
    def dBlue(self):
        self.compra, self.venta, self.fecha = blue()

    def dOficial(self):
        self.compra, self.venta, self.fecha = dolar_oficial()

    def dTarjeta(self, venta, fecha):
        self.venta, self.fecha = dolar_turista()


def blue():
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

def fecha():
    url = 'https://api-dolar-argentina.herokuapp.com/api/dolarturista'
    r = requests.get(url)
    data = r.json()
    fecha = data.get('fecha')
    return fecha

#compra, venta, fecha = blue()
#dblue = Moneda(compra, venta, fecha)
#print(dblue.compra, dblue.venta, dblue.fecha)

fesha = fecha()
dolar = Moneda(fesha)
azul = dolar.dBlue()
unicornio = dolar.dOficial()
ponele_que_solidario = dolar.dTarjeta()

print(ponele_que_solidario)

        