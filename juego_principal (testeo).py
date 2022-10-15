import pygame
from pygame import *

fps = 60
pygame.init()


info = pygame.display.Info()
w = info.current_w
h = info.current_h

ventana = pygame.display.set_mode((info.current_w, info.current_h-50), RESIZABLE)


color_principal = "#fff4bf"



# pantalla_principal = pygame.Surface((infoObject.current_w, infoObject.current_h))
# pantalla_principal.fill(color_principal)

# ventana = pygame.display.set_mode((width, height))

imagen = pygame.image.load("Kitchen Rampage_V0.0.4a/recursos/imagenes/kitchen-rampage-logo.png")
pygame.transform.scale(imagen, (500,500))
# imagen = pygame.transform.scale(imagen, (500, 500))
# pantalla_principal.blit(imagen, (0, 0))
ventana.blit(imagen, (0,0))
activo = True

reloj = pygame.time.Clock()

# rectangulo = pygame.draw.
pantalla_completa = True

while activo:
    for evento in pygame.event.get([MOUSEBUTTONDOWN, QUIT]):
        print(evento.type)
        if evento.type == pygame.QUIT:
            activo = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print(evento.pos[0], evento.pos[1])
        if evento.type == pygame.KEYDOWN:
            tecla = evento.key
            if evento.key == K_F11:
                pantalla_completa = not pantalla_completa            
                if pantalla_completa:
                    ventana = pygame.display.set_mode((info.current_w, info.current_h), FULLSCREEN)
                else:
                    ventana = pygame.display.set_mode((info.current_w, info.current_h-50), RESIZABLE)
        print(evento)
    pygame.display.update()

    reloj.tick(fps)

pygame.quit()