# utilidades.py
# Funciones auxiliares de la biblioteca (Unidad 2: diccionarios y conjuntos)


# ---------- R1: Catálogo de libros (diccionario / HashMap) ----------
# La clave es el código del libro y el valor es otro diccionario
# con el título y el autor.

def crear_catalogo_ejemplo():
    """Devuelve un catálogo con algunos libros de ejemplo."""
    return {
        "L003": {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"},
        "L001": {"titulo": "Huasipungo", "autor": "Jorge Icaza"},
        "L005": {"titulo": "El principito", "autor": "Antoine de Saint-Exupéry"},
        "L002": {"titulo": "Introducción a los algoritmos", "autor": "Thomas Cormen"},
        "L004": {"titulo": "Cosmos", "autor": "Carl Sagan"},
    }


def registrar_libro(catalogo, codigo, titulo, autor):
    """Registra un libro. Devuelve False si el código ya existe."""
    # registrar (put): O(1) promedio
    if codigo in catalogo:  # in: O(1) promedio
        return False
    catalogo[codigo] = {"titulo": titulo, "autor": autor}
    return True


def buscar_libro(catalogo, codigo):
    """Busca un libro por su código. Devuelve None si no existe."""
    # buscar (get): O(1) promedio
    return catalogo.get(codigo)


# ---------- R2: Catálogo ordenado (TreeMap) ----------

def catalogo_ordenado(catalogo):
    """Devuelve la lista de (código, info) ordenada por código."""
    # ordenar con sorted(): O(n log n)
    # Un TreeMap (SortedDict) ya mantiene las claves ordenadas al insertar,
    # por eso recorrerlo en orden cuesta solo O(n).
    return sorted(catalogo.items())


# ---------- R3: Socios registrados (conjunto / HashSet) ----------
# Un conjunto no admite repetidos, así que un socio no se puede
# registrar dos veces con el mismo identificador.

def crear_socios_ejemplo():
    """Devuelve un conjunto con algunos identificadores de socios."""
    return {"S001", "S002", "S003", "S004", "S005"}


def registrar_socio(socios, id_socio):
    """Registra un socio. Devuelve False si ya estaba registrado."""
    # verificar con in: O(1) promedio
    if id_socio in socios:
        return False
    # agregar con add: O(1) promedio
    socios.add(id_socio)
    return True


def socio_registrado(socios, id_socio):
    """Dice al instante si un identificador ya está registrado."""
    # pertenencia con in: O(1) promedio
    return id_socio in socios


# ---------- R4: Análisis de préstamos (operaciones entre conjuntos) ----------
# Hay un conjunto con los socios que sacaron novelas y otro con los
# que sacaron libros de ciencia.

def crear_prestamos_ejemplo():
    """Devuelve (socios con novela, socios con ciencia) de ejemplo."""
    novela = {"S001", "S002", "S003"}
    ciencia = {"S003", "S004"}
    return novela, ciencia


def registrar_prestamo(socios, novela, ciencia, id_socio, genero):
    """Registra un préstamo si el socio existe. Devuelve un texto con el resultado."""
    # verificar que el socio exista: O(1) promedio
    if id_socio not in socios:
        return "no_socio"
    # agregar al conjunto del género: O(1) promedio
    if genero == "novela":
        novela.add(id_socio)
    elif genero == "ciencia":
        ciencia.add(id_socio)
    else:
        return "genero_invalido"
    return "ok"


def socios_ambos_generos(novela, ciencia):
    """Socios que leen novela y también ciencia (intersección)."""
    # intersección: O(n)
    return novela & ciencia


def socios_solo_novela(novela, ciencia):
    """Socios que leen solo novela (diferencia)."""
    # diferencia: O(n)
    return novela - ciencia


def socios_con_prestamos(novela, ciencia):
    """Todos los socios distintos que tienen préstamos (unión)."""
    # unión: O(n)
    return novela | ciencia
