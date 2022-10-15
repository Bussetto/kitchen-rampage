from pygame import *
from sys import exit
from clases.controles_graficos.controles import Ventana
from clases.controles_graficos.eventos import Evento, Tecla_Presionada, Comando

class Juego:
    def __init__(self, ventana):
        self.__juego_activo = True
        self.__ventana = ventana
        self.__jugador = None
        self.__eventos_admitidos = [MOUSEBUTTONDOWN, KEYDOWN, QUIT]
    
    def iniciar_juego(self):
        #Aparece la intro
        self.mostrar_intro()
        
        init()
        
        while self.__juego_activo:
            for evento_pygame in event.get(self.__eventos_admitidos):
                if evento_pygame.type == QUIT:
                    self.cerrar_juego()
                else:
                    evento_recibido = Evento(evento_pygame.type, evento_pygame)
                    self.__ventana.evaluar_evento(evento_recibido)
            self.__ventana.actualizar()

    def mostrar_intro(self):
        #To do: codear para que se vea el video.
        pass

    def cerrar_juego(self):
        self.__juego_activo = False
        quit()
        exit()

    # vid = Video("Assets/Intro.mp4")
    # vid.set_size((tamaño_pantalla))   

    # def intro():
    #     while True:
    #         vid.draw(pantalla, (0, 0))
    #         pygame.display.update()
    #         if vid.frames == 202:
    #             vid.close()



ventana_nueva = Ventana(800,800)
ventana_nueva.agregar_receptor(Tecla_Presionada(K_F11, ventana_nueva, Comando(ventana_nueva.cambiar_tamaño(1000,1000))))

juego_nuevo = Juego(ventana_nueva)

juego_nuevo.iniciar_juego()