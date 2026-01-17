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
    elif opcion == 2:
        resta()
    elif opcion == 3:
        multiplicacion()
    elif opcion == 4:
        division()
    else:
        print("Opcion no valida")

def suma():
    num1 = int(input("Dame el primer numero: "))
    num2 = int(input("Dame el segundo numero: "))
    resultado = num1 + num2
    print("El resultado de la suma es:", resultado)
    
def resta():
    num1 = int(input("Dame el primer numero: "))
    num2 = int(input("Dame el segundo numero: "))
    resultado = num1 - num2
    print("El resultado de la resta es:", resultado)
    
def multiplicacion():
    num1 = int(input("Dame el primer numero: "))
    num2 = int(input("Dame el segundo numero: "))
    resultado = num1 * num2
    print("El resultado de la multiplicacion es:", resultado)
    
def division():
    num1 = int(input("Dame el primer numero: "))
    num2 = int(input("Dame el segundo numero: "))
    resultado = num1 / num2
    print("El resultado de la division es:", resultado)
    
def main():
    menu()
    
if __name__ == "__main__":
    main()