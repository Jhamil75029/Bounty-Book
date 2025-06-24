#Lee y muestra los libros almacenados en la consola
import sqlite3

conn = sqlite3.connect("libreria.db")
cursor = conn.cursor()

# Obtener todos los libros
cursor.execute("""
SELECT l.id, l.titulo, l.autor, l.anio, GROUP_CONCAT(g.nombre, ', ')
FROM libros l
LEFT JOIN libros_generos lg ON l.id = lg.libro_id
LEFT JOIN generos g ON lg.genero_id = g.id
GROUP BY l.id
""")

libros = cursor.fetchall()

print("📚 LIBROS REGISTRADOS:\n")
for libro in libros:
    print(f"ID: {libro[0]} | Título: {libro[1]} | Autor: {libro[2]} | Año: {libro[3]} | Géneros: {libro[4]}")

conn.close()
