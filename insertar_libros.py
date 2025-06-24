#Agrega uno o varios libros a la tabla
import sqlite3

def insertar_libro_con_generos(titulo, autor, anio, lista_generos):
    conn = sqlite3.connect("libreria.db")
    cursor = conn.cursor()

    # Insertar el libro
    cursor.execute("""
    INSERT INTO libros (titulo, autor, anio)
    VALUES (?, ?, ?)
    """, (titulo, autor, anio))
    libro_id = cursor.lastrowid

    for genero in lista_generos:
        # Verificar si el género ya existe
        cursor.execute("SELECT id FROM generos WHERE nombre = ?", (genero,))
        resultado = cursor.fetchone()

        if resultado:
            genero_id = resultado[0]
        else:
            cursor.execute("INSERT INTO generos (nombre) VALUES (?)", (genero,))
            genero_id = cursor.lastrowid

        # Relacionar libro con género
        cursor.execute("""
        INSERT OR IGNORE INTO libros_generos (libro_id, genero_id)
        VALUES (?, ?)
        """, (libro_id, genero_id))

    conn.commit()
    conn.close()
    print(f"Libro '{titulo}' agregado con sus géneros.")

# 🔽 EJEMPLOS
insertar_libro_con_generos("El Código Da Vinci", "Dan Brown", 2003, ["Novela", "Thriller", "Misterio", "Ficción detectivesca"])
insertar_libro_con_generos("Harry Potter y la piedra filosofal", "J.K. Rowling", 1997, ["Fantasía", "Aventura", "Juvenil"])
