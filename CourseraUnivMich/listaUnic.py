my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
unique_list = []  # Lista para almacenar los elementos únicos

for num in my_list:
    if num not in unique_list:  # Verificar si el número ya está en la lista única
        unique_list.append(num)  # Agregar solo si no está presente

print("La lista con elementos únicos:")
print(unique_list)