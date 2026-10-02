# INCORRECTO: Cada vez que hay un nuevo tipo de cliente, modificamos la función
def calcular_descuento(cliente, precio):
    if cliente == "VIP":
        return precio * 0.8
    elif cliente == "Estudiante":
        return precio * 0.9




# CORRECTO: Usamos clases. Para un nuevo cliente, creamos una clase nueva sin tocar las anteriores
    class Descuento:
        def aplicar(self, precio):

            return precio

    class DescuentoVIP(Descuento):
        def aplicar(self, precio):

            return precio * 0.8

    class DescuentoEstudiante(Descuento):
        def aplicar(self, precio):

            return precio * 0.9