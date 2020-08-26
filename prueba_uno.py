nombre = "Oli"
edad =17
#print(f"Hola {nombre} tirnes {edad} ")
#nombre = input("Tu nombre: ")
#Comentario
#if edad>18:
#    print("Mayor de edad")
#else:
#    print('eres una ninia')
# ---CICLO FOR ---
'''
variable=5
for i in [0,1,3,9]:
    print(variable, "x", i, "=", variable*i)
print()
print("Fin")
'''
# ---LISTAS---
"""frutas=["Naranja", "Pera", "Melon", "Manzana", "Platano", "Limon"]
#frutas.append("Limon")
del frutas[1]
print(len(frutas))
"""
#Funciones
"""
name=input("Escribe tu nombre: ")

def funcion_uno(name):
    print(f"Hola {name}")

funcion_uno(name)
"""
#CUENTA REGRESIVA
"""
def cuenta_regresiva(numero):
    numero -= 1
    if numero > 0:
        print(numero)
        cuenta_regresiva(numero)
    else:
        print("Boooooooom!")
        print("Fin de la función", numero)
cuenta_regresiva(5)
"""

#FACTORIAL
"""
def factorial(numero):
    
    print("Valor inicial ->",numero)
    #print(f"{numero} x")
    if numero > 1:
        
        numero = numero * factorial(numero -1)

    print("valor final ->",numero)
    return numero

fac=factorial(5)
print(f"Resultado:  = {fac}")
"""

class OperacionesBasicas:
    def suma(self):
        self.n1 = 3
        self.n2 = 7
        

objeto = OperacionesBasicas()
objeto.suma()
resultado = objeto.n1+objeto.n2
print(resultado)



