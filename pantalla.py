import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Mario")

clock = pygame.time.Clock()
FPS = 60

""" ancho_personaje = 25
altura_personaje = (ancho_personaje * 1.667) """
personaje = pygame.image.load("recursos/policia_frente.png").convert_alpha()
personaje = pygame.transform.scale(personaje, (100, 100))
personaje_x = int(0.02 * WIDTH)
personaje_y = (HEIGHT - personaje.get_height()) // 2

def limitar_posicion(x, y):
    if x < 0:
        x = 0
    elif x + personaje.get_width() > WIDTH:
        x = WIDTH - personaje.get_width()
    if y < 0:
        y = 0
    elif y + personaje.get_height() > HEIGHT:
        y = HEIGHT - personaje.get_height()
    return x, y

def mover_derecha(x, velocidad):
    x += velocidad
    return x

def mover_izquierda(x, velocidad):
    x -= velocidad
    return x

def cambiar_imagen_derecha():
    global personaje
    personaje = pygame.image.load("recursos/policia_corriendo_derecha.png").convert_alpha()
    personaje = pygame.transform.scale(personaje, (100, 100))

def cambiar_imagen_izquierda():
    global personaje
    personaje = pygame.image.load("recursos/policia_corriendo_izquierda.png").convert_alpha()
    personaje = pygame.transform.scale(personaje, (100, 100))

def manejar_teclas_presionadas(keys, x, velocidad):
    if keys[pygame.K_d]:
        x = mover_derecha(x, velocidad)
        cambiar_imagen_derecha()
    elif keys[pygame.K_a]:
        x = mover_izquierda(x, velocidad)
        cambiar_imagen_izquierda()
    return x

colors = [
    (135, 206, 235),
    (255, 255, 255),
    (34, 139, 34)
]

color_index = 0
running = True

while running:
    dt = clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                color_index = 1 - color_index

    screen.fill(colors[color_index])
    screen.blit(personaje, (personaje_x, personaje_y))
    pygame.display.flip()

    keys = pygame.key.get_pressed()
    velocidad = 5
    personaje_x = manejar_teclas_presionadas(keys, personaje_x, velocidad)
    personaje_x, personaje_y = limitar_posicion(personaje_x, personaje_y)


pygame.quit()
sys.exit()