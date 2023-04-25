class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informations_vehicule(self):
        print(f"{self.marque} {self.modele} ({self.annee}) - {self.prix} ")

