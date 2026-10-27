suma = 0
 
for i in range(3):
    nota = float(input("Ingresa una nota: "))
    suma += nota
 
p = suma / 3
print("Tu promedio es:", p)
 
if p >= 3:
    print("Aprobaste")
else:
    print("Reprobaste")
