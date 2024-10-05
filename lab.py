#Strings
# name = 'SY The Swordman'
# print(len(name))
# print(name.lower())
# print(name.upper())
# print(name.strip())

#Numeros
# x = 10
# y = 5.678

# print(type(x), x + x)
# print(type(y), y + x)

#inputs
# nombre = input("Ingrese su nombre: ")
# print(nombre)
# edad = int(input("ingrese su edad: "))
# print(edad)
# print(type(edad))

#Listas
# to_do =[
#     "Despertar",
#     "Desayunar",
#     "Arreglarme",
#     "Dormir"
# ]
# print(to_do)
# print(type(to_do))

# #matrices
# matriz = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]
# print(matriz)
# print(type(matriz))
# print(matriz[0])

# matriz2 = [[[1,2], [3,4]], [[6,7], [8,9]]]
# print(matriz2)

# numeros = (1,2.3,4,5,6,7,8,9)
# numeros2 = 1,2,3,4,5
# print(numeros)
# print(type(numeros2))

numbers = {1:"uno", 2:"dos", 3:"tres"}
print(numbers[2])
information = {"Syrios": {"Title": "The greatest Swordsman",
               "Attribute": "Dark",
               "Class": ["Berseker", "Assassin"]},
               "SY001": {"Title": "Silent death",
                         "Attribute": "Dark",
                         "Class": "Sorccerer"}}
print(information)

print(information.keys())
print(information["Syrios"].values())
print(information.items())
