from  car import *
import time
from grid import *
from copy import *
from queue import *

conf2=[car(0,0,"U",2,"G"),car(3,0,"L",3,"Y"),car(1,2,"R",2,"R"),car(3,2,"D",2,"O"),car(4,2,"U",2,"S"),car(5,1,"U",3,"V"),car(0,3,"L",3,"B"),car(4,4,"L",2,"L"),car(2,5,"D",2,"P"),car(3,5,"L",2,"D"),car(1,5,"R",2,"K")]


class game():


    def __init__(self,conf):
        """
        :return: a game configuration
        :rtype: list of cars
        :UC: None
        :Examples:
        >>> b=game(conf2)
        >>> s=b.get_conf()
        >>> b.__eq__(game(s))
        True
        >>> b.all_move_possible_grid()
        ['YL', 'RR', 'OD', 'SU', 'BR', 'LL', 'DR']
        >>> b.is_finalist()
        (False, '')
        """
        self.conf=conf

    def get_conf(self):
        """
        :return: configuration
        :rtype: list
        :UC: none
        """
        return self.conf

    def __eq__(self,other):
        """
        :return:  if two configuration of cars are equal
        :rtype: boolean
        :UC: none
        """
        return self.conf==other.conf

    def all_move_possible_grid(self):
        """
       
        :return: list of move possible for the configuration
        :rtype: list
        :UC: none
       
        """
        g=grid()
        g.add_configuration_cars(self.conf)
        cpt=0 
        ls=[]
        for i in self.conf :
            for j in range (len(g.move_possible_car(i))):
                ls.append("".join(g.move_possible_car(i)[j][0]))
        for j in ls :
            if j=="":
                ls.remove("")
                
        return ls

    def start_moving(self,move):
        """

        :return: a new  configuration after the move 
        :rtype: list 
        :UC: none

        """
        g=grid()
        g.add_configuration_cars(self.conf)
        cpt=0
        co=[]
        for c in self.conf:

            if c.get_couleur()==move[0]:
                for i in range(len(g.move_possible_car(c))):
                    if move==g.move_possible_car(c)[i][0] :
                        d=car(g.move_possible_car(c)[i][1][0],g.move_possible_car(c)[i][1][1],c.get_direction(),c.get_taille(),c.get_couleur())  
                co.append(d)        
            else:            
                co.append(c)       
        return co

    def start_moving_graphical(self,move):
        """

        :return: the same configuration edited after the move 
        :rtype: list 
        :UC: none

        """
        g=grid()
        g.add_configuration_cars(self.conf)
        cpt=0
        if game(self.conf).winner():
                return ("!!!!you wiiiin!!!")
        if move not in game(self.conf).all_move_possible_grid():
            return ("this move is impossible !!")
        for c in self.conf:

            if c.get_couleur()==move[0]:
                self.conf.remove(c)
                for i in range(len(g.move_possible_car(c))):
                    if move==g.move_possible_car(c)[i][0] :
                        d=car(g.move_possible_car(c)[i][1][0],g.move_possible_car(c)[i][1][1],c.get_direction(),c.get_taille(),c.get_couleur())  
        self.conf.append(d)        
                   
        return self.conf    
    def finding_red_car(self):
         """
         :return: the car of the color red
         :rtype: int
         :UC: none
         """
         for i in self.conf :
            if i.get_couleur()=="R" :
                return i 
         return i       

    def is_finalist(self):
        """

        :return: if the game is finished or not in a tuple with the number of move of the red car to the right 
        :rtype: tuple
        :UC: nNone

        """
        g=grid()
        g.add_configuration_cars(self.conf)
        cr=game.finding_red_car(self)
        d=[]
        if cr.get_position()==[(5,2),(4,2)]:
            return (True,d)
        if cr.get_direction()=="R" :
            x=cr.get_head_x()
        else :
            x=cr.get_head_x()+1

        
        for i in range(5-x):
            d.append("RR")     
        while x<5 :
            x+=1
            if g.grid[2][x]!=" " :
                return (False,"")
        return (True,d)

    def winner(self):
        """
        :return:  True if the user win False if not
        :rtype: boolean 
        :UC: none
        """
        l=game.finding_red_car(self)
        if l.get_position()==[(5,2),(4,2)]:
            return True
    def __hash__(self):
        """
        :return:  associate an unique  number for the  configuration 
        :rtype: int 
        :UC: none
        """
        s=0
        for i in self.conf :
            s= s+i.__hash__()
        return s              

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
