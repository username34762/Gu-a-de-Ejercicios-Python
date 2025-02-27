import Mis_matemáticas

num1 = int(input("Ingrese el numero 1: "))
num2 = int(input("Ingrese el numero 2: "))
objeto = Mis_matemáticas.Mis_matematicas(num1,num2)
print(objeto.multiplicacion())
print(objeto.resta())
print(objeto.suma())
print(objeto.division())
print("El factorial de num1 es: ",objeto.factorial())
print("El factorial de num2 es: ",objeto.factorial2())
print("La división entre tus dos numeros da como resultado que: ",objeto.es_primo())
print("La división entre tus dos numeros da como resultado que: ",objeto.es_primo2())