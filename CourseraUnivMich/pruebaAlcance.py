# Este programa explica el alcance de las variables dentro de una función (local) y fuera de ella (global).

# Variable global
global_var = "Soy una variable global"

def mi_funcion():
    # Variable local
    local_var = "Soy una variable local"
    print("Dentro de la función:")
    print(global_var)  # Se puede acceder a la variable global dentro de la función
    print(local_var)   # Se puede acceder a la variable local dentro de la función

# Llamar a la función
mi_funcion()

# Intentar acceder a la variable local fuera de la función
print("\nFuera de la función:")
print(global_var)  # La variable global sigue siendo accesible
try:
    print(local_var)  # Esto generará un error porque local_var no es accesible fuera de la función
except NameError as e:
    print("Error:", e)