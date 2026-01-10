""" crear un programa que permita realizar las operaciones basicas +, -, *, /
utilizando un funciones que cada operacion y un menú principal para desplegar y
elegir que operacion realizaremos
"""

def menu():
    print("1.Suma")
    print("2.Resta")
    print("3.Multiplicacion")
    print("4.Division")
    opcion = int(input("Elige una opcion: "))
    if opcion == 1:
        suma()
    if opcion == 2:
        resta()
    if opcion == 3:
        multiplicacion()
    if opcion == 4:
        division()

def suma():
    num1 = int(input("Dame el primer numero: "))
    num2 = int(input("Dame el segundo numero: "))
    resultado = num1 + num2
    print(resultado)
    
def resta():
    num1 = int(input("Dame el primer numero: "))
    num2 = int(input("Dame el segundo numero: "))
    resultado = num1 - num2
    print(resultado)
    
def multiplicacion():
    num1 = int(input("Dame el primer numero: "))
    num2 = int(input("Dame el segundo numero: "))
    resultado = num1 * num2
    print(resultado)
    
def division():
    num1 = int(input("Dame el primer numero: "))
    num2 = int(input("Dame el segundo numero: "))
    resultado = num1 / num2
    print(resultado)
    
def main():
    menu()
    
if __name__ == "__main__":
    main()