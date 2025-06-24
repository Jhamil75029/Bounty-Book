#Edita los datos de un libro existente
import sqlite3

conn = sqlite3.connect("libreria.db")
cursor = conn.cursor()

# Cambiar título del libro con ID = 1
cursor.execute("""
UPDATE libros
SET titulo = ?
WHERE id = ?
""", ("Cien años de soledad (Edición revisada)", 1))

conn.commit()
conn.close()
print("Libro actualizado.")
