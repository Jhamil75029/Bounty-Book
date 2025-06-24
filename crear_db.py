import sqlite3

conn = sqlite3.connect("libreria.db")
cursor = conn.cursor()

# Crear tabla de libros
cursor.execute("""
CREATE TABLE IF NOT EXISTS libros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    anio INTEGER,
    precio REAL,
    stock INTEGER,
    isbn TEXT,
    imagen_url TEXT,
    descripcion TEXT
)
""")

# Crear tabla de géneros
cursor.execute("""
CREATE TABLE IF NOT EXISTS generos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT UNIQUE NOT NULL
)
""")

# Crear tabla puente libros-generos
cursor.execute("""
CREATE TABLE IF NOT EXISTS libros_generos (
    libro_id INTEGER,
    genero_id INTEGER,
    FOREIGN KEY (libro_id) REFERENCES libros(id),
    FOREIGN KEY (genero_id) REFERENCES generos(id),
    PRIMARY KEY (libro_id, genero_id)
)
""")

conn.commit()
conn.close()
print("Base de datos y tablas creadas correctamente.")
