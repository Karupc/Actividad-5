while True:
print("\n--MENÚ DE ANÁLISIS DE VENTA--")
opciones = input(f"1. Ingresar lista de ventas (valores enteros positivos)\n2. Mostrar todas las ventas ingresadas\n3. Calcular la venta más alta y la más baja\n4. Calcular promedio de ventas\n5. Contar cuántos días superaron los Q1000\n6. Buscar si una venta específica existe en la lista\n7. Clasificar cada venta: alta (>1000), media (500–1000), baja (<500)\n8. Salir\nIngrese el número de la opción que desea seleccionar: ")
match opciones:
    case "1":
        ventas = int(input("Ingrese el número de ventas que desea agregar: "))
        ventass = []
        for i in range(ventas):
            producto = input("Ingrese el producto")
            venta = int(input("Ingrese eL valor de la venta en enteros positivos: Q"))
            ventass.appent(producto, venta)