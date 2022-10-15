from pygame import Surface
from pygame.transform import scale as reescalar

class Control(Surface):
    def __init__(self, ancho, alto):
        super().__init__((ancho, alto))
        self._ancho = ancho
        self._alto = alto
        self._receptores_eventos = []
        self._coordenada_x = None
        self._coordenada_y = None

    def cambiar_tamaño(self, ancho, alto):
        reescalar(self, (ancho, alto))
        self._ancho = ancho
        self._alto = alto

    def evaluar_evento(self, evento):
        for receptor in self._receptores_eventos:
            if receptor.codigo == evento.codigo:
                if receptor.validar_emision(evento):
                    receptor.ejecutar_comando()
                    return True
        return False

    def agregar_receptor(self, receptor):
        self._receptores_eventos.append(receptor)

    def agregar_coordenadas(self, coordenada_x, coordenada_y):
        self._coordenada_x = coordenada_x
        self._coordenada_y = coordenada_y

    @property
    def coordenada_x(self):
        return self._coordenada_x

    @property
    def coordenada_y(self):
        return self._coordenada_y

    @property
    def ancho(self):
        return self._ancho

    @property
    def alto(self):
        return self._alto

class Control_Padre(Control):
    def __init__(self, ancho, alto):
        super().__init__(ancho, alto)
        self._controles_hijos = []

    def evaluar_evento(self, evento):
        if not super().evaluar_evento(evento):
            return self.evaluar_evento_en_hijos(evento)
        else:
            return True

    def evaluar_evento_en_hijos(self, evento):
        if self._controles_hijos:
            for control_hijo in self._controles_hijos:
                if control_hijo.evaluar_evento(evento):
                    return True
        return False

    def cambiar_tamaño(self, ancho, alto):
        super().cambiar_tamaño(ancho, alto)
        self.cambiar_tamaño_en_hijos(ancho, alto)

    def calcular_diferencias_tamaño(self, ancho, alto):
        diferencia_ancho = ancho - self._ancho
        diferencia_alto = alto - self._alto
        
        porcentaje_diferencia_ancho = diferencia_ancho * 100 / self._ancho
        porcentaje_diferencia_alto = diferencia_alto * 100 / self._alto

        return [porcentaje_diferencia_ancho, porcentaje_diferencia_alto]

    def cambiar_tamaño_en_hijos(self, ancho, alto):
        if self._controles_hijos:
            porcentajes_diferencia = self.calcular_diferencias_tamaño(ancho, alto)
            porcentaje_diferencia_ancho = porcentajes_diferencia[0]
            porcentaje_diferencia_alto = porcentajes_diferencia[1]

            for control_hijo in self._controles_hijos:
                ancho_nuevo = control_hijo.ancho + control_hijo.ancho * porcentaje_diferencia_ancho / 100
                alto_nuevo = control_hijo.alto + control_hijo.alto * porcentaje_diferencia_alto / 100
                
                control_hijo.cambiar_tamaño(ancho_nuevo, alto_nuevo)

    def agregar_control_hijo(self, control_hijo, coordenada_x, coordenada_y):
        self._controles_hijos.append(control_hijo)
        self.blit(control_hijo, (coordenada_x, coordenada_y))
        control_hijo.agregar_coordenadas(coordenada_x, coordenada_y)