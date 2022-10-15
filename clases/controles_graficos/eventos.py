from abc import ABC, abstractmethod
from pygame import KEYDOWN, MOUSEBUTTONDOWN

class Comando():
    def __init__(self, funcion):
        self.ejecutar = funcion

    def ejecutar(self):
        pass

class Evento():
    def __init__(self, codigo, informacion):        
        self.__codigo = codigo
        self.__informacion = informacion

    @property
    def codigo(self):
        return self.__codigo

    @property
    def informacion(self):
        return self.__informacion

# El objeto Evento se envía al Receptor_Evento y se verifica a través del método 
# validar_emision() de este último.

class Receptor_Evento(ABC):
    def __init__(self, emisor, comando):
        self.__emisor = emisor
        self.__comando = comando

    @property
    def codigo(self):
        pass

    @abstractmethod
    def validar_emision(self, evento):
        pass

    def ejecutar_comando(self):
        self.__comando.ejecutar()

class Click(Receptor_Evento):
    def __init__(self, emisor, comando):
        super().__init__(emisor, comando)
        
    @property
    def codigo(self):
        return MOUSEBUTTONDOWN

    def validar_emision(self, evento):
        click_posicion_x, click_posicion_y = evento.informacion.pos[0], evento.informacion.pos[1]
        
        # Declaramos variables para cada lado del control para que sea más legible.
        control_lado_izquierdo = self.__emisor.coordenada_x
        control_lado_derecho = control_lado_izquierdo + self.__emisor.ancho

        control_lado_superior = self.__emisor.coordenada_y
        control_lado_inferior = control_lado_superior + self.__emisor.alto

        # Se valida si las coordenadas del click están dentro del area del control.
        if control_lado_izquierdo < click_posicion_x < control_lado_derecho and control_lado_superior < click_posicion_y < control_lado_inferior:
            return True
        return False

class Tecla_Presionada(Receptor_Evento):
    def __init__(self, codigo_tecla, emisor, comando):
        super().__init__(emisor, comando)
        self.__codigo_tecla = codigo_tecla
    
    @property
    def codigo(self):
        return KEYDOWN

    def validar_emision(self, evento):
        if evento.informacion.key == self.__codigo_tecla:
            return True      
        return False