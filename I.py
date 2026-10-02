from abc import ABC, abstractmethod
# INCORRECTO: Obligamos a una impresora sencilla a implementar el escáner
class Dispositivo(ABC):
    @abstractmethod
    def imprimir(self): pass
    @abstractmethod
    def escanear(self): pass




# CORRECTO: Dividimos en interfaces independientes usando clases abstractas
class Impresora(ABC):
    @abstractmethod
    def imprimir(self): pass

class Escaner(ABC):
    @abstractmethod
    def escanear(self): pass

    class ImpresoraSencilla(Impresora):
        def imprimir(self):
            print("Imprimiendo documento...")