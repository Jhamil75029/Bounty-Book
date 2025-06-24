#Edita los datos de un libro existente
import sqlite3

def editar_libro(libro_id, nuevo_titulo, nuevo_autor, nuevo_anio, nuevo_precio,
                 nuevo_stock, nuevo_isbn, nueva_imagen_url, nueva_descripcion):
    conn = sqlite3.connect("libreria.db")
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE libros
    SET titulo = ?, autor = ?, anio = ?, precio = ?, stock = ?, isbn = ?, imagen_url = ?, descripcion = ?
    WHERE id = ?
    """, (
        nuevo_titulo, nuevo_autor, nuevo_anio, nuevo_precio, nuevo_stock,
        nuevo_isbn, nueva_imagen_url, nueva_descripcion, libro_id
    ))

    conn.commit()
    conn.close()
    print(f"Libro ID {libro_id} actualizado correctamente.")

# 🔽 Ejemplo
editar_libro(
    1,
    "El Código Da Vinci (Edición Especial)",
    "Dan Brown",
    2004,
    18.50,
    8,
    "9780307474278",
    "https://miweb.com/imagenes/codigo_da_vinci_edicion.jpg",
    "Edición especial del exitoso thriller de Dan Brown."
)
