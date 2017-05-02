#!/usr/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *
from game_2048lenght import *
from tkinter.messagebox import *
from os.path import *

themelist={(0,):"Basic",(1,):"Chemical"}
name = "guest"
fenetre = None
grid = None
gr_grid = []
lenght = 4
theme="Basic"
Etat = False
sized=None
box=None
size=4

#Dictionnaire des couleurs du jeu en version Chemical
TILES_BG_COLOR_C = {     2:"#caf4b7", 4:"#6a9657", 8:"#2d4225", 
                  16:"#7fc4bb", 32:"#4b9e93", 64:"#1d635a",
                  128:"#c87ed6", 256:"#783684", 512:"#d62434", 
                  1024:"#84363d", 2048:"#141b77" }
#Dictionnaire des couleurs du jeu en version Basic
TILES_BG_COLOR = {   2:"#eee4da", 4:"#ede0c8", 8:"#f2b179", 
                  16:"#f59563", 32:"#f67c5f", 64:"#f65e3b",
                  128:"#edcf72", 256:"#edcc61", 512:"#edc850", 
                  1024:"#edc53f", 2048:"#edc22e",4096:"#141b77", 8192:"#141b77", 16384:"#141b77"  }

TILES_FG_COLOR = { 2:"#776e65", 4:"#776e65", 8:"#f9f6f2", 16:"#f9f6f2", \
                   32:"#f9f6f2", 64:"#f9f6f2", 128:"#f9f6f2", 256:"#f9f6f2", \
                   512:"#f9f6f2", 1024:"#f9f6f2", 2048:"#f9f6f2", 4096:"#141b77", 8192:"#141b77", 16384:"#141b77" }
#Dictionnaire des couleurs en fonction des thèmes 
COLOR_L = { "Basic" : TILES_BG_COLOR , "Chemical" : TILES_BG_COLOR_C }

COLOR_BG = { "Basic" : "#92877d" , "Chemical" : "#ffffff" }
GAME_BG = "#92877d"
GAME_BG_C = "#b4b3e5"




TILE_EMPTY_BG = "#9e948a"

TILE_EMPTY_D = { "Basic" : "#9e948a", "Chemical" : "#c6d1d0" }
TILES_FONT = {"Verdana", 60, "bold"}

GAME_SIZE = 600

TILES_SIZE = GAME_SIZE // lenght

  
commands = { "Up" : "up", "Left" : "left", "Right" : "right", "Down" : "down" }



def about():
    """ Renvoie des infos """
    showinfo( title = " About ", message = " Beta version 0.1        Developped by Sophie and Simon" )
    
def change_theme():
    """ permet de changer le theme """
    global atheme, box, theme, grid
    select=box.curselection() 
    theme = themelist[select]
    atheme.destroy()
    fenetre.destroy()
    grid = grid_init(lenght)
    main(grid)

def get_theme():
    global atheme, box
    atheme = Toplevel()
    atheme.title('Choose a theme')
    box=Listbox(atheme)
    box.insert(END,"Basic")
    box.insert(END,"Chemical")
    button=Button(atheme, text="Confirm", command=change_theme)
    box.pack()
    button.pack()
    atheme.mainloop()
    
    
def you_lose():
    showinfo(None,"You lose")
    save_scoreG(grid,lenght)

def change_size():
    global sized, box, lenght, grid
    lenght = int(box.get())
    sized.destroy()
    fenetre.destroy()
    grid = grid_init(lenght)
    main(grid)

def get_lenght():
    global sized, box
    sized = Toplevel()
    sized.title('Choose a grid size')
    box=Spinbox(sized, from_=3, to=6, justify = CENTER, state = "readonly" )
    button=Button(sized, text="Confirm", command=change_size)
    box.pack()
    button.pack()
    sized.mainloop()

def ask_name():
    global entry, master
    master = Toplevel()
    master.title("Your Name")
    button=Button(master, text='Input your name and click here', command = get_name, bg= "yellow" )
    usertext= StringVar()
    entry = Entry(master, textvariable=usertext)
    entry.pack()
    button.pack()
    master.mainloop()

    
def get_name():
    global  name, entry, master

    name = str(entry.get())
    master.destroy()
    
    
def game_quit():
    global name, fenetre
    if askyesno("Quit game ?","Are you sure? :("):
        if askyesno("Save ?","Do you want to save your game? "):
            ask_name()
            save_scoreG(grid,lenght)
    fenetre.destroy()

def reset():
    global grid
    if askyesno("Save ?","Do you want to save your game? "):
        ask_name()
        save_scoreG(grid,lenght)
    fenetre.destroy()
    Etat = False
    grid = grid_init(lenght)
    main(grid)

def save_game():
    global grid
    save_grid(grid)
   

def load_game():
    global grid, lenght
    fenetre.destroy()
    grid = grid_load()
    lenght = len(grid)
    
    main(grid)

def manuel():
    showinfo(title="Manuel", message = """ FR : une fois lancée : 
vous pouvez jouer en utilisant les flèches du clavier et vous avez à votre disposition une barre menu composée ainsi : 

1e menu : Game : il comporte 4 options :
    -reset qui recommence une partie
    -Load qui permet de charger une partie sauvegardée précédemment,
    -Save qui permet de sauvegarder la partie.
    -Quit qui permet de quitter le jeu. 
2e menu : options : il comporte 2 options :
    -Size qui permet de choisir la taille de la grille dans une nouvelle fenêtre
    -Theme qui permet de choisir le thème avec les nombres basiques ou le thème avec les éléments du tableau périodique.
3e menu : Score : il comporte 2 options :
    -Topscore affichant le meilleurs score
    -Score affichant le score actuel du joueur dans une fenêtre.
4e menu : About : il comporte 2 options :
    -About affichant une fenetre donnant des informations sur les developpeurs
    -Manuel affichant une fenêtre qui vous donne les règles du jeu.
Amuse-toi bien !!""")

def get_score():
    showinfo(title = "Actual Score", message = "Your Score : " + str(score(grid,lenght)) )

def save_scoreG(grid,lenght):
    global name 
    """ Permet la sauvegarde du score dans un fichier nommé score """
    with open('score','a') as s:
        s.write(str(lenght)+':' +str(score(grid,lenght))+ ':' + name + "."+'\n')
    


def top_score ():
    global lenght
    showinfo( title = " Top Score ", message = str(lenght)+" cases: Top score : "+str(tri_score(lenght)))


def main(grid):
    """
    launch the graphical game
    
    UC : none
    """
    global fenetre, gr_grid, lenght, sized, GAME_BG, GAME_BG_C
    fenetre = Tk()
    fenetre.grid()
    fenetre.title('2048 Beta')
    fenetre.bind("<Key>", key_pressed)


    menubar = Menu(fenetre)
    
    Game = Menu(menubar, tearoff = 0)
    Game.add_command(label = "Reset", command = reset )
    Game.add_command(label = "Load", command = load_game )
    Game.add_command(label = "Save", command = save_game )
    Game.add_separator()
    Game.add_command(label = "Quit", command = game_quit )

    Score = Menu(menubar, tearoff = 0 )
    Score.add_command(label = "Top scores", command = top_score )
    Score.add_command(label = "Score", command = get_score )


    Options = Menu(menubar, tearoff = 0 )
    Options.add_command( label = "Size", command = get_lenght )
    Options.add_command( label = "Theme", command = get_theme )

    About = Menu(menubar, tearoff = 0)
    About.add_command( label = 'About', command = about)
    About.add_command( label='How to play', command = manuel)

    
    

    menubar.add_cascade( label = "Game", menu = Game )
    menubar.add_cascade( label = "Options", menu = Options )
    menubar.add_cascade( label = "Score", menu = Score )
    menubar.add_cascade( label = "Help", menu = About  )
    
    fenetre.config(menu = menubar) 

    background = Frame(fenetre, bg = COLOR_BG[theme],
                       width=GAME_SIZE, height=GAME_SIZE)
    background.grid()
    gr_grid = []

    for i in range(lenght):
        gr_line = []
        for j in range(lenght):
            cell = Frame(background, bg = TILE_EMPTY_D[theme],
                         width = TILES_SIZE, height = TILES_SIZE)
            cell.grid(row=i, column=j,padx=1, pady=1)
            t = Label(master = cell, text = "", bg = TILE_EMPTY_D[theme],
                      justify = CENTER, font = TILES_FONT,
                      width=8, height=4)
            t.grid()
            gr_line.append(t)
        gr_grid.append(gr_line)
    grid_display(grid)
    fenetre.mainloop()

def grid_display(grid):
    """
    graphical grid display
    
    UC : none
    """
    global gr_grid, fenetre, lenght, theme, COLOR_L, COLOR
    for i in range(lenght):
        for j in range(lenght):
            imprime= THEMELIST[theme[0]][grid_get_value(grid,i,j)]
            if imprime == "    " :
                gr_grid[i][j].configure(text="", bg=TILE_EMPTY_D[theme])
            else:
                gr_grid[i][j].configure(text=str(imprime), 
                                        bg=COLOR_L[theme][grid_get_value(grid,i,j)],
                                        fg=TILES_FG_COLOR[grid_get_value(grid,i,j)])
    fenetre.update_idletasks()

def key_pressed(event):
    """
    key press event handler
    
    UC : none
    """
    global fenetre, grid, Etat
    
    key = event.keysym
    if key in commands:
        test= copy(grid,lenght)
        grid_move(grid, commands[key],lenght)
        if get_new_position(grid,lenght) != [] and test != grid: #Le mouvement apporte-t-il des modifications à la grille 
            grid_add_new_tile(grid,lenght)
        test= copy(grid,lenght)
        if is_grid_over(grid,lenght): #Aucun mouvement possible
            you_lose()
        if grid_get_max_value(grid,lenght) == 2048: #Tile 2048 atteinte
            if Etat == False :
                showinfo(title = "Game info" , message = "You win" )
                if askyesno("Keep playing?","Do you want to keep playing?"):
                    Etat = True
                else : 
                    ask_name()
                    save_scoreG(grid,lenght)
        if grid_get_max_value(grid,lenght) == 16384: #La valeur maximale dans les dictionnaires est 16384
            showinfo(title = "Over" , message = "You beat the code ! :)" ) 
            
                
            
        grid_display(grid)


        
    
        
if __name__ == '__main__':
    import sys
    if isfile("save-grid.txt"):
        if askyesno("2048", "A saved game isn't over yet, do you want to load it ?"):
            load_game()

    grid = grid_init(lenght)
    main(grid)
    
