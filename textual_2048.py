#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""

:author: FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>_

:date: 2017, march

"""

from game_2048lenght import *

commands = { "U" : "up", "L" : "left", "R" : "right", "D" : "down", "S" : "save", "LO":"load"}

def read_next_move():
    """
    read a new move

    :UC: none
    """
    move = input('Your Move ? ((U)p, (D)own, (L)eft, (R)ight, (S)ave), (LO)ad ').upper()
    while move not in commands:
        move = input('Your Move ? ((U)p, (D)own, (L)eft, (R)ight, (S)ave), (LO)ad').upper()
    return move

def play():
    """
    main game procedure
    
    """
    theme=ask_theme()
    lenght=read_grid_lenght()
    grid = grid_init(lenght)
    grid_print(grid,lenght,theme)
    while not is_grid_over(grid,lenght) and grid_get_max_value(grid,lenght) < 2048:
        test= copy(grid,lenght)
        move = read_next_move()
        if commands[move]=="save" :
            save_grid(grid)
            exit(0)
        elif commands [move]=="load":
            grid=grid_load(lenght)
        else : 
            grid_move(grid, commands[move],lenght)
        if get_new_position(grid,lenght) != [] and test != grid:
            grid_add_new_tile(grid,lenght)
        grid_print(grid,lenght,theme)
        print("Score :",score(grid,lenght))
    if grid_get_max_value(grid,lenght) == 2048:
        print("You Won !!")
        save_score(grid,lenght)
    else:
        print("You Lose ;-(")
        save_score(grid,lenght)


def usage():
    print('Usage : {:s}'.format(sys.argv[0]))
    exit(1)

if __name__ == '__main__':
    import sys

    play()
    exit(0)
