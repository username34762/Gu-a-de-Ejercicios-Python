#Ejercicio 10.1
# Escribe funciones para:
# - Calcular la edad exacta (años, meses, días) a partir de una fecha de nacimiento
# - Determinar cuántos días faltan para el próximo cumpleaños
from datetime import datetime

def calcular_edad(fecha_nacimiento):
    hoy = datetime.now()
    edad = hoy.year - fecha_nacimiento.year

    if hoy.month < fecha_nacimiento.month or (hoy.month == fecha_nacimiento.month and hoy.day < fecha_nacimiento.day):
        edad -= 1

    return edad

def dias_para_proximo_cumple(fecha_nacimiento):
    hoy = datetime.now()
    proximo_cumple = fecha_nacimiento.replace(year=hoy.year)

    if proximo_cumple < hoy:
        proximo_cumple = proximo_cumple.replace(year=hoy.year + 1)

    dias_faltantes = (proximo_cumple - hoy).days
    return dias_faltantes


fecha_nacimiento = datetime(2008, 1, 4)
edad = calcular_edad(fecha_nacimiento)
print(f"Tienes {edad} años.")
dias_faltantes = dias_para_proximo_cumple(fecha_nacimiento)
print(f"Faltan {dias_faltantes} días para tu próximo cumpleaños.")


#Ejercicio 10.2
# Implementa un generador de contraseñas que:
# - Cree contraseñas de longitud personalizable
# - Incluya letras mayúsculas, minúsculas, números y símbolos
# - Garantice al menos un carácter de cada tipo
import random
import string

def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + "!@#$%^&*()"

    contraseña = ''.join(random.choices(caracteres, k=longitud))

    return contraseña
longitud = 12
contraseña = generar_contraseña(longitud)
print(f"Tu nueva contraseña es: {contraseña}")
