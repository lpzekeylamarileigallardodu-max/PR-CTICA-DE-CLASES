class iluminati:
    def __init__(self):
        self.lado1 = 0
        self.lado2 = 0
        self.lado3 = 0
    def metodo(self):
         t =(self.lado1+self.lado2+self.lado3)/2
         aña=(t*(t-self.lado1)*(t-self.lado2)*(t-self.lado3))**0.5
         return aña    
print("ponle lo tres lados del nacho")
objeto = iluminati()
objeto.lado1 = float(input("Ingrese lado 1: "))
objeto.lado2 = float(input("Ingrese lado 2: "))
objeto.lado3 = float(input("Ingrese lado 3: "))
añia=objeto.metodo()
print("el área es: ", añia)
