from paquete_python_nicoo.modulo1 import Cliente
from paquete_python_nicoo.modulo2 import *

cliente1 = Cliente("Nicolas","nicobotta@gmial.com","algun lugar","1233523")

print(cliente1)

cliente1.actualizar_direccion("Pehuajo, Bs As")
print(cliente1)
cliente1.realizar_pedido("celulares","30")