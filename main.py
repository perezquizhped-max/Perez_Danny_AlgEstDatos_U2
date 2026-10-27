# main.py
# Sistema de gestión de una biblioteca - Unidad 2: Diccionarios
# Autor: Danny Marcelo Pérez Quizhpe
# Ejecutar con: python main.py   (o py main.py en Windows)

from utilidades import (
    crear_catalogo_ejemplo,
    registrar_libro,
    buscar_libro,
    catalogo_ordenado,
)


def mostrar_menu():
    print("\n===== BIBLIOTECA =====")
    print("1. Registrar un libro")
    print("2. Buscar un libro por código")
    print("3. Ver catálogo ordenado por código")
    print("0. Salir")


def opcion_registrar(catalogo):
    codigo = input("Código del libro (ej. L006): ").strip().upper()
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    if not codigo or not titulo or not autor:
        print("Todos los datos son obligatorios.")
    elif registrar_libro(catalogo, codigo, titulo, autor):
        print("Libro registrado.")
    else:
        print("Ese código ya existe, no se registró.")


def opcion_buscar(catalogo):
    codigo = input("Código a buscar: ").strip().upper()
    libro = buscar_libro(catalogo, codigo)
    if libro is None:
        print("No existe un libro con ese código.")
    else:
        print(f"{codigo} -> {libro['titulo']} ({libro['autor']})")


def opcion_ordenado(catalogo):
    print("\nCatálogo ordenado por código:")
    for codigo, libro in catalogo_ordenado(catalogo):
        print(f"{codigo} | {libro['titulo']} | {libro['autor']}")


def main():
    catalogo = crear_catalogo_ejemplo()

    while True:
        mostrar_menu()
        opcion = input("Elija una opción: ").strip()
        if opcion == "1":
            opcion_registrar(catalogo)
        elif opcion == "2":
            opcion_buscar(catalogo)
        elif opcion == "3":
            opcion_ordenado(catalogo)
        elif opcion == "0":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
