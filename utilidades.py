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
