
def sumarecursiva(numero):
    if (numero <= 9):
        return numero
    else: 
        return sumarecursiva(numero // 10) + numero % 10 
    
def  sumaiterativa(Numero):
    Suma = 0
    while Numero  > 9:
        Suma += Numero % 10 
        Numero //= 10 
    return (Suma + Numero)

print("Se calcula la suma de todos los digitos que se ingrese")

numerodatoingresado = int(input("ingresa el numero deseado: "))


print(f"la suma de {numerodatoingresado} con la sumarecursiva es: {sumarecursiva(numerodatoingresado)}")
print(f"la suma de {numerodatoingresado} con la sumaiterativa es: {sumaiterativa(numerodatoingresado)}")




