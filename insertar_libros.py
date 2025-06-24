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

insertar_libro_con_generos(
    "El Símbolo Perdido",
    "Dan Brown",
    2009,
    30.00,
    75,
    "9788408176015",
    "https://proassetspdlcom.cdnstatics2.com/usuaris/libros/fotos/10/original/portada_el-simbolo-perdido_dan-brown_201505260959.jpg",
    "Robert se encuentra con la masonería",
    ["Thriller", "Misterio", "Ficción detectivesca"]
)

insertar_libro_con_generos(
    "El Origen",
    "Dan Brown",
    2017,
    27.78,
    29,
    "9788408177081",
    "https://pictures.abebooks.com/isbn/9789584261625-us.jpg",
    "Robert Langdon descubre que el big bang es posible",
    ["Thriller", "Misterio", "Ficción detectivesca"]
)

insertar_libro_con_generos(
    "Unas Galletitas de Muerte",
    "Joanne Fluke",
    2024,
    20,
    755,
    "9788418933615",
    "https://m.media-amazon.com/images/I/71QlSSLKJCL.jpg",
    "Hannah está ocupada intentado esquivar los intentos de su madre por casarla mientras dirige la panadería más popular de Lake Eden. Pero cuando encuentran a Ron LaSalle, el querido repartidor de periódicos muerto en la parte trasera de su panadería, su vida ya no puede ir a peor.",
    ["Cozy mystery", "Terror", "Suspenso", "Misterio"]
)
