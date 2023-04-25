class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix
        self.info_message = f"Marque = {self.marque}\nModel = {self.modele}\nAnnée = {self.annee}\nPrix = {self.prix}\n"

    def informations_vehicule(self):
        print(self.info_message)

    def demarrer(self):
        print("Attention, je roule !")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.portes: int = 4
        self.info_message += f"Nombre de porte = {self.portes}\n"
    
    def demarrer(self):
        print("Je démarre ma voiture.")
        super().demarrer()


class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roue: int = 2
        self.info_message += f"Nombre de roue = {self.roue}\n"
    
    def demarrer(self):
        print("Je démarre ma moto.")
        super().demarrer()

    
if __name__ == "__main__":
    vehicule_6 = Vehicule("Mercedes", "Classe A", 2020, 18500)
    vehicule_6.informations_vehicule()
    vehicule_6.demarrer()

    voiture_6 = Voiture("Mercedes", "Classe A", 2020, 18500)
    voiture_6.informations_vehicule()
    voiture_6.demarrer()

    moto_6 = Moto("Yamaha", "1200 Vmax", 1987, 4500)
    moto_6.informations_vehicule()
    moto_6.demarrer()