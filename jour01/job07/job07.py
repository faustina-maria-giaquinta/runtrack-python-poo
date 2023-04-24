class Livre:
    def __init__(self, titre, auteur, n_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__n_pages = n_pages

    def afficher_titre(self):
        return self.__titre

    def modifier_titre(self, nouveau_titre):
        self.__titre = nouveau_titre

    def afficher_auteur(self):
        return self.__auteur
    
    def modifier_auteur(self, nouveau_auteur):
        self.__auteur = nouveau_auteur

    def afficher_n_pages(self):
        return self.__n_pages
        
    def modifier_n_pages(self, nouveau_n_pages):
        if nouveau_n_pages > 0:
            self.__n_pages = nouveau_n_pages
        else:
            raise ValueError("Le nombre de pages donné est négatif. Merci de réessayer.")


if __name__ == "__main__":
    livre = Livre("L'Élégance du hérisson", "Muriel Barbery", 500)
    print(f"Le livre ajouté est {livre.afficher_titre()}, de {livre.afficher_auteur()}, {livre.afficher_n_pages()} pages.\n")
    print("Changer la valeur de la variable 'nombre de pages' (n_pages) avec une valeur positive:")

    livre.modifier_n_pages(410)
    print(f"Le livre ajouté est {livre.afficher_titre()}, de {livre.afficher_auteur()}, {livre.afficher_n_pages()} pages.\n")

    print("Changer la valeur de la variable 'nombre de pages' (n_pages) avec une valeur négative:")
    livre.modifier_n_pages(-10)
    print(f"Le livre ajouté est {livre.afficher_titre()}, de {livre.afficher_auteur()}, {livre.afficher_n_pages()} pages.")