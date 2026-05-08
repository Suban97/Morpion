import pygame
import sys
pygame.init()

colonne = 3
ligne = 3
taille_case = 200

largeur = colonne * taille_case
hauteur = ligne * taille_case

class GrilleManager:
    def __init__(self, colonne, ligne, taille_case):
        self.colonne = colonne
        self.ligne = ligne
        self.taille_case = taille_case
        
        
        self.largeur = colonne * taille_case
        self.hauteur = ligne * taille_case
        self.centre = taille_case/2
        
        self.reset()
        
        
    def reset(self):
        lettre = 'ABC'
        self.cases = [
             [lettre[x]+ str(y+1), #coordonnées servant d'identité ex: "A1", "B2"
              None,
               x * self.taille_case,
               y * self.taille_case,
               self.taille_case] for x in range(self.colonne)
            for y in range(self.ligne) ]
        print(self.cases)
    
    
    def draw(self, screen, croix, cercle, taille_font):
        for carre in self.cases:
            
            if carre[1] == 'croix':
                pygame.draw.rect(screen, (250, 250, 250), (carre[2], carre[3], carre[4], carre[4]))
                pygame.draw.rect(screen, (0,0,0), (carre[2], carre[3], carre[4], carre[4]), 2)
                
                centre_x = carre[2] + carre[4] // 2
                centre_y = carre[3] + carre[4] // 2

                rect = croix.get_rect(center=(centre_x, centre_y))
                screen.blit(croix, rect)
                
            elif carre[1] == 'cercle':
                pygame.draw.rect(screen, (250, 250, 250), (carre[2], carre[3], carre[4], carre[4]))
                pygame.draw.rect(screen, (0,0,0), (carre[2], carre[3], carre[4], carre[4]), 2)
                
                centre_x = carre[2] + carre[4] // 2
                centre_y = carre[3] + carre[4] // 2

                rect = cercle.get_rect(center=(centre_x, centre_y))
                screen.blit(cercle, rect)
                
            else:
                pygame.draw.rect(screen, (250, 250, 250), (carre[2], carre[3], carre[4], carre[4]))
                pygame.draw.rect(screen, (0,0,0), (carre[2], carre[3], carre[4], carre[4]), 2)
                    
    
    
    def in_case(self, game, croix, cercle, events, mouse_x, mouse_y):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

                for carre in self.cases:
                    if not carre[1] and game.game_active:
                        if (carre[2] < mouse_x < carre[2] + carre[4] and
                            carre[3] < mouse_y < carre[3] + carre[4]):
                            
                            print("in case")
                            print(carre)
                            
                            if game.joueur_actuel() == 'joueur1' and carre:
                                print("Croix")
                                carre[1] = 'croix'
                                game.prise_case('joueur1', carre[0])
                                
                            elif game.joueur_actuel() == 'joueur2':
                                print("Cercle")
                                carre[1] = 'cercle'
                                game.prise_case('joueur2', carre[0])
                            
                            game.fin_tour()






class GameManager:
    
    def __init__(self):
        self.reset()

    def reset(self):
        self.game_active = True
        self.joueurs = ['joueur1', 'joueur2']
        self.index = 0
        self.cases1 = []
        self.cases2 = []
        self.winner = None
        
    
    
    def joueur_actuel(self):
        return self.joueurs[self.index]
    
    def fin_tour(self):
        self.index = (self.index + 1) % len(self.joueurs)
    
    
    def prise_case(self, joueur, nom):
        if self.game_active:
            if joueur == 'joueur1':
                self.cases1.append(nom)
            elif joueur == 'joueur2':
                self.cases2.append(nom)
    
    
    def test_win(self, game):
        winlist = [
            ("A1", "A2", "A3"), ("B1", "B2", "B3"),("C1", "C2", "C3"), #vertical
            ("A1", "B1", "C1"), ("A2", "B2", "C2"), ("A3", "B3", "C3"), #horizontal
            ("A1", "B2", "C3"), ("A3", "B2", "C1") #diagonale
        ]
        
        if any(set(combo).issubset(self.cases1) for combo in winlist):
            self.game_active = False
            self.winner = "Joueur 1"

        if any(set(combo).issubset(self.cases2) for combo in winlist):
            self.game_active = False
            self.winner = "Joueur 2"
        
    def equal(self, grille):
        if all(carre[1] is not None for carre in grille.cases) and self.game_active == True:
            print("égalité")
            main()
        
            
            
        
def draw_buttons(screen, game, grille, events):
    font = pygame.font.SysFont(None, 50)
    
    replay_rect = pygame.Rect(100, 250, 180, 70)
    quit_rect = pygame.Rect(320, 250, 180, 70)
    
    pygame.draw.rect(screen, (100,200,100), replay_rect)
    pygame.draw.rect(screen, (200, 80, 80), quit_rect)
    
    replay_text = font.render("Rejouer", True, (255,255,255))
    quit_text = font.render("Quitter", True, (255,255,255))
    
    screen.blit(replay_text, replay_text.get_rect(center= replay_rect.center))
    screen.blit(quit_text, quit_text.get_rect(center=quit_rect.center))
    
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if replay_rect.collidepoint(event.pos):
                game.reset()
                grille.reset()
                
            if quit_rect.collidepoint(event.pos):
                print("quitter")
                pygame.quit()
                sys.exit()
    
    
        




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
        game.equal(grille)
        
        
        if not game.game_active:
            draw_buttons(screen, game, grille, events)
            
        pygame.display.update()




if __name__ == "__main__":
    main()
