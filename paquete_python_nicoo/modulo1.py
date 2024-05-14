class Cliente:
    def __init__(self, nombre, email, direccion, telefono):
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f"Nombre: {self.nombre}, Email: {self.email}, Dirección: {self.direccion}, Teléfono: {self.telefono}"

    def actualizar_direccion(self, nueva_direccion):
        self.direccion = nueva_direccion
        print(f"La dirección de {self.nombre} ha sido actualizada a: {nueva_direccion}")

    def realizar_pedido(self, producto, cantidad):
        print(f"{self.nombre} ha realizado un pedido de {cantidad} unidades de {producto}")
