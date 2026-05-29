import pygame, sys

def reset_buttons(game, grille):
    game.reset()
    grille.reset()

def quit_buttons():
    print("quitter")
    pygame.quit()
    sys.exit()


def draw_button(screen, events, rect, text, couleur, action):
    font = pygame.font.SysFont("georgia", 20, bold=True)

    rect = pygame.Rect(rect)
    
    # Récupérer la position de la souris
    mouse_pos = pygame.mouse.get_pos()
    is_hovered = rect.collidepoint(mouse_pos)
    
    # Effet de survol : augmenter légèrement la luminosité
    if is_hovered:
        couleur_finale = tuple(min(int(c * 1.1), 255) for c in couleur)
    else:
        couleur_finale = couleur
    
    # Bouton principal avec bordure fine
    pygame.draw.rect(screen, couleur_finale, rect)
    pygame.draw.rect(screen, (200, 210, 220), rect, 1)  # Bordure fine

    # Texte blanc/clair
    text_surface = font.render(text, True, (248, 248, 252))
    screen.blit(text_surface, text_surface.get_rect(center=rect.center))

    # Gestion du clic
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                action()
