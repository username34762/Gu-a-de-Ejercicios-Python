import math

class Mis_matematicas:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def suma(self):
        return self.a + self.b
    def resta(self):
        return self.a - self.b
    def multiplicacion(self):
        return self.a * self.b
    def division(self):
        return self.a / self.b
    def factorial(self):
        return math.factorial(self.a)
    def factorial2(self):
        return math.factorial(self.b)
    def es_primo(self):
        if self.a < 2:
            return f"{self.a} no es primo"
        for i in range(2, self.a):
            if self.a % i == 0:
                return f"{self.a} no es primo"
        return f"{self.a} es primo"
    def es_primo2(self):
        if self.b < 2:
            return f"{self.b} no es primo"
        for i in range(2, self.b):
            if self.b % i == 0:
                return f"{self.b} no es primo"
        return f"{self.b} es primo"
