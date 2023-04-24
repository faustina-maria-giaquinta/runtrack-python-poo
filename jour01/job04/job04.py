class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def se_presenter(self):
        print(f"Je suis {self.prenom} {self.nom}")

personne = Personne("Doe", "John")
personne.se_presenter()

personne = Personne("Dupond", "Jean")
personne.se_presenter()