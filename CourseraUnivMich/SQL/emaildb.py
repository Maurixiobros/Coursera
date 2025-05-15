import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
# Crear la tabla solo si no existe
cur.execute('''
CREATE TABLE IF NOT EXISTS Counts (org TEXT, count INTEGER)''')

# Solicitar el nombre del archivo
fname = input('Enter file name: ')
if (len(fname) < 1): 
    fname = 'mbox.txt'

# Abrir el archivo y procesar las líneas
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): 
        continue
    pieces = line.split()
    email = pieces[1]
    domain = email.split('@')[1]  # Extraer el dominio después del '@'
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (domain,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (domain,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (domain,))
    conn.commit()

# Consultar y mostrar todos los dominios ordenados de mayor a menor
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'

print("\nAll domain counts (ordered by count):")
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

# Consultar y mostrar el dominio con el valor máximo
cur.execute('SELECT org, count FROM Counts ORDER BY count DESC LIMIT 1')
max_row = cur.fetchone()
if max_row:
    print("\nDomain with maximum count:")
    print(str(max_row[0]), max_row[1])

# Cerrar la conexión
cur.close()
conn.close()
