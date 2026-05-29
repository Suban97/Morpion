import pygame

class GrilleManager:
    def __init__(self, colonne, ligne, taille_case, padding=0):
        self.colonne = colonne
        self.ligne = ligne
        self.taille_case = taille_case
        self.padding = padding
        
        self.largeur = colonne * taille_case
        self.hauteur = ligne * taille_case
        self.centre = taille_case/2
        
        self.reset()
        
    def reset(self):
        lettre = 'ABC'
        self.cases = [
             [lettre[x]+ str(y+1),
              None,
                20 + x * (self.taille_case + self.padding) + self.padding,
                70 + y * (self.taille_case + self.padding) + self.padding,
                self.taille_case] for x in range(self.colonne)
            for y in range(self.ligne) ]
        print(self.cases)
    
    def draw(self, screen, croix, cercle, taille_font):
        # Palette raffinée
        COULEUR_CASE_VIDE = (245, 245, 250)
        COULEUR_BORDURE = (200, 210, 220)
        COULEUR_HOVER = (235, 240, 248)
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        
        for carre in self.cases:
            x, y, w, h = carre[2], carre[3], carre[4], carre[4]
            
            # Vérifier si la souris est sur la case
            is_hovered = (x < mouse_x < x + w and y < mouse_y < y + h) and not carre[1]
            
            # Couleur de fond selon l'état
            if carre[1]:
                couleur_fond = (242, 242, 248)
            elif is_hovered:
                couleur_fond = COULEUR_HOVER
            else:
                couleur_fond = COULEUR_CASE_VIDE
            
            # Dessiner le fond
            pygame.draw.rect(screen, couleur_fond, (x, y, w, h))
            # Bordure fine et élégante
            pygame.draw.rect(screen, COULEUR_BORDURE, (x, y, w, h), 1)
            
            # Dessiner X
            if carre[1] == 'croix':
                centre_x = x + w // 2
                centre_y = y + h // 2
                rect = croix.get_rect(center=(centre_x, centre_y))
                screen.blit(croix, rect)
                
            # Dessiner O
            elif carre[1] == 'cercle':
                centre_x = x + w // 2
                centre_y = y + h // 2
                rect = cercle.get_rect(center=(centre_x, centre_y))
                screen.blit(cercle, rect)
    
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
