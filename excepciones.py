#Ejercicio 6.1
# Escribe una función division_segura que reciba dos números,
# realice la división y maneje correctamente las excepciones de:
# - División por cero
# - Tipo de dato incorrecto (si se pasan valores no numéricos)
def division_segura(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        return "Error: No se puede dividir por cero."
    except TypeError:
        return "Error: Ambos valores deben ser números."


print(division_segura(10, 2))
print(division_segura(10, 0)) 
print(division_segura(10, 'a')) 

#Ejercicio 6.2
# Crea una excepción personalizada EdadInvalidaError
# Implementa una función verificar_edad que reciba una edad y:
# - Lance EdadInvalidaError si la edad es negativa o mayor a 120
# - Devuelva True si la edad es válida
def verificar_edad(edad):
    try:
        if edad < 0 or edad > 120:
            raise ValueError("La edad no debe ser negativa o mayor a 120")
    except ValueError as EdadInvalidaError:
        print(f"Error en tu edad: {EdadInvalidaError}")
    else:
        return True 

print(verificar_edad(5)) 
print(verificar_edad(400)) 
