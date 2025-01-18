# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 14:51:18 2024

@author: camil
"""

class Gomoku:
    def __init__(self):
        self.plateau = [[' ' for x in range(15)] for y in range(15)]
        self.turn = 'B' #B for Black, W for White
        self.utility = 0
        
    def __str__(self):
        s = ""
        for x in range(15) :
            s+="\n| "
            for y in range(15):
                s += self.plateau[x][y] +" | "
        return s 
        
    def Actions(self):
        return [chr(x+97).upper() + str(y) for x in range(15) for y in range(15) if self.plateau[x][y] == ' ']

    def PlayerTurn(self):
        self.turn = 'W' if self.turn == 'B' else 'B'
            
    def Result(self, action):
        if action in self.Actions():
            self.plateau[ord(action[0].lower()) - 97][int(action[1:])] = self.turn
            self.PlayerTurn()
        else :
            print("Action impossible")
            
    def Terminal_Test(self):
        #check si toutes les cases pleines
        if(all(self.plateau[x][y] != ' ' for x in range(15) for y in range(15))):
            return True
       
        #check si un joueur gagne via diagonales
        for i in range(10):
            for j in range(10):
                if (self.plateau[i][j] == self.plateau[i+1][j+1] == self.plateau[i+2][j+2] == self.plateau[i+3][j+3] == self.plateau[i+4][j+4] != ' '):
                    self.Utility(self.plateau[i][j])
                    return True
                elif(self.plateau[i][14] == self.plateau[i+1][14-j] == self.plateau[i+2][14 - j - 1] == self.plateau[i+3][14 - j - 2] == self.plateau[i+4][14 - j - 3] != ' '):
                    self.Utility(self.plateau[i][14])
                    return True         
         
        #check si un joueur gagne via colonnes ou lignes
        for i in range(15):
            for j in range(10):
                if self.plateau[i][j] == self.plateau[i][1 + j] == self.plateau[i][2 + j] == self.plateau[i][3 + j] == self.plateau[i][4 + j]  != ' ':
                    self.Utility(self.plateau[i][j])
                    return True
                if self.plateau[j][i] == self.plateau[1 + j][i] == self.plateau[2 + j][i] == self.plateau[3 + j][i] == self.plateau[4 + j][i] != ' ':
                    self.Utility(self.plateau[j][i])
                    return True
        return False
    
    def Utility(self, player):
        if player == 'B':
            self.utility = 1
        else :
            self.utility = -1

def Max_Value(game):
    return None

def Min_Value(game):
    return None

def Minimax_Decision(game):
    return None

#retourne V si contenue dans le carré
def LongPro(move):
    #entre 4 et 10 et entre E et K
    return move in [chr(x+97).upper() + str(y) for x in range(4,11) for y in range(4,11)]

def Jeu():
    tour = 1
    game = Gomoku()
    
    inputPlayer = ""
    while inputPlayer != 'B' and inputPlayer != 'W':
        inputPlayer = input("Quelle couleur voulez vous jouer ? (B for Black, W for White)\nLe joueur B commence en premier. Son premier mouvement est imposé en H7 pour jouer la variante Long Pro.\n").upper()
    
    #modifier le code car pour l'instant implémenté en sachant que Minimax fonctionne pas
    while not game.Terminal_Test():
        if(game.turn == inputPlayer):
            if(inputPlayer == 'B'):
                print("\nTour n°" + str(tour))
                print(game)
                print("Votre tour !")
                if (tour == 1):
                    move = 'H7'
                elif (tour == 2) :
                    move = input('Entrez votre mouvement (ligne entre A et O, colonne entre 0 et 14, format : AO)\nAttention : votre pion ne peut pas être placée dans un carré de taille 7 cases sur 7 cases de centre H7 pour ce tour.\n')
                    while LongPro(move):
                        move = input('\nAttention : votre pion ne peut pas être placé e dans un carré de taille 7 cases sur 7 cases de centre H7 pour ce tour.\nRéessayez une autre action.\n')
                else :
                    move = input('Entrez votre mouvement (ligne entre A et O, colonne entre 0 et 14, format : AO\n')
                game.Result(move)
                tour += 1
            else :
                print(game)
                print("Votre tour !")
                move = input('Entrez votre mouvement (ligne entre A et O, colonne entre 0 et 14, format : AO\n')
                game.Result(move)        
        else :
            print("Tour de la machine...")
            if(inputPlayer == 'B'):
               # move = Minimax_Decision(game) #coder Minimax avant de décommenter
                move = 'H4' #retirer une fois minimax codé
            else :
                print("\nTour n°" + str(tour))
                print(game)
                if (tour == 1):
                    move = 'H7'
                else :
                    move = Minimax_Decision(game)
                    if(tour == 2):
                        while LongPro(move):
                            move = Minimax_Decision(game)
                tour += 1
            game.Result(move)

    print("Partie finie !")
    print(game)
    score = game.Utility()
    if score == 1:
        print('Bravo, vous avez gagné !')
    elif score == 0:
        print('Ex aequo')
    else:
        print('Vous avez perdu :(')
        
Jeu()

#%% Test NE PAS COMPILER    
a = Gomoku()
print(a.Actions())

##check gagnant lignes
a.Result('D4')
a.Result('B0')
a.Result('A1')
a.Result('B1')
a.Result('A2')
a.Result('B2')
a.Result('A3')
a.Result('B3')
a.Result('A4')
a.Result('B4')

## check gagnant lignes colonnes
# a.Result('A0')
# a.Result('A1')
# a.Result('B0')
# a.Result('B2')
# a.Result('C0')
# a.Result('C3')
# a.Result('D0')
# a.Result('D4')
# a.Result('E3') #remplacer par 'E0' pour tester les colonnes
# a.Result('E5')
print(a)
print(a.Terminal_Test())
print(a.utility)