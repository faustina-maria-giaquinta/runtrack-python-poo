class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.__largeur = largeur
        self.__hauteur = hauteur
    
    def aire(self):
        return self.__hauteur * self.__largeur


if __name__ == "__main__":
    rectangle = Rectangle(10, 15)

    print(rectangle.aire())
# end main