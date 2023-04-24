class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def afficher_longueur(self): #get_length
        return f"La longueur du rectangle créé est {self.__longueur}"
        
    def modifier_longueur(self, longueur):
        self.__longueur = longueur

    def afficher_largeur(self): #get_width
        return f"La largeur du rectangle créé est {self.__largeur}"
        
    def modifier_largeur(self, largeur):
        self.__largeur = largeur
    

rectangle = Rectangle(10, 15)

print(rectangle._Rectangle__longueur) # name mangling
rectangle.modifier_longueur(20)
print(rectangle.afficher_longueur())

print(rectangle._Rectangle__largeur) # name mangling
rectangle.modifier_largeur(4)
print(rectangle.afficher_largeur())

# not callable
print(rectangle.__largeur)
print(rectangle.__longueur)