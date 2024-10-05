# squares = [x**2 for x in range(1,11)]
# print("Cuadrados:", squares)

#List Comprehension
# celsius = [x*10 for x in range(0,5)]
# fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
# print(celsius)
# print("Temperatura en F:", fahrenheit)

# #numeros pares
# pares = [x for x in range(1,21) if x%2 == 0]
# print(pares)
# impares = [x for x in range(1,21) if x%2 != 0]
# print(impares)

# matriz = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]

# transposed = [[row[i] for row in matriz] for i in range(len(matriz[0]))]
# print(transposed)

#Conditionals
is_member = False
age = 18

if is_member:
    if age >= 15:
        print("Tienes acceso ya que eres miembro y mayor o igual a 15 años")

    else:
        print("No tienes acceso ya que eres miembro pero menor a 15 años")
    
else:
    print("Quien sos?")