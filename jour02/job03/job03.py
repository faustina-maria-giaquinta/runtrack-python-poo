class Rectangle:
    def __init__(self, largeur, longueur):
        self.__largeur = largeur
        self.__longueur = longueur
    
    def perimetre(self):
        return self.__largeur * 2 + self.__longueur * 2
    
    def surface(self):
        return self.__largeur * self.__longueur