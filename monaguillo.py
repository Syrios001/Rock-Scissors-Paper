import pygame
import random

# Inicialización de Pygame
pygame.init()

# Definir dimensiones de la pantalla
ANCHO = 800
ALTO = 600
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Monaguillos vs Brujas")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)

# Clases de personajes
class Monaguillo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = ALTO // 2
        self.velocidad = 5

    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP]:
            self.rect.y -= self.velocidad
        if teclas[pygame.K_DOWN]:
            self.rect.y += self.velocidad
        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.velocidad
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidad

    def ataque(self):
        proyectil = Proyectil(self.rect.centerx, self.rect.top)
        todos_los_sprites.add(proyectil)
        proyectiles.add(proyectil)

class Bruja(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(ANCHO // 2, ANCHO - 50)
        self.rect.y = random.randint(0, ALTO - 50)
        self.velocidad = random.randint(1, 3)

    def update(self):
        self.rect.x -= self.velocidad
        if self.rect.right < 0:
            self.rect.x = ANCHO
            self.rect.y = random.randint(0, ALTO - 50)

class Proyectil(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocidad = 10

    def update(self):
        self.rect.x += self.velocidad
        if self.rect.left > ANCHO:
            self.kill()

# Grupos de sprites
todos_los_sprites = pygame.sprite.Group()
brujas = pygame.sprite.Group()
proyectiles = pygame.sprite.Group()

# Crear personaje principal
monaguillo = Monaguillo()
todos_los_sprites.add(monaguillo)

# Crear brujas
for i in range(5):
    bruja = Bruja()
    todos_los_sprites.add(bruja)
    brujas.add(bruja)

# Reloj para controlar FPS
reloj = pygame.time.Clock()

# Bucle principal del juego
ejecutando = True
while ejecutando:
    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                monaguillo.ataque()

    # Actualizar
    todos_los_sprites.update()

    # Colisiones
    colisiones = pygame.sprite.groupcollide(proyectiles, brujas, True, True)

    # Dibujar
    PANTALLA.fill(NEGRO)
    todos_los_sprites.draw(PANTALLA)

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar FPS
    reloj.tick(60)

# Salir de Pygame
pygame.quit()
