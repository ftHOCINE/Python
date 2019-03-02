from  car import *
import time
from grid import *
from random import *
from copy import *
from queue import *
from game import *
conf4=[car(2,2,"R",2,"R"),car(0,1,"U",3,"I"),car(3,1,"U",3,"Y"),car(1,0,"R",2,"G"),car(5,0,"U",3,"C"),car(5,4,"R",2,"F"),car(4,5,"R",3,"P"),car(0,4,"U",2,"O")]
conf2=[car(0,0,"U",2,"G"),car(3,0,"L",3,"Y"),car(1,2,"R",2,"R"),car(3,2,"D",2,"O"),car(4,2,"U",2,"S"),car(5,1,"U",3,"V"),car(0,3,"L",3,"B"),car(4,4,"L",2,"L"),car(2,5,"D",2,"P"),car(3,5,"L",2,"D"),car(1,5,"R",2,"K")]
conf1=[car(2,2,"R",2,"R"),car(3,3,"D",3,"B"),car(4,4,"L",2,"S"),car(4,5,"R",3,"K"),car(5,0,"U",3,"Y")]
conf3=[car(0,0,"U",2,"G"),car(5,0,"R",3,"Y"),car(1,1,"L",2,"O"),car(1,2,"R",2,"R"),car(2,3,"D",2,"P"),car(3,2,"D",2,"S"),car(3,3,"L",2,"Z"),car(5,2,"U",3,"K"),car(2,5,"D",2,"F"),car(3,4,"L",2,"B"),car(5,5,"R",3,"C")]
conf5=[car(3,2,"R",2,"R")]
conf38=[car(0,0,"U",2,"G"),car(5,0,"R",3,"Y"),car(1,1,"L",2,"O"),car(1,2,"R",2,"R"),car(3,2,"D",2,"B"),car(2,3,"D",2,"P"),car(3,3,"L",2,"V"),car(3,4,"L",2,"D"),car(2,5,"D",2,"M"),car(5,5,"R",3,"K"),car(5,2,"U",3,"Z")]
conf39=[car(2,0,"U",2,"G"),car(3,0,"L",3,"Y"),car(3,1,"U",2,"O"),car(1,2,"R",2,"R"),car(2,3,"D",2,"B"),car(4,3,"R",2,"M"),car(0,4,"U",2,"K"),car(1,5,"D",2,"I"),car(3,4,"R",2,"F"),car(2,5,"L",2,"N"),car(5,4,"D",2,"V"),car(0,3,"L",2,"P")]
conf40=[car(0,2,"D",3,"Y"),car(1,1,"U",2,"X"),car(2,0,"R",2,"G"),car(4,1,"D",2,"O"),car(2,2,"D",2,"P"),car(5,1,"U",3,"J"),car(4,2,"R",2,"R"),car(0,3,"L",3,"K"),car(3,3,"U",2,"V"),car(4,4,"L",2,"D"),car(2,5,"D",2,"N"),car(0,5,"L",2,"F"),car(4,5,"R",2,"H")]
confl=[car(0,0,"L",3,"Y"),car(3,0,"U",2,"X"),car(4,0,"U",3,"G"),car(5,0,"U",3,"O"),car(0,1,"U",2,"P"),car(1,1,"L",2,"J"),car(3,2,"R",2,"R"),car(1,3,"R",2,"K"),car(2,3,"U",2,"V"),car(1,4,"U",2,"D"),car(5,4,"R",2,"N"),car(2,5,"L",2,"F"),car(4,5,"L",2,"H")]
def solution1(conf):
    """

    :return:  the solution of the configuration passed on paramètre and the time that it taks to found it
    :rtype: tuple  
    :UC: none
    :Examples:
    >>> g=game(conf39)
    >>> solution1(g)
    ['FR', 'BD', 'RR', 'VU', 'FR', 'VU', 'MR', 'OD', 'OD', 'RR', 'RR', 'GD', 'YL', 'VU', 'RR']
    """
    q=Queue()
    q.put(conf)
    dico=dict()
    dico[conf]= []
    debut=time.time()
    if conf.is_finalist()[0]:
        return conf.is_finalist()[1]
    while not q.empty() :
        c = q.get()
        l= c.all_move_possible_grid()
        for move in l:
            co= c.start_moving(move)
            d=game(co)
            if d.is_finalist()[0]:
                dico[d]=dico[c]+[move]+d.is_finalist()[1]
                fin=time.time()
                return dico[d]
            if d not in dico :
                dico[d]=dico[c]+[move]
                q.put(d)
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
