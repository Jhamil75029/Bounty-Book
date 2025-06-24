import sqlite3

# Crear una conexión a la base de datos (se crea un archivo si no existe)
conn = sqlite3.connect("libreria.db")

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Crear la tabla de libros
cursor.execute("""
CREATE TABLE IF NOT EXISTS libros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    anio INTEGER,
    genero TEXT
)
""")

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

#print("Base de datos y tabla 'libros' creadas exitosamente.")
