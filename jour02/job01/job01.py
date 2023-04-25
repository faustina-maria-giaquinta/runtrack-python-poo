class Personne:
    def __init__(self):
        self.age: int = 14

    def afficher_age(self):
        print(self.age)

    def bonjour(self):
        print("Hello")
    
    def modifier_age(self, age):
        if type(age) == int:
            self.age = age

class Eleve(Personne):
    def __init__(self):
        super().__init__()

    def aller_en_cours(self):
        print("Je vais en cours.")
    
    def affichage_age(self):
        print(f"J'ai {self.age} ans")

    
class Professeur:
    def __init__(self, matiere):
        self.__matiere_enseignee = matiere

    def enseigner(self):
        print("Le cours va commencer.")


if __name__ == "__main__":
    personne_1 = Personne()
    eleve_1 = Eleve()
    
    personne_1.afficher_age()
    eleve_1.affichage_age()
# end main
