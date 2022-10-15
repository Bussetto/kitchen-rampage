from pygame import SHOWN, display, FULLSCREEN
from .control import Control_Padre
from pygame import display
from pygame.time import Clock

# Nuestra clase Ventana contiene una referencia a la ventana que utiliza pygame para mostrar las cosas.
# Nuestra clase Ventana sería la que manejaría la lógica y la "referencia_ventana_pygame" la que maneja gráficos.

class Ventana(Control_Padre):
    def __init__(self, ancho, alto, pantalla = None):
        super().__init__(ancho, alto)
        self.__referencia_ventana_pygame = display.set_mode((ancho, alto))
        self.__estado_vista = SHOWN        
        self.__FPS = 25
        # self.agregar_control_hijo(pantalla)

    def cambiar_vista(self):
        if self.__estado_vista == SHOWN:
            self.__estado_vista = FULLSCREEN
        else:
            self.__estado_vista = SHOWN

        display.set_mode((self._ancho, self._alto), self.__estado_vista)

    def cambiar_tamaño(self, ancho, alto):
        display.set_mode((ancho, alto), self.__estado_vista)
        self._ancho = ancho
        self._alto = alto

        self.cambiar_tamaño_en_hijos(ancho, alto)

    def cambiar_pantalla(self, pantalla_nueva):
        self._controles_hijos.clear()
        self.agregar_control_hijo(pantalla_nueva)

    def agregar_control_hijo(self, control_hijo):
        self._controles_hijos.append(control_hijo)
        self.__referencia_ventana_pygame.blit(control_hijo , (0, 0))

    def cambiar_fps(self, FPS):
        self.__FPS = FPS

    def actualizar(self):
        Clock().tick(self.__FPS)
        display.update()

    @property
    def FPS(self):
        return self.__FPS

    @property
    def estado_vista(self):
        if self.__estado_vista == SHOWN:
            return "Modo ventana"
        else:
            return "Modo pantalla completa"