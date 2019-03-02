
from tkinter import * 
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


dico=dict()
dico={"N":"dark green","H":"light blue","J":"dark red","X":"gold","D":"fuchsia","K":"violet","L":"lime","B":"turquoise","V":"brown","S":"gray","Y":"yellow","G":"green","C":"orange","I":"black","R":"red","P":"pink","F":"blue","O":"purple"," ":"white"}
var=[]
def main():
    """
    launch the graphical game
    
    UC : none
    """
    global fenetre,grid,text,value,entree
    fenetre = Tk()
    value = StringVar()
    value.set("votre mouvement exp:'YL'")
    entree = Entry(fenetre, textvariable=value, width=30)
    entree.grid(row=0)
    entree.bind("<Return>", move)
    Button(fenetre,text='beginner',width=10,command=beginner).grid(row= 1,column=0)
    Button(fenetre,text='medium',width=10,command=medium).grid(row= 2,column=0)
    Button(fenetre,text='expert',width=10,command=expert).grid(row= 3,column=0)
    Button(fenetre,text="idea!!",width=10,command=aide).grid(row= 5,column=0)
    for i in range (6):
        for j in range (7) :
            if i==2 and j==6 :
                Button(fenetre, text="sortie" , borderwidth=1,width=3,height=2,background="red").grid(row=i+1, column=j+1)
            elif j<6:    
                Button(fenetre, text="" , borderwidth=1,width=3,height=2,background="white").grid(row=i+1, column=j+1)
    Button(fenetre,text='solve',width=10,command=solve).grid(row= 4)
    text = Text(fenetre, width=30,height=10)
    text.grid(columnspan=7)
    fenetre.mainloop()

def beginner():
    """
    return :None
    this function add a configuration of a biginner to the grid
    UC: None
    """
    global grid, fenetre,var,v
    v=[car(2,2,"R",2,"R"),car(3,3,"D",3,"B"),car(4,4,"L",2,"S"),car(4,5,"R",3,"K"),car(5,0,"U",3,"Y")]
    var=v
    display(var)
    
def medium():
    """
    return :None
    this function add a medium configuration to the grid
    UC: None
    """
    global grid, fenetre,var,v
    v=[car(0,0,"U",2,"G"),car(3,0,"L",3,"Y"),car(1,2,"R",2,"R"),car(3,2,"D",2,"O"),car(4,2,"U",2,"S"),car(5,1,"U",3,"V"),car(0,3,"L",3,"B"),car(4,4,"L",2,"L"),car(2,5,"D",2,"P"),car(3,5,"L",2,"D"),car(1,5,"R",2,"K")]
    var=v
    display(var)
    
def expert():
    """
    return :None
    this function add a configuration of an expert to the grid
    UC: None
    """
    global grid, fenetre,var,text
    v=[car(0,2,"D",3,"Y"),car(1,1,"U",2,"X"),car(2,0,"R",2,"G"),car(4,1,"D",2,"O"),car(2,2,"D",2,"P"),car(5,1,"U",3,"J"),car(4,2,"R",2,"R"),car(0,3,"L",3,"K"),car(3,3,"U",2,"V"),car(4,4,"L",2,"D"),car(2,5,"D",2,"N"),car(0,5,"L",2,"F"),car(4,5,"R",2,"H")]
    var=v
    display(var)
def aide() :
    global fenetre,text,var
    f="*****"+""+solution1(game(var))[0]+""+"*****"
    text.delete(1.0,END)
    text.insert(END, str(f))
    
def solve():
    """
    return :None
    this function resolve the configuration showen in the grid and give the result as a text in a widget
    UC: None
    """
    global fenetre,text,var
    l=solution1(game(var))
    text.delete(1.0,END)
    text.insert(END, str(l))
def move(event):
    """
    this function edit the grid and show the new configuration resulted from the move chosen by th user
    and show message of imposible move or that you win
    UC:None
    """
    global grid ,var,value,entree,text
    if var!=[] :    
        c=game(var)
        cn=c.start_moving_graphical(entree.get().upper())
        if cn!= "this move is impossible !!" and cn!="!!!!you wiiiin!!!":
            text.delete(1.0,END)
            if game(cn).winner():
                t=("!!!!you wiiiin!!!")
                text.insert(END, t)
            var=cn
            display(cn)
        else:
            text.delete(1.0,END)
            text.insert(END,cn)
    else :
         y=("please chose a level")
         text.delete(1.0,END)
         text.insert(END, y)
        
def display(conf):
    """
    graphical grid display
    
    UC : none
    """
    global fenetre,grid
    g=grid()
    g.add_configuration_cars(conf)
    for i in range (6):
        for j in range (6) :
            Button(fenetre, text=g.grid[i][j] , borderwidth=1,width=3,height=2,background=dico[g.grid[i][j]]).grid(row=i+1, column=j+1)
    
class GridError(Exception):
    def  __init(self):
        self.msg= message
if __name__ == '__main__':
    import sys
    main()

    
