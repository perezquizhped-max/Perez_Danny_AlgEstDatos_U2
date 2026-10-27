# main.py
# Sistema de gestión de una biblioteca - Unidad 2: Diccionarios
# Autor: Danny Marcelo Pérez Quizhpe
# Ejecutar con: python main.py   (o py main.py en Windows)

from utilidades import (
    crear_catalogo_ejemplo,
    registrar_libro,
    buscar_libro,
    catalogo_ordenado,
    crear_socios_ejemplo,
    registrar_socio,
    socio_registrado,
    crear_prestamos_ejemplo,
    registrar_prestamo,
    socios_ambos_generos,
    socios_solo_novela,
    socios_con_prestamos,
)


def mostrar_menu():
    print("\n===== BIBLIOTECA =====")
    print("1. Registrar un libro")
    print("2. Buscar un libro por código")
    print("3. Ver catálogo ordenado por código")
    print("4. Registrar un socio")
    print("5. Verificar si un socio está registrado")
    print("6. Ver cuántos socios hay")
    print("7. Registrar un préstamo")
    print("8. Análisis de préstamos")
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


def opcion_registrar_socio(socios):
    id_socio = input("Identificador del socio (ej. S006): ").strip().upper()
    if not id_socio:
        print("El identificador no puede estar vacío.")
    elif registrar_socio(socios, id_socio):
        print("Socio registrado.")
    else:
        print("Ese socio ya estaba registrado, no se duplicó.")


def opcion_verificar_socio(socios):
    id_socio = input("Identificador a verificar: ").strip().upper()
    if socio_registrado(socios, id_socio):
        print("Sí, ese socio está registrado.")
    else:
        print("No, ese socio no está registrado.")


def opcion_contar_socios(socios):
    print(f"Hay {len(socios)} socios registrados.")


def opcion_registrar_prestamo(socios, novela, ciencia):
    id_socio = input("Identificador del socio: ").strip().upper()
    genero = input("Género (novela o ciencia): ").strip().lower()
    resultado = registrar_prestamo(socios, novela, ciencia, id_socio, genero)
    if resultado == "ok":
        print("Préstamo registrado.")
    elif resultado == "no_socio":
        print("Ese socio no está registrado. Regístrelo primero (opción 4).")
    else:
        print("El género debe ser novela o ciencia.")


def opcion_analisis(novela, ciencia):
    print("\nAnálisis de préstamos:")
    print("Leen novela y ciencia:", sorted(socios_ambos_generos(novela, ciencia)))
    print("Leen solo novela:", sorted(socios_solo_novela(novela, ciencia)))
    total = socios_con_prestamos(novela, ciencia)
    print(f"Total de socios con préstamos: {len(total)} -> {sorted(total)}")


def main():
    catalogo = crear_catalogo_ejemplo()
    socios = crear_socios_ejemplo()
    novela, ciencia = crear_prestamos_ejemplo()

    while True:
        mostrar_menu()
        opcion = input("Elija una opción: ").strip()
        if opcion == "1":
            opcion_registrar(catalogo)
        elif opcion == "2":
            opcion_buscar(catalogo)
        elif opcion == "3":
            opcion_ordenado(catalogo)
        elif opcion == "4":
            opcion_registrar_socio(socios)
        elif opcion == "5":
            opcion_verificar_socio(socios)
        elif opcion == "6":
            opcion_contar_socios(socios)
        elif opcion == "7":
            opcion_registrar_prestamo(socios, novela, ciencia)
        elif opcion == "8":
            opcion_analisis(novela, ciencia)
        elif opcion == "0":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
