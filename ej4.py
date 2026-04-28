import math
class tomate:
    def __init__(self):
        self.precio = 0
        self.gg = 0
        self.ono = 0
        self.tot = 0
    def metodo(self):
        gg = self.precio*0.12
        ono = (gg+self.precio)*0.06
        tot = self.precio+self.gg+self.ono
        return gg,ono,tot    
print("metele punto 1")
objeto = tomate()
objeto.precio = float(input("cuánto cuesta la cybertruck: "))
gg,ono,tot = objeto.metodo()
print("vas a ganar: ",gg)
print("tus impuestos van a ser: ",ono,"(evádelos)")
print("total ",tot)
