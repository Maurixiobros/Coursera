import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Crear las tablas desde cero
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Artist (
    id  INTEGER PRIMARY KEY,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER PRIMARY KEY,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER PRIMARY KEY,
    name    TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER PRIMARY KEY,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

handle = open('tracks.csv')

# Procesar el archivo CSV
for line in handle:
    line = line.strip()
    pieces = line.split(',')
    if len(pieces) < 7: continue  # Asegurarse de que haya suficientes columnas

    name = pieces[0]
    artist = pieces[1]
    album = pieces[2]
    genre = pieces[6]  # Extraer el género desde la columna "len"
    count = pieces[3]
    rating = pieces[4]
    length = None  # No hay longitud disponible en este caso

    print(name, artist, album, genre, count, rating)

    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', (artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist,))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', (album, artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album,))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name) 
        VALUES ( ? )''', (genre,))
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre,))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''', 
        (name, album_id, genre_id, length, rating, count))

    conn.commit()

# Bloque de consulta SQL para filtrar y mostrar resultados específicos
print("\nFiltered results:")
cur.execute('''
SELECT Track.title, Artist.name, Album.title, Genre.name
    FROM Track 
    JOIN Genre ON Track.genre_id = Genre.id
    JOIN Album ON Track.album_id = Album.id
    JOIN Artist ON Album.artist_id = Artist.id
    WHERE Artist.name = 'AC/DC' AND Album.title = 'Who Made Who' AND Genre.name = 'Rock'
    ORDER BY Track.title
''')

# Mostrar los resultados de la consulta
for row in cur.fetchall():
    print(f"Track: {row[0]}, Artist: {row[1]}, Album: {row[2]}, Genre: {row[3]}")

# Cerrar la conexión
cur.close()
conn.close()
