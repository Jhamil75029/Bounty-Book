#Edita los datos de un libro existente
import sqlite3

def editar_libro(libro_id, nuevo_titulo, nuevo_autor, nuevo_anio):
    conn = sqlite3.connect("libreria.db")
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE libros
    SET titulo = ?, autor = ?, anio = ?
    WHERE id = ?
    """, (nuevo_titulo, nuevo_autor, nuevo_anio, libro_id))

    conn.commit()
    conn.close()
    print(f"Libro ID {libro_id} actualizado.")

# 🔽 EJEMPLO: editar libro con ID 1
editar_libro(1, "El Código Da Vinci (Edición Especial)", "Dan Brown", 2004)
