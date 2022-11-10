# Gabriel Santana Silva
# RA: 21429
# BasicGame

# Importar e iniciar pygame
import pygame
import models.player as pl1

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

# Instancia o player
player = pl1.Player()

# Inicia o programa
pygame.init()

# Define as dimensões
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Configura a tela de acordo com o tamanho estabelecido
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Mantem o jogo rodando
running = True

while running:
    # Verifica cada evento na fila

    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
        # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
        # Sai se o usuario clicar no botao de sair
        if event.type == pygame.QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()

    # Preenche em branco
    screen.fill((0, 0, 0))

    # Cria uma superfice passando sua largura e altura
    surf = pygame.Surface((50, 50))

    # Da a superfice uma cor para separar do plano de fundo
    surf.fill((255, 255, 255))
    rect = surf.get_rect()

    # Ponha o centro da surf no centro do centro da tela
    surf_center = (
        (SCREEN_WIDTH-surf.get_width())/2,
        (SCREEN_HEIGHT-surf.get_height())/2
    )

    # Desenha a superfice no centro da tela
    screen.blit(player.surf, player.rect)
    # Flip a tela
    pygame.display.flip()

# Terminou fechando o app
pygame.quit()