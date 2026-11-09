from src.database import inicializar_base_datos, conectar

def mostrar_menu():
    print("\n==================================================")
    print("   SGI-VENTAS - PRIMER AVANCE (UGB)")
    print("==================================================")
    print("1. Registrar producto")
    print("2. Ver inventario")
    print("3. Salir")

def registrar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    try:
        precio = float(input("Ingrese el precio ($): "))
        stock = int(input("Ingrese la cantidad en stock: "))
        
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)", (nombre, precio, stock))
        conexion.commit()
        conexion.close()
        print("Producto registrado con exito.")
    except ValueError:
        print("Error: Ingrese valores numericos validos.")

def ver_inventario():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conexion.close()
    
    print("\n--- INVENTARIO ACTUAL ---")
    if not productos:
        print("No hay productos registrados.")
    for p in productos:
        print(f"ID: {p[0]} | Producto: {p[1]} | Precio: ${p[2]:.2f} | Stock: {p[3]} unidades")

def main():
    inicializar_base_datos()
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opcion: ")
        
        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            ver_inventario()
        elif opcion == "3":
            print("\nSaliendo del prototipo. Hasta luego!")
            break
        else:
            print("Opcion invalida.")

if __name__ == "__main__":
    main()