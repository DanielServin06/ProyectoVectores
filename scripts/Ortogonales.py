import math
print("¡Hola! Bienvenid@")

print("Por favor, introduce las coordenadas de tu primer vector")
x = float(input())
y = float(input())


print("-----------------------")

print("Por favor, introduce las coordenadas de tu segundo vector")
a = float(input())
b = float(input())
print("-----------------------")
"""
Aquí se está declarando a los vectores resultantes de la suma vectorial (es r) y la
resta vectorial (es r2), para poder acceder a sus celdas de memoria y jugar con ellas 
"""
r = [x+a,y+b]
r2 = [x-a,y-b]

norma_r = math.sqrt(pow(r[0],2)+pow(r[1],2))
norma_r2 = math.sqrt(pow(r2[0],2)+pow(r2[1],2))

if a == -y:
        print("Los vectores son ortogonales, De hecho, ¡Has encontrado a su compadre ortogonal!")
elif norma_r == norma_r2:
    print("¡Los vectores son ortogonales!")

else:
    print("Los vectores no son ortogonales):")