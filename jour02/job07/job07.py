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

class BlackJack:
    def __init__(self):
        self.jeu = Jeu()
        self.jeu.melanger()
        self.main_joueur = []
        self.main_croupier = []

    def distribuer_cartes(self):
        for i in range(2):
            self.main_joueur.append(self.jeu.tirer_carte())
            self.main_croupier.append(self.jeu.tirer_carte())

    def total_main(self, main):
        total = 0
        as_count = 0
        for carte in main:
            if carte.valeur in ["Valet", "Dame", "Roi"]:
                total += 10
            elif carte.valeur == "As":
                as_count += 1
                total += 11
            else:
                total += int(carte.valeur)
        while total > 21 and as_count > 0:
            total -= 10
            as_count -= 1
        return total

    def afficher_mains(self):
        print("Votre main :")
        for carte in self.main_joueur:
            print(carte)
        print(f"Total : {self.total_main(self.main_joueur)}")
        print("\nMain du croupier :")
        print(self.main_croupier[0])
        print("Une carte cachée")

    def tour_joueur(self):
        while True:
            choix = input("Voulez-vous tirer une carte (t) ou passer (p) ? ")
            if choix.lower() == "t":
                self.main_joueur.append(self.jeu.tirer_carte())
                print("\nVotre main :")
                for carte in self.main_joueur:
                    print(carte)
                print(f"Total : {self.total_main(self.main_joueur)}")
                if self.total_main(self.main_joueur) > 21:
                    print("Vous avez dépassé 21 ! Vous avez perdu...")
                    return False
            elif choix.lower() == "p":
                return True
            else:
                print("Choix invalide ! Veuillez saisir 't' ou 'p'.")

    def tour_croupier(self):
        while self.total_main(self.main_croupier) < 17:
            self.main_croupier.append(self.jeu.tirer_carte())
        print("\nMain du croupier :")
        for carte in self.main_croupier:
            print(carte)
        print(f"Total : {self.total_main(self.main_croupier)}")
        if self.total_main(self.main_croupier) > 21:
            print("Le croupier a dépassé 21 ! Vous avez gagné !")
            return True
        elif self.total_main(self.main_croupier) >= self.total_main(self.main_joueur):
            print("Le croupier a une meilleure main que vous ! Vous avez perdu...")
            return False
        else:
            print("Vous avez une meilleure main que le croupier ! Vous avez gagné !")
            return True

    def jouer(self):
        print("Bienvenue au Blackjack !")
        self.distribuer_cartes()
        self.afficher_mains()
        if self.total_main(self.main_joueur) == 21:
            print("Blackjack ! Vous avez gagné !")
            return
        while self.tour_joueur():
            self.afficher_mains()
            if self.total_main(self.main_joueur) == 21:
                print("Blackjack ! Vous avez gagné !")
