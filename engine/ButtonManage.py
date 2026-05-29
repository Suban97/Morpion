import pygame, sys

def reset_buttons(game, grille):
    game.reset()
    grille.reset()

def quit_buttons():
    print("quitter")
    pygame.quit()
    sys.exit()


# rect = (x, y, width, height)
# action = fonction à appeler lors du clic sur le bouton
# text = texte à afficher sur le bouton
def draw_button(screen, events, rect, text, couleur, action):
    font = pygame.font.SysFont(None, 50)

    rect = pygame.Rect(rect)
    pygame.draw.rect(screen, couleur, rect)

    text_surface = font.render(text, True, (255,255,255))
    screen.blit(text_surface, text_surface.get_rect(center=rect.center))

    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                action()
