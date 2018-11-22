from tkinter import *
from tkinter import ttk
from Affichage_Mat import*
import textual_2048

import grid_2048
import move_2048
import numpy as np
import Affichage_Mat

#textual

def modif_commentaire(text):
    global Commentaire
    Commentaire.delete(0,"end")
    Commentaire.insert(0,text)


#def set_direction():
   # move= ""
  #  while not move in ["g","d","h","b"]:
 #       move = input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)):")
#    return move
Valeurs=[0,' ']
for i in range (1,12):
    Valeurs.append(2**i)
Dict={}
Dict[' ']='0.gif'
Dict[0]='0.gif'
for i in range(1,12):
    Dict[2**i]=str(2**i)+".gif"

def set_size_grid():
    global Entry_size
    size=""
    i=0
    while not size.isdigit():

        size = Entry_size.get()
        if i>0:
           modif_commentaire( "Sérieux putain??? on a dit entier...")
        i+=1
    return size

def set_theme_grid():
    global Entry_theme
    theme=""
    i=0
    while not theme in ["0","1","2"]:

        theme = Entry_theme.get()
        if i>0:
            modif_commentaire("là t'abuse fdp soi 0,1 ou 2 c pas trop difficile wesh")
        i+=1
    return theme

#textual

def play():
    global grid
    ia=False
    if not ia:

        dic_move = {0: "g", 1: "d", 2: "h", 3: "b"}
        size = int(set_size_grid())

        theme = grid_2048.THEMES[set_theme_grid()]
        grid = grid_2048.init_game(size)
        print("Situation de départ :")
        print(grid_2048.grid_to_string_with_size_and_theme(grid, theme, size))
        Affiche_mat(grid,root,Dict)#,theme#
        tour = 1
        dic_move = {0: "g", 1: "d", 2: "h", 3: "b"}
        while not move_2048.is_game_over(grid) and grid_2048.get_grid_tile_max(grid) < 2048:
            moves = move_2048.move_possible(grid)
            commands_possible = [dic_move[i] for i in range(4) if moves[i]]
            command=textual_2048.set_direction()
            while not command in commands_possible:
                print("Deplacement impossible")
                Commentaire.delete(0,"end")
                Commentaire.insert(0,"Deplacement impossible, t'es con")
                command=textual_2048.set_direction()
                print("stuck")
            grid = move_2048.move_grid(grid, command)
            print("grid modifiée")
            Affiche_mat(grid,root,Dict)
            if not grid_2048.is_full_grid(grid):
                grid = grid_2048.grid_add_new_tile(grid)
            #print("Tour {}, deplacement {} :".format(tour, command))
            #textual_2048.modif_commentaire("Tour {"+str(tour)+"}, deplacement {"+command+"} :")
            #print(grid_2048.py.grid_to_string_with_size_and_theme(grid, theme, size))
                Affiche_mat(grid,root,Dict)
                print("new tile ajoutée")

            #tour += 1
            print("boucle atteinte")
        if grid_2048.get_grid_tile_max(grid) >= 2048:
            Commentaire.delete(0,"end")
            Commentaire.insert(0,"woohoo!! ça t'as pris du temps qd mm")
            print('vic')
            return "Victoire !"
        Commentaire.delete(0,"end")
        Commentaire.insert(0,"ha! comme si t'aurais vraiment gagné ...")
        print('GO')
        return "Game Over"
Start_game=Button(root, text="Commencer le jeu",command=play)
Start_game.grid(row= 2,column=0,sticky=W)
grid=np.zeros((5,5))
#root= Tk() #à modifier si la fenêtre est deja créee




root.mainloop()



