#Elimina libros por su ID
import sqlite3

conn = sqlite3.connect("libreria.db")
cursor = conn.cursor()

# Eliminar libro con ID = 2
cursor.execute("DELETE FROM libros WHERE id = ?", (2,))

conn.commit()
conn.close()
print("Libro eliminado.")
