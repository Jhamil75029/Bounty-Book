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

insertar_libro_con_generos(
    "Ángeles y Demonios",
    "Dan Brown",
    2000,
    58,
    501,
    "9788495618719",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlQ5BB9pTVjmd6Dqxh4jN1PvKmIJnJdsn3Yg&s",
    "Robert se enfrenta a los Illuminati",
    ["Misterio", "Suspenso", "Ficción Conspirativa"]
)

insertar_libro_con_generos(
    "Inferno",
    "Dan Brown",
    2013,
    23.99,
    83,
    "9788408176039",
    "https://m.media-amazon.com/images/I/71aUA1-B9aL._UF1000,1000_QL80_.jpg",
    "Inferno es una novela de misterio, ficción y suspenso del escritor estadounidense Dan Brown, basada en la simbología oculta en la Divina Comedia, obra clásica de Dante Alighieri, así como en los problemas de la superpoblación mundial.",
    ["Misterio", "Suspenso", "Thriller", "Novela"]
)

insertar_libro_con_generos(
    "Morir Por Una Tarta De Fresa",
    "Joanne Fluke",
    2025,
    27.87,
    10,
    "9788419599421",
    "https://cdn.prod.website-files.com/6034d7d1f3e0f52c50b2adee/681df46c0ca86ae78febb0b7_fVdDMUhY-ekQ-swylWZ1p3PsFnxRA1THeQKTBsdWdfM.jpeg",
    "Harinas Hartland va a celebrar su primer concurso de repostería en Lake Eden y Hannah, propietaria de The Cookie Jar, es elegida para ser la presidenta del jurado.",
    ["Cozy mystery", "Novela"]
)

insertar_libro_con_generos(
    "El Signo De Los Cuatro",
    "Arthur Conan Doyle",
    1890,
    24.01,
    26,
    "9788499898919",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCbfoNJv2o4Qe7QoGXEmo7DKIdZfVYZM6NGQ&s",
    "El signo de los cuatro es la segunda novela protagonizada por Sherlock Holmes, escrita por Arthur Conan Doyle. Su título también se ha traducido como La señal de los cuatro.",
    ["Novela", "Misterio", "Ficción detectivesca"]
)

insertar_libro_con_generos(
    "El Hombre Invisible",
    "H. G. Wells",
    1897,
    32,
    34,
    "9788466706049",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRol58mdlxPBcSDL-IJs2DbTtHXrSvKqU2j_w&s",
    "El hombre invisible es una novela de ciencia ficción y terror del escritor británico H. G. Wells. La obra fue originalmente publicada en entregas en la revista Pearson's Magazine en 1897 y como novela el mismo año.",
    ["Novela", "Ciencia Ficción", "Terror", "Novela científica"]
)

insertar_libro_con_generos(
    "La Máquina Del Tiempo",
    "H. G. Wells",
    1895,
    54,
    87,
    "9788426140005",
    "https://escritosdeunexabstemio.wordpress.com/wp-content/uploads/2022/12/maquina-del-tiempo-portada.jpg",
    "En un viaje experimental llega al año 802.701 y encuentra la tierra habitada por los Eloi, pacíficos y ociosos. El Viajero del Tiempo deduce que están tan avanzados que unas máquinas deben de trabajar por ellos. Más tarde descubrirá a los malvados y depredadores Morlocks, y habrá de escapar para salvar la vida.",
    ["Novela científica", "Ciencia Ficción", "Ficción distópica", "Literatura fantástica"]
)
