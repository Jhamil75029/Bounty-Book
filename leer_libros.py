#Lee y muestra los libros almacenados en la consola
import sqlite3

conn = sqlite3.connect("libreria.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM libros")
libros = cursor.fetchall()

for libro in libros:
    print(f"ID: {libro[0]} | Título: {libro[1]} | Autor: {libro[2]} | Año: {libro[3]} | Género: {libro[4]}")

conn.close()
