# Biblioteca con diccionarios y conjuntos

Tarea de la Unidad 2 de Algoritmos y Estructuras de Datos (Ciencia de Datos, UPS).

Autor: Danny Marcelo Pérez Quizhpe

## ¿De qué trata?

Es un programa de consola en Python para manejar el catálogo de libros y los préstamos de una biblioteca pequeña. Para hacerlo usé solo el `dict` y el `set` que ya trae Python, que son las estructuras que vimos en la Unidad 2.

## Cómo ejecutarlo

1. Tener Python instalado.
2. Bajar el repositorio (botón verde "Code" y luego "Download ZIP") o clonarlo.
3. Abrir una terminal dentro de la carpeta del proyecto.
4. Escribir:

```
python main.py
```

En Windows a mí me funciona con `py main.py`.

El programa ya trae libros, socios y préstamos de ejemplo, así que se puede probar de una vez sin ingresar nada.

## Archivos

- `main.py`: el menú y lo que se ve en pantalla.
- `utilidades.py`: las funciones de cada requerimiento.

## Qué hace cada requerimiento

**R1 - Catálogo de libros (diccionario).** La clave es el código del libro y el valor es su título y autor. Con la opción 1 se registra un libro y con la opción 2 se busca por código. Como es un diccionario, la búsqueda es inmediata, O(1) en promedio.

**R2 - Catálogo ordenado (TreeMap).** La opción 3 muestra todos los libros ordenados por código. Para esto usé `sorted()`, que cuesta O(n log n). Un TreeMap ya tiene las claves ordenadas desde que se insertan, por eso recorrerlo en orden solo cuesta O(n).

**R3 - Socios registrados (conjunto).** Los identificadores de los socios se guardan en un conjunto. La opción 4 registra un socio y no deja repetirlo, la opción 5 verifica si un identificador ya existe y la opción 6 cuenta cuántos socios hay. Agregar y verificar cuestan O(1) en promedio.

**R4 - Análisis de préstamos (operaciones entre conjuntos).** Hay un conjunto con los socios que sacaron novelas y otro con los que sacaron libros de ciencia. La opción 7 registra un préstamo (solo si el socio ya está registrado) y la opción 8 muestra:

- los socios que leen los dos géneros (intersección),
- los que leen solo novela (diferencia),
- el total de socios distintos con préstamos (unión).

Las tres operaciones cuestan O(n).
