#INCORRECTO: la clase maneja los datos y se encarga de guardarlos
class Reporte:
    def __init__(self, contenido):
        self.contenido = contenido

    def guardar_en_archivo(self, ruta):
         with open(ruta, "w") as f:
                f.write(self.contenido)


#CORRECTO: separamos la estructura del reporte de la logica de guardado
class Reporte:
    def __init__(self, contenido):
        self.contenido = contenido

class GuardadorReporte:
    def guardar(self, reporte: Reporte, ruta: str):
        with open(ruta, "w") as f:
                f.write(reporte.contenido)

