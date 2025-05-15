hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# Calcular la hora de finalización
mins += dura
if mins >= 60:
    hour += mins // 60
    mins = mins % 60
if hour >= 24:
    hour = hour % 24
print(f"Hora de finalización: {hour:02d}:{mins:02d}")

 