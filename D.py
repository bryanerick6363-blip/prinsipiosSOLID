# INCORRECTO: Notificador depende directamente de ServicioSMS
class ServicioSMS:
    def enviar(self, msg): print(f"SMS: {msg}")

class Notificador:
    def __init__(self):
        self.sms = ServicioSMS() # Acoplamiento directo




# CORRECTO: Notificador depende de una abstracción (ServicioMensaje)
class ServicioMensaje(ABC):
    @abstractmethod
    def enviar(self, msg): pass

class ServicioSMS(ServicioMensaje):
    def enviar(self, msg): print(f"SMS: {msg}")

class ServicioEmail(ServicioMensaje):
    def enviar(self, msg): print(f"Email: {msg}")

class Notificador:
    def __init__(self, servicio: ServicioMensaje): # Inyección de dependencia
        self.servicio = servicio
    def enviar_alerta(self, msg):
        self.servicio.enviar(msg)