class Personnage:

    def __init__(self,nom,prenom):
        self.nom = nom
        self.prenom = prenom

    def sePresenter(self):
        return f"Je suis: {self.prenom} {self.nom}."
personne = Personnage("Bouaichi","Childebert")
print(personne.sePresenter())