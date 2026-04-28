import math
class exponentecúbicont:
    def __init__(self):
        self.experimentodepruebaxd = 0
    def metodo(self):
        cubont = self.experimentodepruebaxd**(1/3)
        return cubont    
print("a qué número quieres reducir tan drásticamente?")
objeto = exponentecúbicont()
objeto.experimentodepruebaxd = float(input("ingrésalp: "))
cubont = objeto.metodo()
print("su exponente cúbico'nt es: ",cubont)

