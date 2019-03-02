



class car():


    def __init__(self , head_x, head_y ,direction, taille,coleur):
        
        """
        :return: a car with a valid configuration
        :rtype: Car
        :UC: 0<=head_x<=5 , 0<=head_y<=5 , 1<taille<4 , direction='U' or direction='D' or direction='L' or direction='R' 
        :Examples:
        >>> C=car(2,5,"L",2,"F")
        >>> C.get_head_x()
        2
        >>> C.get_head_y()
        5
        >>> C.get_taille()
        2
        >>> C.get_cordinate_head()
        (2, 5)
        >>> C.get_couleur()
        'F'
        >>> C.get_direction()
        'L'
        >>> C.get_position()
        [(2, 5), (3, 5)]
        >>> C.check_configuration_car()
        (True, 0)
        """
        self.head_x = head_x
        self.head_y = head_y
        self.direction = direction
        self.t = taille
        self.c= coleur

        
    def get_head_x(self):
       """
       :return: cordinate x of the head of the car
       :rtype: int
       :UC: none
       """
       return self.head_x

    def get_head_y(self):
        """
        :return: cordinate y of the head of the car
        :rtype: int
        :UC: none
        """
        return self.head_y
    def get_taille(self):
        
        """
        :return: The length of the car
        :rtype: int
        :UC: none
        """
        return self.t
    def get_cordinate_head(self):
        """
        :return: cordinate of the head of the car
        :rtype: int
        :UC: none
        """ 
        return (self.head_x , self.head_y) 
    def get_couleur(self):
        """
        :return: the color of the car
        :rtype: str
        :UC: none
        """ 
        return self.c
    def get_direction(self):
        """
        :return: the direction of the car's head
        :rtype: int
        :UC: none
        """ 
        return self.direction
    def get_position(self):
        """
        :return:  the cordinate of the cels occuped by the car
        :rtype: list of tuple
        :UC: none
        """ 
        if self.direction=="U" :
            if self.t== 2:
                return [(self.head_x,self.head_y) , (self.head_x,self.head_y+1)]
            return [(self.head_x,self.head_y) , (self.head_x,self.head_y+1),(self.head_x,self.head_y+2)]
        if self.direction=="D" :
            if self.t== 2:
                return [(self.head_x,self.head_y) , (self.head_x,self.head_y-1)]
            return [(self.head_x,self.head_y) , (self.head_x,self.head_y-1),(self.head_x,self.head_y-2)]
        if self.direction=="L"  :
            if self.t== 2:
                return [(self.head_x,self.head_y) , (self.head_x+1,self.head_y)]
            return [(self.head_x,self.head_y) , (self.head_x+1,self.head_y),(self.head_x+2,self.head_y)]  
        if self.direction=="R" :
            if self.t== 2:
                return [(self.head_x,self.head_y) , (self.head_x-1,self.head_y)]
            return [(self.head_x,self.head_y) , (self.head_x-1,self.head_y),(self.head_x-2,self.head_y)]
    def check_configuration_car(self):
        
        """
        :return: if it's a correcte configuration of car and the position of the mistake in parametrs of the car if not
        :rtype: tuple 
        :UC: none
        """ 
        if self.t!=2 and self.t!=3 :
            return (False,"4")
        if self.direction!="U" and self.direction!="D" and self.direction!="L" and self.direction!="R" :
            return (False,"3")
        for i in self.get_position() :
            
            if i[0]>5 or i[0]<0 or i[1]<0 or i[1]>5 :
                return (False,"1 and 2")    
        return (True,0)    

    def __eq__(self,other):
        """
        :return:  if two cars are equal
        :rtype: boolean
        :UC: none
        """
        return (self.head_x,self.head_y,self.c)==(other.head_x,other.head_y,other.c)

    def __hash__(self):
        """
        :return:  associate an unique  number for the car 
        :rtype: int 
        :UC: none
        """
        return hash(self.c)*self.head_x<<self.head_y
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
