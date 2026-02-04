class Produit:

    def __init__(self,nom,prixHT,tva):
        self.nom = nom
        self.prixHT = prixHT
        self.tva = tva

    def calculer_prix_ttc(self):
        return self.prixHT +(self.prixHT * self.tva / 100)

    def afficher(self):
        return f"Nom: {self.nom} prix: {self.calculer_prix_ttc()}"
produit = Produit("ordinateur",100,20)

print(produit.afficher())