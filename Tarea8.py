# Clase Producto
class Producto:
    def __init__(self, pid: int, nombre: str, precio: float):
        self.id = pid          # identificador único
        self.nombre = nombre   # nombre del producto
        self.precio = precio   # precio del producto

    def __str__(self):
        # cómo se muestra el producto al imprimirlo
        return f"ID {self.id} | {self.nombre} | ${self.precio:.2f}"


# Clase GestorProductos para CRUD
class GestorProductos:
    def __init__(self):
        self.productos = []   # lista donde se guardan los productos
        self.next_id = 1      # contador de IDs

    # Crear producto
    def crear(self, nombre: str, precio: float):
        producto = Producto(self.next_id, nombre, precio)
        self.productos.append(producto)
        self.next_id += 1
        print("✔ Producto registrado.")

    # Listar productos
    def listar(self):
        if not self.productos:
            print("(No hay productos registrados)")
        for p in self.productos:
            print(p)

    # Editar producto por ID
    def editar(self, pid: int, nuevo_nombre: str, nuevo_precio: float):
        for p in self.productos:
            if p.id == pid:
                p.nombre = nuevo_nombre
                p.precio = nuevo_precio
                print("✔ Producto actualizado.")
                return
        print("✘ Producto no encontrado.")

    # Eliminar producto por ID
    def eliminar(self, pid: int):
        for p in self.productos:
            if p.id == pid:
                self.productos.remove(p)
                print("✔ Producto eliminado.")
                return
        print("✘ Producto no encontrado.")

# Clase principal con menú
class App:
    def __init__(self):
        self.gestor = GestorProductos()

    def run(self):
        while True:
            print("\n--- Menú de Productos ---")
            print("1) Registrar producto")
            print("2) Listar productos")
            print("3) Editar producto")
            print("4) Eliminar producto")
            print("0) Salir")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                nombre = input("Nombre: ")
                precio = float(input("Precio: "))
                self.gestor.crear(nombre, precio)

            elif opcion == "2":
                self.gestor.listar()

            elif opcion == "3":
                pid = int(input("N° de ID a editar: "))
                nombre = input("Nuevo nombre: ")
                precio = float(input("Nuevo precio: "))
                self.gestor.editar(pid, nombre, precio)

            elif opcion == "4":
                pid = int(input("N° de ID a eliminar: "))
                self.gestor.eliminar(pid)

            elif opcion == "0":
                print("Salida exitosa")
                break

            else:
                print("Opción inválida.")


# Ejecutar aplicación
if __name__ == "__main__":
    App().run()
