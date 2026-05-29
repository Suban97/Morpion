import pygame

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
        
    def equal(self, grille, main):
        if all(carre[1] is not None for carre in grille.cases) and self.game_active == True:
            print("égalité")
            main()
        
            
            
        

