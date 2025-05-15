# Solicitar el número de bloques
bloques = int(input("Introduce el número de bloques: "))

altura = 0
nivel = 1

# Calcular la altura de la pirámide
while bloques >= nivel:
    bloques -= nivel
    altura += 1
    nivel += 1

print(f"La altura de la pirámide es: {altura}")