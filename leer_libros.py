#Lee y muestra los libros almacenados en la consola
import sqlite3

conn = sqlite3.connect("libreria.db")
cursor = conn.cursor()

cursor.execute("""
SELECT l.id, l.titulo, l.autor, l.anio, l.precio, l.stock, l.isbn, l.imagen_url, l.descripcion,
       GROUP_CONCAT(g.nombre, ', ')
FROM libros l
LEFT JOIN libros_generos lg ON l.id = lg.libro_id
LEFT JOIN generos g ON lg.genero_id = g.id
GROUP BY l.id
""")

libros = cursor.fetchall()

print("📚 LIBROS DISPONIBLES:\n")
for libro in libros:
    print(f"""\
ID: {libro[0]}
Título: {libro[1]}
Autor: {libro[2]}
Año: {libro[3]}
Precio: ${libro[4]:.2f}
Stock: {libro[5]}
ISBN: {libro[6]}
Imagen: {libro[7]}
Descripción: {libro[8]}
Géneros: {libro[9]}
{"-"*50}
""")

conn.close()
