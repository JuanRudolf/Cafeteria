class Cliente:
    def __init__(self, rut, nombre):
        self.rut = rut
        self.nombre = nombre
        self.compras = []

    def comprar(self, producto):
        self.compras.append(producto)

    def listar_compras(self):
        return [producto.nombre for producto in self.compras]

    def total_gastado(self):
        return sum(producto.precio for producto in self.compras)

    def get_nombre(self):
        return self.nombre


class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.clientes = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def listar_clientes(self):
        return [cliente.nombre for cliente in self.clientes]

    def get_nombre(self):
        return self.nombre


def ejemplo_basico():
    print("=== Cafetería ===")

    # Crear productos
    cafe = Producto(1, "Café Americano", 1500)
    sandwich = Producto(2, "Sándwich de Pollo", 3000)

    # Crear clientes
    pedro = Cliente("11.111.111-1", "Pedro")
    sofia = Cliente("22.222.222-2", "Sofía")

    # Pedro compra café
    pedro.comprar(cafe)
    cafe.agregar_cliente(pedro)

    # Sofía compra café y sándwich
    sofia.comprar(cafe)
    sofia.comprar(sandwich)
    cafe.agregar_cliente(sofia)
    sandwich.agregar_cliente(sofia)

    # Mostrar resultados
    print("Compras de Pedro:", pedro.listar_compras())
    print("Total gastado por Pedro:", pedro.total_gastado())
    print("Clientes que compraron Café:", cafe.listar_clientes())


def menu_principal():
    clientes = {}   # Diccionario: rut -> Cliente
    productos = {}  # Diccionario: codigo -> Producto

    while True:
        print("\n--- MENÚ CAFETERÍA ---")
        print("1. Crear cliente")
        print("2. Crear producto")
        print("3. Registrar compra")
        print("4. Ver compras de un cliente")
        print("5. Ver clientes de un producto")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            rut = input("Ingresa RUT del cliente: ")
            nombre = input("Ingresa nombre: ")
            clientes[rut] = Cliente(rut, nombre)
            print(f"Cliente {nombre} creado")

        elif opcion == "2":
            codigo = int(input("Ingresa código del producto: "))
            nombre = input("Ingresa nombre del producto: ")
            precio = int(input("Ingresa precio del producto: "))
            productos[codigo] = Producto(codigo, nombre, precio)
            print(f"Producto {nombre} creado")

        elif opcion == "3":
            rut = input("RUT del cliente: ")
            codigo = int(input("Código del producto: "))

            if rut in clientes and codigo in productos:
                cliente = clientes[rut]
                producto = productos[codigo]
                cliente.comprar(producto)
                producto.agregar_cliente(cliente)
                print(f"{cliente.nombre} compró {producto.nombre} (${producto.precio})")
            else:
                print("Cliente o producto no encontrado")

        elif opcion == "4":
            rut = input("RUT del cliente: ")
            if rut in clientes:
                cliente = clientes[rut]
                print(f"Compras de {cliente.nombre}:")
                for nombre in cliente.listar_compras():
                    print(f"- {nombre}")
                print(f"Total gastado: ${cliente.total_gastado()}")
            else:
                print("Cliente no encontrado")

        elif opcion == "5":
            codigo = int(input("Código del producto: "))
            if codigo in productos:
                producto = productos[codigo]
                print(f"Clientes que compraron {producto.nombre}:")
                for nombre in producto.listar_clientes():
                    print(f"- {nombre}")
            else:
                print("Producto no encontrado")

        elif opcion == "6":
            print("¡Gracias por visitar la cafetería!")
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    ejemplo_basico()

    print("\n" + "="*40)
    menu_principal()
