import pygame
import sys

from engine.Grille import GrilleManager
from engine.Player import GameManager
from engine.ButtonManage import draw_button, reset_buttons, quit_buttons

pygame.init()

# Palette raffinée et minimaliste
COULEUR_FOND = (248, 248, 252)
COULEUR_CASE_VIDE = (245, 245, 250)
COULEUR_CASE_HOVER = (235, 240, 248)
COULEUR_X = (70, 130, 180)
COULEUR_O = (178, 34, 34)
COULEUR_BORDURE = (200, 210, 220)
COULEUR_TEXTE = (45, 50, 60)
COULEUR_ACCENT = (200, 160, 100)
COULEUR_BOUTON_REPLAY = (70, 130, 180)
COULEUR_BOUTON_QUIT = (178, 34, 34)

colonne = 3
ligne = 3
taille_case = 120
padding = 12

largeur = colonne * taille_case + (colonne + 1) * padding + 60
hauteur = ligne * taille_case + (ligne + 1) * padding + 200

screen = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Morpion — Tic Tac Toe")

def main():
    taille_font = int(taille_case * 0.65)
    font_game = pygame.font.SysFont("georgia", taille_font, bold=True)
    font_title = pygame.font.SysFont("georgia", 44, bold=True)
    font_info = pygame.font.SysFont("georgia", 26)
    
    croix = font_game.render("X", True, COULEUR_X)
    cercle = font_game.render("O", True, COULEUR_O)
    
    grille = GrilleManager(colonne, ligne, taille_case, padding)
    game = GameManager()
        
    while True:
        screen.fill(COULEUR_FOND)
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Ligne décorative sous le titre
        pygame.draw.line(screen, COULEUR_ACCENT, (30, 70), (largeur - 30, 70), 2)
        
        # Dessiner le titre
        titre = font_title.render("MORPION", True, COULEUR_TEXTE)
        screen.blit(titre, (30, 20))
        
        # Dessiner la grille
        grille.draw(screen, croix, cercle, taille_font)
        
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Gestion des clics
        grille.in_case(game, croix, cercle, events, mouse_x, mouse_y)
        
        game.test_win(game)
        game.equal(grille, main)
        
        # Afficher le joueur actuel ou le résultat
        joueur_y = hauteur - 140
        if game.game_active:
            joueur_text = font_info.render(f"Tour du {game.joueur_actuel().replace('joueur', 'Joueur ')}", True, COULEUR_TEXTE)
        else:
            if game.winner:
                joueur_text = font_info.render(f"{game.winner} a gagné", True, COULEUR_ACCENT)
            else:
                joueur_text = font_info.render("Égalité", True, COULEUR_ACCENT)
        screen.blit(joueur_text, (30, joueur_y))
        
        # Afficher les boutons
        if not game.game_active:
            draw_button(screen, events, (30, hauteur - 70, 140, 50), "Rejouer", COULEUR_BOUTON_REPLAY, lambda: reset_buttons(game, grille))
            draw_button(screen, events, (largeur - 170, hauteur - 70, 140, 50), "Quitter", COULEUR_BOUTON_QUIT, lambda: quit_buttons())
            
        pygame.display.update()
if __name__ == "__main__":
    main()
