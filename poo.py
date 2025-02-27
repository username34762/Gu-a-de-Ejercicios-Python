
#class Persona:
 # Implementa esta clase con:
 # - Atributos: nombre, edad, dirección
 # - Método constructor
 # - Método __str__ para representación en cadena
 # - Método cumplir_años que incremente la edad en 1
 # - Método cambiar_direccion que actualice la dirección

class Persona:
    def __init__(self, nombre, edad, direccion):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Dirección: {self.direccion}"

    def cumplir_años(self):
        self.edad += 1 

    def cambiar_direccion(self, nueva_direccion):
        self.direccion = nueva_direccion

persona1 = Persona("Rodrigo", 17, "Cidad Arce")
print(persona1)

persona1.cumplir_años() 
print(persona1)  

persona1.cambiar_direccion("Chanmico") 
print(persona1)  


#Ejercicio 5.2
# Crea una clase Estudiante que herede de Persona y añada:
# - Atributo: curso
# - Método: cambiar_curso
# - Sobrecarga del método __str__ para incluir el curso
class Estudiante(Persona): 
    def __init__(self, nombre, edad, direccion, curso):
        super().__init__(nombre, edad, direccion) 
        self.curso = curso  

    def cambiar_curso(self, nuevo_curso):
        self.curso = nuevo_curso 

    def __str__(self):
        return f"{super().__str__()}, Curso: {self.curso}" 



estudiante1 = Estudiante("Rodrigo", 17, "Chanmico", "JavaScript")
print(estudiante1)  

estudiante1.cambiar_curso("Python") 
print(estudiante1)  
