import math
class exuacióndetercergrado:
    def __init__(self):
        self.X = 0
        self.nosoyysoyw =0
    def metodo(self):
        nosoyysoyw = 4*(self.x**3) + 2*(self.x**2) + 6*self.x - 5
        return nosoyysoyw    
print("reealizar esta ecuación con x: Y = 4X³ + 2X² + 6X - 5")
objeto = exuacióndetercergrado()
objeto.x = float(input("ingrésa x: "))
nosoyysoyw = objeto.metodo()
print("el valor de y es: ",nosoyysoyw)
