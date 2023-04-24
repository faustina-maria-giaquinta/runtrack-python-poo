import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from job07.job07 import Livre as Parent_Class_Livre

class Livre(Parent_Class_Livre):
    def __init__(self, titre, auteur, n_pages):
        super().__init__(titre, auteur, n_pages)
        self.__disponible = True
    
    def verification(self, afficher = False):
        if afficher:
            if self.__disponible:
                print("Il est disponible.")
            elif not self.__disponible:
                print("Il n'est pas disponible.")
        else:
            return self.__disponible
    
    def emprunter(self):
        self.__disponible = False
    
    def rendre(self):
        if not self.verification():
            self.__disponible = True



if __name__ == "__main__":
    livre = Livre("L'Élégance du hérisson", "Muriel Barbery", 500)
    message = f"Le livre ajouté est {livre.afficher_titre()}, de {livre.afficher_auteur()}, {livre.afficher_n_pages()} pages. "
    
    print(message, end=''), livre.verification(afficher=True)
    livre.emprunter()
    print(message, end=''), livre.verification(afficher=True)