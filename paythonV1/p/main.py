import json

productos = []
ARCHIVO = "productos.json"

# FUNCIONES DE FORMATO


def formato_precio(valor):
    """Convierte un número a formato colombiano con puntos."""
    return f"${valor:,.0f}".replace(",", ".")


def mostrar_tabla(lista):
    """Muestra los productos organizados en una tabla."""

    if not lista:
        print("\nNo hay productos para mostrar.")
        return

    print("#==========================================================================================#")
    print("#                                   PRODUCTOS AGROCBA                                      #")
    print("#==========================================================================================#")

    print(
        f"{'Código':<10}"
        f"{'Nombre':<22}"
        f"{'Categoría':<18}"
        f"{'Cantidad':>10}"
        f"{'Precio':>14}"
    )

    print("#==========================================================================================#")

    for producto in lista:
        print(
            f"{producto['codigo']:<10}"
            f"{producto['nombre']:<22}"
            f"{producto['categoria']:<18}"
            f"{producto['cantidad']:>10}"
            f"{formato_precio(producto['precio']):>14}"
        )

    print("#==========================================================================================#")


# MENÚ


def mostrar_menu():
    print("=====================================================")
    print("agrocba tiendita")
    print("=====================================================")
    print("1. Registrar producto")
    print("2. Consultar productos")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("=====================================================")
    print("6. Mostrar valor total del inventario")
    print("7. Mostrar cantidad total de unidades")
    print("8. Mostrar producto con mayor precio")
    print("9. Mostrar producto con mayor cantidad")
    print("10. Consultar productos por categoría")
    print("=====================================================")
    print("11. Ordenar productos alfabéticamente")
    print("12. Mostrar productos con bajo inventario")
    print("13. Guardar datos en JSON")
    print("14. Cargar datos desde JSON")
    print("15. Salir")
    print("=====================================================")
# REGISTRAR PRODUCTO


def registrar_producto():

    print("\n--- REGISTRAR PRODUCTO ---")

    codigo = input("Código: ").strip()

    if codigo == "":
        print("no puedesestar basio invalido.")
        return

    for producto in productos:
        if producto["codigo"].lower() == codigo.lower():
            print("el codigo no se puede duplicar.")
            return

    nombre = input("Nombre: ").strip()

    if nombre == "":
        print("el nombre no puede estar vacio")
        return

    categoria = input("Categoría: ").strip()

    if categoria == "":
        print("sin categoria no valida.")
        return

    try:
        cantidad = int(input("Cantidad: "))

        if cantidad < 0:
            print("la cantidad es negativa invalido.")
            return

    except ValueError:
        print("La cantidad debe ser un número entero.")
        return

    try:
        precio = float(input("Precio: "))

        if precio <= 0:
            print("El precio debe ser mayor que 0.")
            return

    except ValueError:
        print("El precio debe ser un número válido.")
        return

    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "cantidad": cantidad,
        "precio": precio
    }

    productos.append(producto)

    print("\n Producto registrado exitosamente.")
    mostrar_tabla([producto])




def consultar_productos():
    print("\n--- CONSULTAR PRODUCTOS ---")
    mostrar_tabla(productos)


def buscar_producto():

    print("\n--- BUSCAR PRODUCTO ---")

    codigo = input("Ingrese el código del producto: ").strip()

    for producto in productos:

        if producto["codigo"].lower() == codigo.lower():

            print("\n Producto encontrado:")
            mostrar_tabla([producto])
            return

    print(" Producto no encontrado.")


def actualizar_producto():

    print("\n--- ACTUALIZAR PRODUCTO ---")

    codigo = input("Ingrese el código del producto: ").strip()

    for producto in productos:

        if producto["codigo"].lower() == codigo.lower():

            print("\nProducto actual:")
            mostrar_tabla([producto])

            print("\nIngrese los nuevos datos.")

            nombre = input("Nuevo nombre: ").strip()

            if nombre == "":
                print(" El nombre no puede estar vacío.")
                return

            categoria = input("Nueva categoría: ").strip()

            if categoria == "":
                print(" La categoría no puede estar vacía.")
                return

            try:
                cantidad = int(input("Nueva cantidad: "))

                if cantidad < 0:
                    print(" La cantidad no puede ser negativa.")
                    return

            except ValueError:
                print(" La cantidad debe ser un número entero.")
                return

            try:
                precio = float(input("Nuevo precio: "))

                if precio <= 0:
                    print(" El precio debe ser mayor que 0.")
                    return

            except ValueError:
                print(" El precio debe ser un número válido.")
                return

            producto["nombre"] = nombre
            producto["categoria"] = categoria
            producto["cantidad"] = cantidad
            producto["precio"] = precio

            print("\n✅ Producto actualizado correctamente.")
            mostrar_tabla([producto])
            return

    print(" Producto no encontrado.")

def eliminar_producto():

    print("\n--- ELIMINAR PRODUCTO ---")

    codigo = input("Ingrese el código del producto: ").strip()

    for producto in productos:

        if producto["codigo"].lower() == codigo.lower():

            mostrar_tabla([producto])

            confirmar = input(
                "\n¿Está seguro de eliminar este producto? (s/n): "
            ).lower()

            if confirmar == "s":

                productos.remove(producto)

                print("\n Producto eliminado exitosamente.")

            else:

                print("\n Eliminación cancelada.")

            return

    print(" no c encontro el producto.")



def calcular_inventario():

    print("\n--- VALOR TOTAL DEL INVENTARIO ---")

    total = 0

    for producto in productos:
        total += producto["cantidad"] * producto["precio"]

    print("\n Valor total en el inventario:")
    print(f"   {formato_precio(total)}")




def cantidad_total_unidades():

    print("\n--- TOTAL DE UNIDADES ---")

    total = 0

    for producto in productos:
        total += producto["cantidad"]

    print(f"\n Cantidad total de unidades: {total}")




def producto_mayor_precio():

    print("\n--- PRODUCTO CON MAYOR PRECIO ---")

    if not productos:
        print(" No hay productos registrados.")
        return

    mayor = productos[0]

    for producto in productos:

        if producto["precio"] > mayor["precio"]:
            mayor = producto

    mostrar_tabla([mayor])


def producto_mayor_cantidad():

    print("\n--- PRODUCTO CON MAYOR CANTIDAD ---")

    if not productos:
        print(" No hay productos registrados.")
        return

    mayor = productos[0]

    for producto in productos:

        if producto["cantidad"] > mayor["cantidad"]:
            mayor = producto

    mostrar_tabla([mayor])



def consultar_por_categoria():

    print("\n--- CONSULTAR POR CATEGORÍA ---")

    categoria = input("Ingrese la categoría: ").strip()

    encontrados = []

    for producto in productos:

        if producto["categoria"].lower() == categoria.lower():
            encontrados.append(producto)

    if encontrados:
        mostrar_tabla(encontrados)
    else:
        print(" No se encontraron productos de esa categoría.")



def ordenar_productos():

    print("\n--- PRODUCTOS ORDENADOS ALFABÉTICAMENTE ---")

    ordenados = sorted(
        productos,
        key=lambda producto: producto["nombre"].lower()
    )

    mostrar_tabla(ordenados)


def bajo_inventario():

    print("\n--- PRODUCTOS CON BAJO INVENTARIO ---")
    print("Productos con cantidad menor o igual a 5.")

    bajos = []

    for producto in productos:

        if producto["cantidad"] <= 5:
            bajos.append(producto)

    if bajos:
        mostrar_tabla(bajos)
    else:
        print("\n No hay productos con bajo inventario.")


def guardar_json():

    try:

        with open(ARCHIVO, "w", encoding="utf-8") as archivo:

            json.dump(
                productos,
                archivo,
                indent=4,
                ensure_ascii=False
            )

        print("\n Datos guardados correctamente en productos.json.")

    except Exception as error:

        print(f"\n Error al guardar los datos: {error}")

def cargar_json():

    global productos

    try:

        with open(ARCHIVO, "r", encoding="utf-8") as archivo:

            productos = json.load(archivo)

        print("\n Datos cargados correctamente.")

    except FileNotFoundError:

        print("\n No existe un archivo de datos todavía.")
        print("Se comenzará con el inventario vacío.")

    except json.JSONDecodeError:

        print("\n El archivo productos.json está dañado.")

    except Exception as error:

        print(f"\n hay un error en la carga de los datos: {error}")



def main():

    while True:

        mostrar_menu()

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_producto()

        elif opcion == "2":
            consultar_productos()

        elif opcion == "3":
            buscar_producto()

        elif opcion == "4":
            actualizar_producto()

        elif opcion == "5":
            eliminar_producto()

        elif opcion == "6":
            calcular_inventario()

        elif opcion == "7":
            cantidad_total_unidades()

        elif opcion == "8":
            producto_mayor_precio()

        elif opcion == "9":
            producto_mayor_cantidad()

        elif opcion == "10":
            consultar_por_categoria()

        elif opcion == "11":
            ordenar_productos()

        elif opcion == "12":
            bajo_inventario()

        elif opcion == "13":
            guardar_json()

        elif opcion == "14":
            cargar_json()

        elif opcion == "15":
            print("\n Gracias por utilizar AgroCBA.")
            break

        else:
            print("\n Opción inválida. Intente nuevamente.")



if __name__ == "__main__":
    main()