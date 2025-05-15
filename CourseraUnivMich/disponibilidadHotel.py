# Manejo de disponibilidad de habitaciones en un hotel
# 15 pisos y 20 habitaciones por piso
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(1)]

def reservar_habitacion():
    piso = int(input("Introduce el número de piso (0-14): "))
    habitacion = int(input("Introduce el número de habitación (0-19): "))
    if rooms[0][piso][habitacion]:
        print("La habitación ya está ocupada.")
    else:
        rooms[0][piso][habitacion] = True
        print("Habitación reservada con éxito.")

def desocupar_habitacion():
    piso = int(input("Introduce el número de piso (0-14): "))
    habitacion = int(input("Introduce el número de habitación (0-19): "))
    if not rooms[0][piso][habitacion]:
        print("La habitación ya está desocupada.")
    else:
        rooms[0][piso][habitacion] = False
        print("Habitación desocupada con éxito.")

def consultar_habitacion():
    piso = int(input("Introduce el número de piso (0-14): "))
    habitacion = int(input("Introduce el número de habitación (0-19): "))
    estado = "ocupada" if rooms[0][piso][habitacion] else "desocupada"
    print(f"La habitación en el piso {piso}, número {habitacion}, está {estado}.")

# Menú principal
while True:
    print("\nOpciones:")
    print("1. Reservar habitación")
    print("2. Desocupar habitación")
    print("3. Consultar habitación")
    print("4. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        reservar_habitacion()
    elif opcion == "2":
        desocupar_habitacion()
    elif opcion == "3":
        consultar_habitacion()
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")