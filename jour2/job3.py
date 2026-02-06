class Livre:

    def __init__(self,__titre,__auteur,__nombrePage,__disponible):
        self.__titre = __titre
        self.__auteur = __auteur
        self.__nombrePage = __nombrePage
        self.__disponible = __disponible
        __disponible  = True

    def verification(self):
        
        if self.__disponible == False:
            return False
        else:
            return True
    
    def emprunter(self):
        
        if self.verification():
            print("Vous avez emprunter le livre par un tiers. le livre est maintenant indisponible en stock.")
            
            
        else:
            print("Le livre est disponible en stock inutile d'emprunter à un tiers.")

    def rendre(self):
        if self.verification() == False:
            print("La personne qui a emprunté le livre la rendu.")
            
        else:
            print("La personne na pas encore rendu le livre.")
            
    def get_livre(self):
        return f"titre du livre: {self.__titre},nom de l'auteur: {self.__auteur}, nombre de page: {self.__nombrePage}"

    def set_livre(self,titre,auteur,nombrePage):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombrePage = nombrePage
        try:

            if nombrePage > 0:
                return f"Nouv titre du livre: {self.__titre},Nouv nom de l'auteur: {self.__auteur}, Nouv nombre de page: {self.__nombrePage}"
            else:
                print("Le nombre de page doit être supérieur à 0")
        except:
                print("Vous ne pouvez choisir que des nombres entier est positif.")
livre = Livre("Space Hulk","GW",50,False)
livre.emprunter()
livre.rendre()
