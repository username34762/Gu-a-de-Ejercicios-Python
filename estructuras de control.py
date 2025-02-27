# Dado un número, imprime:
# - "Par positivo" si es par y mayor que cero
# - "Par negativo" si es par y menor que cero
# - "Impar positivo" si es impar y mayor que cero
# - "Impar negativo" si es impar y menor que cero
# - "Cero" si es exactamente cero

def numeros(numero):
    if numero == 0:
      print("Cero")
    elif numero % 2 == 0:  
        if numero > 0: 
            print("Par positivo")
        else: 
            print("Par negativo")
    else:  
        if numero > 0:
            print("Impar positivo")
        else:  
            print("Impar negativo")


numeros(5)    
numeros(-4)   
numeros(0) 
numeros(8)    
numeros(-7)   

#fibonacci
n = int(input("Ingrese un numero: ")) 
a = 0
b = 1
for i in range(n):
    print(a)  
    c = a + b 
    a = b  
    b = c 


#Escribe un programa que recorra una lista e imprima solo los números pares.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numeros:
    if i % 2 == 0:
        print(i)