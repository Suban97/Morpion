import pygame

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
