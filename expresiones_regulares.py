# Crea una función validar_email que determine si una cadena es un email válido
# Ejemplos válidos: usuario@dominio.com, nombre.apellido@empresa.co.uk
#Ejercicio 9.1
import re

def validar_email(email):
    patron = r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, email) is not None

# Ejemplos
print(validar_email("usuario@dominio.com"))
print(validar_email("nombre.apellido@empresa.co.uk"))
print(validar_email("correo_invalido"))

#Ejercicio 9.2
# Dado un texto con fechas en formato DD/MM/AAAA, extrae todas las fechas
texto = "La reunión será el 15/04/2023 y la entrega está programada para el 30/05/2023."

patron = r'\b\d{2}/\d{2}/\d{4}\b'

fechas = re.findall(patron, texto)

print("Fechas encontradas:", fechas)