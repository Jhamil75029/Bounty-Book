#Agrega uno o varios libros a la tabla
import sqlite3

def insertar_libro_con_generos(
    titulo, autor, anio, precio, stock, isbn, imagen_url, descripcion, lista_generos
):
    conn = sqlite3.connect("libreria.db")
    cursor = conn.cursor()

    # Insertar el libro
    cursor.execute("""
    INSERT INTO libros (titulo, autor, anio, precio, stock, isbn, imagen_url, descripcion)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (titulo, autor, anio, precio, stock, isbn, imagen_url, descripcion))
    libro_id = cursor.lastrowid

    # Insertar y vincular géneros
    for genero in lista_generos:
        cursor.execute("SELECT id FROM generos WHERE nombre = ?", (genero,))
        resultado = cursor.fetchone()

        if resultado:
            genero_id = resultado[0]
        else:
            cursor.execute("INSERT INTO generos (nombre) VALUES (?)", (genero,))
            genero_id = cursor.lastrowid

        cursor.execute("""
        INSERT OR IGNORE INTO libros_generos (libro_id, genero_id)
        VALUES (?, ?)
        """, (libro_id, genero_id))

    conn.commit()
    conn.close()
    print(f"Libro '{titulo}' agregado correctamente.")

# 🔽 Ejemplo de uso
insertar_libro_con_generos(
    "El Código Da Vinci",
    "Dan Brown",
    2003,
    15.99,
    12,
    "9780307474278",
    "https://miweb.com/imagenes/codigo_da_vinci.jpg",
    "Un thriller de conspiraciones religiosas y arte renacentista.",
    ["Thriller", "Misterio", "Ficción detectivesca"]
)
