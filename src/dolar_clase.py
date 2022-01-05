# NEIN
from clases import blue


class Dolar():

    def __init__(self, venta, fecha):
        self.venta = venta
        self.fecha = fecha

    def blue(self):
        self.compra, self.venta, self.fecha = blue()

