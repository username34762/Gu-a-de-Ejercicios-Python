#Ejercicio 4.1
# Crea la función suma_total que pueda recibir cualquier cantidad de números
# Ejemplo: suma_total(1, 2, 3, 4) debe devolver 10
def suma_total(*numeros): # (*numeros) puede recibir cualquier cantidad, nuevo conocimiento
    return sum(numeros)

suma = suma_total(1,2,3,4)
print(suma)
    
#Ejercicio 4.2
# Crea un decorador tiempo_ejecucion que imprima cuánto tiempo tardó en ejecutarse la función decorada
import time

def tiempo_ejecucion(func):
    def ejecucion():
        inicio = time.time()
        func()
        print(f"Tiempo de ejecución: {time.time() - inicio:.5f} segundos")
    return ejecucion

@tiempo_ejecucion
def mi_funcion():
    time.sleep(2)
    print("Función terminada")

mi_funcion()
