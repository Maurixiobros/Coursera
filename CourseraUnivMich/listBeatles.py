beatles=[]
print("Paso 1:", beatles)

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Paso 2:", beatles)

for name in range(2):
    name = beatles.append(str(input("Agrega los demás: ")))
    
print("Paso 3:", beatles)

del beatles[3]
del beatles[3]
print("Paso 4:", beatles)

beatles.insert(0,"Ringo Starr")
print("Paso 5:", beatles)


# probando la longitud de la lista
print("Los Fav", len(beatles))

