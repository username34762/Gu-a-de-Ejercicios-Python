# Crea una función que reciba una lista de nombres y los guarde en un archivo
# Crea otra función que lea el archivo y devuelva la lista de nombres
#Ejercicio 8.1
def guardar_nombres(lista_nombres, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        for nombre in lista_nombres:
            archivo.write(nombre + '\n')

def leer_nombres(nombre_archivo):
    lista_nombres = []
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            lista_nombres.append(linea.strip())
    return lista_nombres

nombres = ["Axel", "Javier", "Daniel", "Rodrigo"]
guardar_nombres(nombres, 'nombres.txt')
nombres_leidos = leer_nombres('nombres.txt')
print(nombres_leidos)

#Ejercicio 8.2 
import csv

empleados = [
    ["Nombre", "Edad", "Cargo", "Salario"],
    ["Rodrigo", 30, "Desarrollador", 1500],
    ["Itzel", 25, "Diseñadora", 1200],
    ["Axel", 35, "Desarrollador", 1800],
    ["Angie", 28, "Diseñadora", 1300]
]

with open('empleados.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(empleados)

cargos = {}
with open('empleados.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        cargo = row[2]
        salario = int(row[3])
        if cargo not in cargos:
            cargos[cargo] = []
        cargos[cargo].append(salario)

for cargo, salarios in cargos.items():
    print("El salario promedio de", cargo, "es:", sum(salarios)/len(salarios))
