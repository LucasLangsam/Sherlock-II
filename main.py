def digitos(numero):
    return len(numero)

def obtener_prefijo(numero, n):
    return int(numero[:n])

def tipo_tarjeta(numero):
    prefijo = obtener_prefijo(numero, 1)
    longitud = digitos(numero)

    if prefijo == 4:
        return "Visa" if longitud in [13, 16] else "Invalid"
    elif 34 <= int(numero[:2]) <= 37:
        return "American Express" if longitud == 15 else "Invalid"
    elif 51 <= int(numero[:2]) <= 55:
        return "Mastercard" if longitud == 16 else "Invalid"
    elif (36 <= prefijo <= 38) or (300 <= prefijo <= 305):
        return "Diners Club y Carte Blanche" if longitud == 14 else "Invalid"
    elif prefijo == 6011:
        return "Discover" if longitud == 16 else "Invalid"
    elif 1800 <= int(numero[:4]) <= 1803 or 1805 <= int(numero[:4]) <= 1809 or 1810 <= int(numero[:4]) <= 1812:
        return "JCB" if longitud == 16 else "Invalid"
    elif prefijo == 3:
        return "JCB" if longitud == 15 else "Invalid"
    else:
        return "Invalid"

def digitos_impares(numero):
    return [int(numero[i]) for i in range(len(numero) - 1, 0, -2)]

def digitos_pares(numero):
    return [int(numero[i]) for i in range(len(numero) - 2, 0, -2)]

def sumar_digitos(numeros):
    return sum(int(digito) for numero in numeros for digito in str(numero))

def luhn(numero):
    impares = digitos_impares(numero)
    pares = digitos_pares(numero)
    suma_impares = sumar_digitos(impares)
    suma_pares = sumar_digitos(pares)
    total = suma_impares + suma_pares
    return total % 10 == 0

def validar_tarjeta(numero):
    return tipo_tarjeta(numero) != "Invalid" and luhn(numero)
