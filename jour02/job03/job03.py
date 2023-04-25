import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from jour01.job06.job06 import Rectangle as Rct

class Rectangle(Rct):
    def __init__(self, largeur, longueur):
        self.__largeur = largeur
        self.__longueur = longueur
    
    def perimetre(self):
        return self.__largeur * 2 + self.__longueur * 2
    
    def surface(self):
        return self.__largeur * self.__longueur

class Parallelepipede(Rectangle):
    def __init__(self, hauteur):
        super().__init__()
        self.__hauteur = hauteur

    def afficher_longueur(self):
        return f"La longueur du parallélépipèdengle créé est {self.__longueur}"
        
    def afficher_largeur(self): 
        return f"La largeur du parallélépipède créé est {self.__largeur}"

    def afficher_hauteur(self):
        return f"La hauteur du parallélépipède créé est {self.__hauteur}"
        
    def modifier_hauteur(self, hauteur):
        self.__largeur = largeur
    
    def volume(self):
        return self.__largeur * self.__longueur * self.__hauteur

if __name__ == "__main__":
    rectangle = Rectangle(10, 15)

    print(rectangle._Rectangle__longueur) # name mangling
    rectangle.modifier_longueur(20)
    print(rectangle.afficher_longueur())

    print(rectangle._Rectangle__largeur) # name mangling
    rectangle.modifier_largeur(4)
    print(rectangle.afficher_largeur())