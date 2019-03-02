from car import *
class grid():
    def __init__(self):
        """
        :return: a new empty grid.
        :rtype: list of 6 list
        :UC: None
        :Examples:
        >>> b=grid()
        >>> b.check_configuration([car(0,0,"L",3,"Y"),car(3,0,"U",2,"X"),car(4,0,"U",3,"G")])
        (True, '')
        >>> b.add_configuration_cars([car(0,0,"L",3,"Y"),car(3,0,"U",2,"X"),car(4,0,"U",3,"G")])
        >>> b.draw_grid()
        *--*--*--*--*--*--*
        |Y |Y |Y |X |G |  |
        *--*--*--*--*--*--*
        |  |  |  |X |G |  |
        *--*--*--*--*--*--*
        |  |  |  |  |G |  
        *--*--*--*--*--*--*
        |  |  |  |  |  |  |
        *--*--*--*--*--*--*
        |  |  |  |  |  |  |
        *--*--*--*--*--*--*
        |  |  |  |  |  |  |
        *--*--*--*--*--*--*
        >>> b.add_car(car(5,5,"D",3,"N"))
        >>> b.draw_grid()
        *--*--*--*--*--*--*
        |Y |Y |Y |X |G |  |
        *--*--*--*--*--*--*
        |  |  |  |X |G |  |
        *--*--*--*--*--*--*
        |  |  |  |  |G |  
        *--*--*--*--*--*--*
        |  |  |  |  |  |N |
        *--*--*--*--*--*--*
        |  |  |  |  |  |N |
        *--*--*--*--*--*--*
        |  |  |  |  |  |N |
        *--*--*--*--*--*--*
        >>> b.move_possible_car(car(3,0,"U",2,"X"))
        [['XD', (3, 1)]]
        """

        self.grid= [[(" ")for i in range (6)] for j in range (6)]

    
    def add_car(self,a):
        """
        :return: the mistake in the configuration of the car if it exict or add it if there is no mistake  
        :rtype: boolean and str or just str
        :UC: none
        """
        if a.check_configuration_car()[0]==True:
            cpt=0
            for i in a.get_position():
                if self.grid[i[1]][i[0]]==" " :
                    cpt+=1
                else:
                    return print("erreur !! chauvechement de la voiture de  la couleur ",a.get_couleur()," !!")
            if cpt==a.get_taille():
                for i in a.get_position():
                    self.grid[i[1]][i[0]]=a.get_couleur()

        else:
            print("check the parametre",a.check_configuration_car()[1]," of the configuration car of color",a.get_couleur()," please !!!")
    
        
        
    def draw_grid(self):
        """
        :return: a grid 
        :rtype: str
        :UC: none
        """
        g=0
        print("*--"*6+"*" )
        for i in self.grid:
            s="|"
            for j in i:
                s+=str(j)+" |"
            g+=1
            if g==3:
                s=s[:len(s)-1]
                    
            print(s)
            print("*--"*6+"*" )
    def clean_grid(self):
        """
        :return: None, just clear the grid in paramètre 
        :rtype: None
        :UC: none
        """
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                self.grid[i][j]=" "

    def check_configuration(self,liste):
        """
        :return: if there is a mistake in the configuration and what is it
        :rtype: tuple 
        :UC: none
        """
        l=[]
        for i in liste :
           if i.get_couleur() not in l :
                l.append(i.get_couleur())
           else:
               return (False , "you can't add 2 cars of a same color !!!")
        for i in liste :
           if i.get_couleur()=="R" and i.get_head_y()!= 2 :
               return (False , "The red car must be in ligne 2 !!!")
            
        return (True ,"")
    

    def add_configuration_cars(self,liste):
        """
        :return: add the configuration to the grid or return the mistake in the configuration if it exict
        :rtype: str
        :UC: none
        """
        if self.check_configuration(liste)[0]==True:
           for i in liste :
               self.add_car(i)
        else :
           return self.check_configuration(liste)[1]
       
           
                    
    def move_possible_car(self,c):
        """
        :return:  list of the move possible of a car 
        :rtype: list
        :UC: none
        """
        l=[]
        var=c.get_direction()
        xh=c.get_head_x()
        yh=c.get_head_y()
        xt=c.get_position()[c.get_taille()-1][0]
        yt=c.get_position()[c.get_taille()-1][1]
        if var=="L" :
            if 6>xh-1>=0 and self.grid[yh][xh-1]==" ":
                l.append([c.get_couleur()+"L",(xh-1,yh)])
            if 6>xt+1>=0 and self.grid[yh][xt+1]==" ":
                l.append([c.get_couleur()+"R",(xh+1,yh)])
            return  l    
        if var=="R" :
            if 6>xt-1>=0 and self.grid[yh][xt-1]==" ":
                l.append([c.get_couleur()+"L",(xh-1,yh)])
            if 6>xh+1>=0 and self.grid[yh][xh+1]==" ":
                l.append([c.get_couleur()+"R",(xh+1,yh)])
            return  l    
        if var=="U" :
            if 6>yh-1>=0 and self.grid[yh-1][xh]==" ":
                l.append([c.get_couleur()+"U",(xh,yh-1)])
            if 6>yt+1>=0 and self.grid[yt+1][xt]==" ":
                l.append([c.get_couleur()+"D",(xt,yh+1)])
            return  l    
        if var=="D" :
            if 6>yt-1>=0 and self.grid[yt-1][xt]==" ":
                l.append([c.get_couleur()+"U",(xt,yh-1)])
            if 6>yh+1>=0 and self.grid[yh+1][xh]==" ":
                l.append([c.get_couleur()+"D",(xh,yh+1)])
            return  l    
           
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
           
