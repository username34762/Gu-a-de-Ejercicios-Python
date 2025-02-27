#Ejercicio 3.1
lista = [1, 2, 3, 4, 5]
# a) Añade el número 6 al final
# b) Inserta el número 0 al inicio
# c) Elimina el número 3
# d) Ordena la lista en orden descendente
# e) Crea una nueva lista con los elementos duplicados
lista.append(6) #a
lista.insert(0,0) #b
lista.pop(3) #c
lista.reverse() #d
lista_duplicada = [x*2 for x in lista] #e
print(lista)
print(lista_duplicada)


#Ejercicio 3.2
numeros = [23, 54, 12, 87, 32, 45, 98, 76]
# Encuentra y muestra el segundo valor más alto
maximo = max(numeros)
numeros.remove(maximo)
segunto_alto = max(numeros)
print("El segundo numéro mas alto es: ",segunto_alto)

#Ejercicio 3.3
texto = "Python es un lenguaje de programación. Python es fácil de aprender."
palabras = texto.split()
frecuencia = {}
for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] +=1
    else:
        frecuencia[palabra] = 1
print(frecuencia)

#Ejercicio 3.4
estudiantes = {
 "Juan": {"edad": 20, "curso": "Python", "promedio": 8.5},
 "María": {"edad": 22, "curso": "Java", "promedio": 9.0},
 "Pedro": {"edad": 21, "curso": "Python", "promedio": 7.8}
}
# a) Agrega un nuevo estudiante
# b) Actualiza el promedio de Juan a 9.0
# c) Muestra solo los estudiantes de Python
# d) Calcula el promedio de edad de todos los estudiantes
estudiantes["Rodrigo"] = {"edad": 20,"curso": "Python", "promedio": 8.9}

estudiantes["Juan"]["promedio"] = 9.0

print(estudiantes)

for nombre, datos in estudiantes.items():
    if datos["curso"] == "Python":
        print("Estos estudiantes cursan Python: ",nombre)

total_edad = sum(datos["edad"] for datos in estudiantes.values())
promedio_edad = total_edad / len(estudiantes)

print(f"El promedio de edad de los estudiantes es: {promedio_edad:.1f}")