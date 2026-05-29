import pygame
import sys

from engine.Grille import GrilleManager
from engine.Player import GameManager
from engine.ButtonManage import draw_button, reset_buttons, quit_buttons

pygame.init()

colonne = 3
ligne = 3
taille_case = 200

largeur = colonne * taille_case
hauteur = ligne * taille_case

screen = pygame.display.set_mode((largeur, hauteur))

def main():
    taille_font = 150
    font = pygame.font.SysFont(None, taille_font)
    
    croix = font.render("X", True, (250,100,100))
    cercle = font.render("O", True, (100,100,250))
    
    grille = GrilleManager(3,3,200)
    game = GameManager()
        
    while True:
        screen.fill((255,255,255))
        mouse_x, mouse_y = pygame.mouse.get_pos()

        grille.draw(screen, croix, cercle, taille_font)
        
        
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        
        grille.in_case( game, croix, cercle, events, mouse_x, mouse_y)
        
        game.test_win(game)
        game.equal(grille, main)
        
        
        if not game.game_active:
            draw_button(screen, events, (100, 250, 180, 70), "Rejouer", (100,200,100), lambda: reset_buttons(game, grille))
            draw_button(screen, events, (320, 250, 180, 70), "Quitter", (200, 100, 100), lambda: quit_buttons())
            
        pygame.display.update()




if __name__ == "__main__":
    main()
