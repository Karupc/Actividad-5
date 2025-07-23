ventas = []
while True:
    print("MENÚ DE ANÁLISIS DE VENTAS")
    print("1. Ingresar ventas")
    print("2. Mostrar ventas")
    print("3. Venta más alta y más baja")
    print("4. Promedio de ventas")
    print("5. Días con ventas > Q1000")
    print("6. Clasificar ventas")
    print("7. Salir")
    opcion = input("Ingresa el número de la opción que deseas seleccionar: ")
    match opcion:
        case "1":
            cantidad = int(input("¿Cuántos días desea ingresar?(Ingrese valores enteros positivos): "))
            for i in range(cantidad):
                venta = int(input(f"Ingrese la venta del día {i + 1}: Q"))
                if venta > 0:
                    ventas.append(venta)
                else:
                    print("La venta tiene que ser de algún valor, no se guardó")
        case "2":
            if ventas:
                for i, v in enumerate(ventas, 1):
                    print(f"Día {i}: Q{v}")
            else:
                print("No hay ventas registradas.")
