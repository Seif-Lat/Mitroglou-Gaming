
import Affichage_Mat
def modif_commentaire(text):
    global Commentaire
    Commentaire.delete(0,"end")
    Commentaire.insert(0,text)
    

def set_direction():

    Affichage_Mat.waiting()
    print(Affichage_Mat.command.get())

    return(Affichage_Mat.command.get())

    #while not move in ["g","d","h","b"]:
     #   move = input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)):")
    #return move

def set_size_grid():
    global Entry_size
    size=""
    i=0
    while not size.isdigit():
        i+=1
        size = Entry_size.get()
        if i>0:
           modif_commentaire( "Sérieux putain??? on a dit entier...")
            
    return size

def set_theme_grid():
    global Entry_theme
    theme=""
    i=0
    while not theme in ["0","1","2"]: 
        i+=1
        theme = Entry_theme.get()
        if i>0:
            modif_commentaire("là t'abuse fdp soi 0,1 ou 2 c pas trop difficile wesh")
    return theme

