import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __repr__(self):
        return f"{self.valeur} de {self.couleur}"

class Jeu:
    def __init__(self):
        self.paquet = []
        self.construire_paquet()

    def construire_paquet(self):
        couleurs = ["Coeur", "Carreau", "Trèfle", "Pique"]
        valeurs = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]
        for couleur in couleurs:
            for valeur in valeurs:
                self.paquet.append(Carte(valeur, couleur))

    def melanger(self):
        random.shuffle(self.paquet)

    def tirer_carte(self):
        return self.paquet.pop()

