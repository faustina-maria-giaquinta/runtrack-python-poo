class Voiture:
    def __init__(self, marque, modele, annee, km):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__km = km
        self.en_marche = False

    def afficher_marque(self):
        return self.__marque

    def modifier_marque(self, nouveau_marque):
        self.__marque = nouveau_marque

    def afficher_modele(self):
        return self.__modele

    def modifier_modele(self, nouveau_modele):
        self.__modele = nouveau_modele

    def afficher_annee(self):
        return self.__annee

    def modifier_annee(self, nouveau_annee):
        self.__annee = nouveau_annee
    
    def afficher_km(self):
        return self.__km

    def modifier_km(self, nouveau_km):
        self.__km = nouveau_km
    
    def afficher_en_marche(self, afficher = False):
        if afficher:
            if self.en_marche:
                print("La voiture est en marche.")
            else:
                print("La voiture est éteinte.")
        return self.en_marche

    def modifier_en_marche(self, change_en_marche):
        self.en_marche = change_en_marche

    def demarrer(self):
        if not self.en_marche:
            self.en_marche = True

    def arreter(self):
        if self.en_marche:
            self.en_marche = False