import math
class cilindrouwu:
    def __init__(self):
        self.radio = 0
        self.altura = 0
    def metodo(self):
        tuboarea = math.pi*(self.radio*self.radio)*self.altura
        return tuboarea    
print("metele el radio y la altura de tu cilindro")
objeto = cilindrouwu()
objeto.radio = float(input("radio gaga: "))
objeto.altura = float(input("con altura: "))
añia = objeto.metodo()
print("el área es: ",añia)
