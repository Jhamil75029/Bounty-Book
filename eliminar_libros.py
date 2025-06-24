#Elimina libros por su ID
import sqlite3

def eliminar_libro(libro_id):
    conn = sqlite3.connect("libreria.db")
    cursor = conn.cursor()

    # Eliminar relaciones con géneros primero
    cursor.execute("DELETE FROM libros_generos WHERE libro_id = ?", (libro_id,))

    # Luego eliminar el libro
    cursor.execute("DELETE FROM libros WHERE id = ?", (libro_id,))

    conn.commit()
    conn.close()
    print(f"Libro ID {libro_id} eliminado correctamente.")

# 🔽 Ejemplo
eliminar_libro(1)
