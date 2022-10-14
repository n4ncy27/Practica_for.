# Ejemplo básicos instrucción for 
print("Ejercicio 1\n")

for i in [1,2,3,4,5]:
    print(i)

print("Ejercicio 2\n")
for i in (1,2,3,4,5):
    print(i)

print("Ejercicio 3\n")
lista = [1,2,3,4,5]
for i in lista:
    print(i)

print("Ejercicio 4\n")
for i in range(1,6):
    print(i)


print("Ejercicio 5\n")
texto = "UIS no es uno, somos todos"
for i in texto:
    print(i)

print ("Ejercicio 6: suma N primeros números")
suma = 0
for i in range(10) :
    suma = suma + 1
print(suma)

print ("Ejercicio 7: suma N primeros números")
N = int(input("Digite el valor de N: "))
suma = 0
for i in range(1,N+1) :
    suma = suma + 1
print(suma)

print ("Ejercicio 8: Contar vocales en frase")
frase = input("Digite una frase: ")
base = "aeiouAEIOU"
num_vocales = 0
for i in frase:
    if i in base:
        num_vocales = num_vocales + 1 
print("El numero de vocales es " + str(num_vocales))
