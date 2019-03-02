
from  car import *
import time
from grid import *
from solution import *
from copy import *
from queue import *
from game import *


conf2=[car(0,0,"U",2,"G"),car(3,0,"L",3,"Y"),car(1,2,"R",2,"R"),car(3,2,"D",2,"O"),car(4,2,"U",2,"S"),car(5,1,"U",3,"V"),car(0,3,"L",3,"B"),car(4,4,"L",2,"L"),car(2,5,"D",2,"P"),car(3,5,"L",2,"D"),car(1,5,"R",2,"K")]
conf1=[car(2,2,"R",2,"R"),car(3,3,"D",3,"B"),car(4,4,"L",2,"S"),car(4,5,"R",3,"K"),car(5,0,"U",3,"Y")]
conf40=[car(0,2,"D",3,"Y"),car(1,1,"U",2,"X"),car(2,0,"R",2,"G"),car(4,1,"D",2,"O"),car(2,2,"D",2,"P"),car(5,1,"U",3,"J"),car(4,2,"R",2,"R"),car(0,3,"L",3,"K"),car(3,3,"U",2,"V"),car(4,4,"L",2,"D"),car(2,5,"D",2,"N"),car(0,5,"L",2,"F"),car(4,5,"R",2,"H")]


def jeu():
    """
    jouer rush hour en textueal
    """
    var=input("veuillez choisir le niveau (1:biginner 2:medium 3:expert ) ")
    if var=="1" :
        cn=conf1
    elif var=="2" :
        cn =conf2
    elif var=="3" :
        cn=conf40
    else :
        jeu()
    g=grid()
    g.add_configuration_cars(cn)
    g.draw_grid()
    d=game(cn)
    while not d.winner():

        d=game(cn)
        mv=input("mouvement:(exp : 'YD'), idea: '?' , solve: S ,quitter:Q ")
        if mv=='?':
            print(solution1(game(cn))[0])
        elif mv.upper()=="S":
            print(solution1(game(cn)))
        elif mv.upper()=="Q" :
            c=input("etes vous sur de vouloir faire sa (O:oui N:non) ")
            if c.upper()=='O' :
                exit(0)

        else :
            d=game(cn)
            if mv.upper() not in d.all_move_possible_grid():
                print("le mouvement est impossible")
            else:
                cn=d.start_moving_graphical(mv.upper())
                g=grid()
                g.add_configuration_cars(cn)
                g.draw_grid()
    return ("bravo")      



jeu()
