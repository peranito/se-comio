def PreguntarNum():
    for k in range(10):
        print("¿Escribe un número positivo o negativo?")
        Num = input()
        if Num > '0':
            print("El número", Num, "es positivo")
        elif Num < '0':
            print("El número", Num, "es Negativo")
        else:
            print("El número es cero")
 
def main():
    PreguntarNum()
    
main()