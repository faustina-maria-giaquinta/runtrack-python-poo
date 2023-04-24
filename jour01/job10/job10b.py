import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from job10a import Voiture as Parent_Class_Voiture

class Voiture(Parent_Class_Voiture):
    def __init__(self, marque, modele, annee, km):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__km = km
        self.__reservoir = 50
        self.en_marche = False

    def modifier_reservoir(self, nouveau_reservoir):
        self.__reservoir = nouveau_reservoir
    
    def afficher_reservoir(self):
        return self.__reservoir

    def __verifier_plein(self):
        return self.__reservoir
    
    def demarrer(self):
        if not self.en_marche and self.__verifier_plein() > 5:
            self.en_marche = True


if __name__ == "__main__":
    voiture = Voiture("Ferrari", "Roma", 2021, 200)

    print(f"Cette voiture est un {voiture.afficher_marque()} {voiture.afficher_modele()} {voiture.afficher_annee()} ({voiture.afficher_km()} km).")

    voiture.afficher_en_marche(afficher=True)
    voiture.demarrer()
    voiture.afficher_en_marche(afficher=True)
    
    voiture.arreter()
    voiture.afficher_en_marche(afficher=True)

    voiture.modifier_reservoir(2)
    voiture.demarrer()
    voiture.afficher_en_marche(afficher=True)

    