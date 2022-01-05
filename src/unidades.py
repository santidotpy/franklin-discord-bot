

def feet_and_meter(numero:float, unidad_numero):
    conversor = 3.281
    if unidad_numero == 'ft':
        resultado = "%.2f" % (numero / conversor)
        show = f'{numero} ft = {resultado} m'

    elif unidad_numero == 'm':
        resultado = "%.2f" % (numero * conversor)
        show = f'{numero} m = {resultado} ft'

    else:
        raise ValueError('Indicador incorrecto')

    return show


def inches_and_cm(numero:float, unidad_numero):
    conversor = 2.54
    if unidad_numero == '"':
        resultado = "%.2f" % (numero * conversor)
        show = f'{numero} " = {resultado} cm'
    
    elif unidad_numero == 'cm':
        resultado = "%.2f" % (numero / conversor)
        show = f'{numero} cm = {resultado} "'

    else:
        raise ValueError('Indicador incorrecto')

    return show

