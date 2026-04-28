import math
class murodeberlinxd:
    def __init__(self):
        self.pim = 0
        self.charlie = 0
        self.jefe = 0
        self.alan = 0
    def metodo(self):
        dis = ((self.charlie-self.pim)**2 + (self.alan-self.jefe)**2) ** 0.5
        return dis    
print("metele punto 1")
objeto = murodeberlinxd()
objeto.pim = float(input("distancia inicial a: "))
objeto.charlie = float(input("distancia final a : "))
objeto.jefe = float(input("distancia inicial b: "))
objeto.alan = float(input("distancia final b: "))
añia = objeto.metodo()
print("la distancia que los separa es: ",añia)
