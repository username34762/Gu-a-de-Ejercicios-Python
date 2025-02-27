a = 5  #int
b = 3.14 #float
c = "Python" #string
d = [1, 2, 3] #list
e = (4, 5, 6) #tuple
f = {"nombre": "Juan", "edad": 30} #dict
g = {1, 2, 3} #set
h = True #bool

# Convierte lo siguiente:

# - El entero 10 a flotante
entero = 10
flotante = float(entero)
print(flotante)

# - El flotante 7.5 a entero
decimal = 7.5
entero2 = int(decimal)
print(entero2)

# - La cadena "25" a entero
cadena = "25"
cadena_a_entero = int(cadena)
print(cadena_a_entero)

# - La lista [1, 2, 3] a tupla
lista = [1,2,3]
tupla = tuple(lista)
print(tupla)

# - La tupla (4, 5, 6) a lista
tupla2 = (4,5,6)
lista2 = list(tupla2)
print(lista2)

# - La lista [1, 2, 2, 3, 4, 4] a conjunto
lista3 = [1,2,2,3,4,4]
conjunto = set(lista3)
print(conjunto)


#Resuelve las siguientes expresiones y determina su resultado:
# Aritmética
a = 10 + 5 * 2 - 8 / 4  #18
b = (10 + 5) * (2 - 8) / 4 #-22.5

# Asignación
c = 10  # 10
c += 5  # c = 10 + 5 => c = 15
c *= 2  #30 c = 15 * 2 => c = 30
c /= 5  #6 c = 30 / 5 => c = 6.0
#el valor final de c sería 6.0

# Comparación
d = 10 > 5 # true
e = 10 != 10 #false
f = "abc" == "abc" #true

# Lógica
g = (10 > 5) and (7 < 12)  #true
h = (10 < 5) or (7 > 12) #false
i = not (10 > 5) #false