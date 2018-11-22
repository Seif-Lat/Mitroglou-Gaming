
import numpy as np
from tkinter import *
root=Tk()
root.title("Working state")

frame = Frame(root)
frame.grid()
#Entry_theme=StringVar()
Entry_theme= Entry(root,width=50, text= "inserer le theme souhaité(1,2,3)")#, textvariable=Entry_theme)
Entry_theme.grid(row=0,column=4,sticky=W,padx=10)
Label(root, text="Théme:").grid(row=0,column=0,sticky=W,padx=10)

#Entry_theme=StringVar()
Entry_size= Entry(root,width=50, text= "inserer la taille de la grille")#, textvariable=Entry_theme)
Entry_size.grid(row=1,column=4,sticky=W,padx=10)
Label(root, text="Théme:").grid(row=0,column=0,sticky=W,padx=10)

Com=StringVar()
Commentaire= Entry(root, text= "ATTENTION REGARDEZ ICI EN JOUANT", textvariable=Com,width=50)
Commentaire.grid(row=2,column=4,sticky=W,padx=10)
Label(root, text="Taille:").grid(row=1,column=0,sticky=W,padx=10)



#--Cette partie dessine les boutons de jeu--

def waiting():
    global command
    Button_left.wait_variable(command)

command=StringVar()
Text1=StringVar()
Button_left=Radiobutton(root,indicatoron=0,textvariable=Text1, variable=command,value="g")
Button_left.grid(row=5, column=0, padx=2, sticky=E)
Text1.set("left")

Text2=StringVar()
Button_right=Radiobutton(root,indicatoron=0, variable=command,textvariable=Text2,value="d")
Button_right.grid(row=5, column=2, padx=4, sticky=W)
Text2.set("Right")

Text3=StringVar()
Button_up=Radiobutton(root,indicatoron=0, variable=command,value="h",textvariable=Text3)
Button_up.grid(row=4, column=1, pady=2, )
Text3.set("Up")

Text4=StringVar()
Button_down=Radiobutton(root,indicatoron=0, variable=command ,value="b",textvariable=Text4)
Button_down.grid(row=5, column=1, padx=2, sticky=W)
Text4.set("Down")




def Affiche_mat(A,root,Dict):

    #root= Tk() #à modifier si la fenêtre est deja créee

    nb_lignes=len(A)
    nb_colonnes=len(A[0])
    L=[]
    H=[]
    for i in range (0,nb_lignes):
        for j in range (0,nb_colonnes):
            adresse_image=Dict[A[i][j]]
            #photo=PhotoImage(file=adresse_image)
            contenu=StringVar()
            contenu.set(A[i][j])
            L.append(contenu)
            label=Label(root,width=10,height=5,borderwidth=3,relief='groove',textvariable=L[i*nb_colonnes+j])
            label.grid(row=i+6,column=j+6)
            H.append(label)

            #exec("var_"+str(i)+"_"+str(j)+"= StringVar()")
            #exec("var_"+str(i)+"_"+str(j)+".set(A[i][j])")

                        #print("var_"+str(i)+"_"+str(j)+".set(A[i][j])")
    return(H,L)




