#Agrega uno o varios libros a la tabla
import sqlite3

conn = sqlite3.connect("libreria.db")
cursor = conn.cursor()

# Inserta un solo libro
cursor.execute("""
INSERT INTO libros (titulo, autor, anio, genero)
VALUES (?, ?, ?, ?)
""", ("Cien años de soledad", "Gabriel García Márquez", 1967, "Realismo mágico"))

# O varios libros a la vez
libros = [
    ("1984", "George Orwell", 1949, "Distopía"),
    ("El Principito", "Antoine de Saint-Exupéry", 1943, "Fábula")
]

cursor.executemany("""
INSERT INTO libros (titulo, autor, anio, genero)
VALUES (?, ?, ?, ?)
""", libros)

conn.commit()
conn.close()
print("Libros insertados.")
