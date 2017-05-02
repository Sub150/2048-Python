
#DE BONVILLE Sophie
# DESCAMPS Simon


from textual_2048 import *
import random
import pickle
commands = { "U" : "up", "L" : "left", "R" : "right", "D" : "down", "S" : "save"}

Chemical={ None:"    ",2: "H", 4: "He",8: "Li", 16:"Be", 32:"B",64:"C",128:"N",256:"O",512:"F",1024:"Ne",2048:"Na",4096:"Mg",8192:"Al",16384:"Si"}
Basic={ None:"    ",2: 2, 4: 4,8: 8, 16:16, 32:32,64:64,128:128,256:256,512:512,1024:1024,2048:2048,4096:4096,8192:8192,16384:16384}

#le thème hell a pour but de changer les couleurs des cases, et non les nombres. Il n'est pas encore implémenté au programme.
Hell={ None:"    ",2: 2, 4: 4,8: 8, 16:16, 32:32,64:64,128:128,256:256,512:512,1024:1024,2048:2048,4096:4096,8192:8192,16384:16384}

#liste des thèmes
THEMELIST={"B":Basic,"C":Chemical, "H" : Hell }

def read_grid_lenght():
    """
    Pas de paramètre d'entrée. Permet de choisir le format de la grille. (Dans la version graphique la version le format est 4x4 )
    Cu : la valeur entrée doit être comprise entre 3 et 6
    """
    #fonction utile pour textual2048 uniquement
    lenght = input('What grid size do you want between 3 and 6? ( usualy 4 ) ')
    while not 2 < int(lenght) < 7 :
        lenght = input('What grid size do you want between 3 and 6? ( usualy 4 ) ')
    return int(lenght)

def grid_init(lenght):
    """
    paramètre d'entrée : lenght, la longueur définie dans la fonction read_grid_lenght()

    Cette fonction initialise une grille de format lenght*lenght 
    """
    grid=[]
    for l in range(lenght):
        grid += [list( None for c in range(lenght))]
    grid_add_new_tile(grid,lenght)
    return grid
            


def get_new_position (grid,lenght):
    """
    Liste l'ensemble des couples correspondant aux positions c et j des cases vides
    Pas de Cu
    """
    LISTE=[]
    for l in range (lenght):
        for c in range (lenght):
            if grid[l][c] == None :
                LISTE+=[[l,c]]
    return LISTE

def grid_add_new_tile(grid,lenght):
    """ 
    remplace une case vide dans la grille. La nouvelle valeur de celle-ci est soit 2 soit 4
    pas de Cu
    """
    res=get_new_position(grid,lenght)
    coord=random.choice(res)
    l,c=coord[0],coord[1]
    NOMBRE=random.choice((2,2,4))
    grid[l][c]=NOMBRE

def ask_theme():
    """
    Permet de choisir un thème. On désigne le thème par une lettre qu'on entre en majuscule sans guillements.

    Si vous voulez jouer le thème Basic par exemple, entrez B puis appuyez sur entrer.
    
    """
    #Cette fonction est utile pour la version textual seulement.
    theme = input('Choose a theme between (B)asic and (C)hemical    ')
    while not theme in THEMELIST :
        theme = input('Choose a theme between (B)asic and (C)hemical ; tapez B ou C sans guillements    ')
    return theme
def grid_print(grille,lenght,theme):
    """
    entrée : une grille sous forme de liste de listes, la largeur ( lenght ) et le theme.
    imprime la grille de jeu avec les valeurs de chaque case.
    """
    top=" -------"*lenght
    mid="|-------"*lenght + "|"
    middle=0
    print (top)
    for i in range(lenght):
        for j in range(lenght):
            if grid_get_value(grille,i,j)==None :    
                print("|", "    ", end="\t")
            else:
                print("|",THEMELIST[theme][grid_get_value(grille,i,j)],end="\t") 
        print("|",end='\n')
        if middle < (lenght-1) :
            print(mid)
            middle+=1
            
        else :
            print(top)
        

def grid_get_next_grid(grid,i,j,d):
    """
    paramètres : une grille(grid), des coordonnées (i,j) et une direction (d)
    Renvoie la case adjacente à la case de coordonées (i,j) selon la direction d ( "U","L","R","D" )
    l'ensemble des commandes se trouve dans le dictionnaire commands.
        
    """
    if d == "right" :
        if j == 3:
            return None
        else :
            return(grid[i][j+1])
    if d == "left":
        if j == 0:
            return None
        else :
            return(grid[i][j-1])
    if d == "up":
        if i == 0 :
            return None
        else :
            return(grid[i-1][j])
    if d == "down":
        if i == 3 :
            return None
        else :
            return(grid[i+1][j])
        

def is_grid_over(grid,lenght):
    """
    Renvoie True si un mouvement est possible dans une direction minimum, False Sinon
    """
    test = copy(grid,lenght) 
    copy1=copy(grid,lenght)
    copy2=copy(grid,lenght)
    copy3=copy(grid,lenght)
    copy4=copy(grid,lenght)
    grid_move(copy1,commands["R"],lenght)
    grid_move(copy2,commands["L"],lenght)
    grid_move(copy3,commands["D"],lenght)
    grid_move(copy4,commands["U"],lenght)
    return test == copy1 and test == copy2 and test == copy3 and test == copy4 



def grid_get_max_value (grid,lenght):
    """
    Renvoie la valeur de la case la plus haute dans la grille.
    """
    res=0
    for i in range (lenght):
        for j in range (lenght):
            v=grid[i][j]
            if grid[i][j] == None :
                v=0
            if v>res:
               res=v
    if res==0:
        return None 
    return res






def grid_move(grid,move,lenght):
    """
    permet de déplacement de tous les éléments de la grille en fonction de Move dans le cas où il désigne une direction
    """
    if move == "right" :
        l = 0
        while l < lenght :
            c = (lenght-1)
            while c >= 0 :
                if c == (lenght-1) and grid[l][c] != None :
                    m = (lenght-2)
                    while m>0 and grid[l][m] == None :
                        m-=1
                    if grid[l][m] == grid[l][c] :
                        grid[l][m],grid[l][c] = None,grid_get_value(grid,l,m)*2
                        
                       
                elif grid[l][c] != None :
                    if grid[l][c+1]==None :
                        grid[l][c+1],grid[l][c]=grid[l][c],None
                        c+=2
                       
                    else :
                        if m != 0:  
                            m = c-1
                            while m>0 and grid[l][m] == None :
                                m-=1
                            if grid[l][m] == grid[l][c] :
                                grid[l][m],grid[l][c] = None,grid_get_value(grid,l,m)*2
                c-=1
            l+=1

    if move == "left":
        l = 0
        while l < lenght :
            c = 0
            while c <= (lenght-1) :
                if c == 0 and grid[l][c] != None :
                    m = 1
                    while m<(lenght-1) and grid[l][m] == None :
                        m+=1
                    if grid[l][m] == grid[l][c] :
                        grid[l][m],grid[l][c] = None,grid_get_value(grid,l,m)*2
                        
                       
                elif grid[l][c] != None :
                    if grid[l][c-1]==None :
                        grid[l][c-1],grid[l][c]=grid[l][c],None
                        c-=2
                        
                    else :
                        if m != (lenght-1):
                            m = c+1
                            while m<(lenght-1) and grid[l][m] == None :
                                m+=1
                            if grid[l][m] == grid[l][c] :
                                grid[l][m],grid[l][c] = None,grid_get_value(grid,l,m)*2
                c+=1
            l+=1

    if move == "up":
        c = 0
        while c < lenght :
            l = 0
            while l <= (lenght-1) :
                if l == 0 and grid[l][c] != None :
                    m = 1
                    while m<(lenght-1) and grid[m][c] == None :
                        m+=1
                    if grid[m][c] == grid[l][c] :
                        grid[m][c],grid[l][c] = None,grid_get_value(grid,m,c)*2
                        
                       
                elif grid[l][c] != None :
                    if grid[l-1][c]==None :
                        grid[l-1][c],grid[l][c]=grid[l][c],None
                        l-=2
                        
                    else :
                        if m != (lenght-1) :
                            m = l+1
                            while m<(lenght-1) and grid[m][c] == None :
                                m+=1
        
            
                            if grid[m][c] == grid[l][c] :
                                grid[m][c],grid[l][c] = None,grid_get_value(grid,m,c)*2
                l+=1
            c+=1
            

    if move == "down":
        c = 0
        while c < lenght :
            l = (lenght-1)
            while l >= 0 :
                if l == (lenght-1) and grid[l][c] != None :
                    m = (lenght-2)
                    while m>0 and grid[m][c] == None :
                        m-=1
                    if grid[m][c] == grid[l][c] :
                        grid[m][c],grid[l][c] = None,grid_get_value(grid,m,c)*2
                        
                       
                elif grid[l][c] != None :
                    if grid[l+1][c]==None :
                        grid[l+1][c],grid[l][c]=grid[l][c],None
                        l+=2
                        
                    else :
                        if m != 0:
                            m = l-1
                            while m>0 and grid[m][c] == None :
                                m-=1
                            if grid[m][c] == grid[l][c] :
                                grid[m][c],grid[l][c] = None,grid_get_value(grid,m,c)*2
                l-=1
            c+=1

    
    
    
def grid_get_value(grid,i,j):
    """
    renvoie la valeur d'une case de coordonnées i ( ligne ) et j ( colonne )
    """
    return grid[i][j]



def copy(grid,lenght):
    """
    Permet d'effectuer une copie de la grille
    """
    res=[]
    for L in range(lenght):#tester si grid_init utilisable
        res += [list( None for c in range(lenght))]
    for l in range(lenght) :
        for c in range(lenght) :
            res[l][c] = grid_get_value(grid,l,c)
    return res
                
    


def score(grid,lenght):
    """ Renvoie le score de la grille """
    res=0
    for l in range (lenght):
        for c in range (lenght):
            if grid[l][c]== None or grid[l][c]==2:
                res+=0
            else:
                  res+=grid[l][c]
    return res 


def save_score (grid,lenght):
    """ Permet la sauvegarde du score dans un fichier nommé score """
    with open('score','a') as s:
        s.write(str(lenght)+':' + str(input('Input your name'))+':'+ str(score(grid,lenght))+'\n')



def save_grid(grid):
    """ permet la sauvegarde de la grille dans un fichier nommé save-grid"""
    with open('save-grid','wb') as g:
        pickle.dump(grid,g)
        

def grid_load():
    """ permet de charger un fichier dans une partie """
    with open('save-grid','rb') as g:
        grid = pickle.load(g)
    return grid
       
    

def tri_score  (lenght):
    L=[]
    with open ('score','r') as s:
        txt=str(s.read())
        txtList=txt.split('.')
        for i in range (len(txtList)):
            if txtList[i][0]==str(lenght):
                L+=txtList[i]
        triTxT=sorted(L)
        if triTxT==[]:
            return 0
        else :
            return triTxT[-1]
            
        








    

        













    

        
