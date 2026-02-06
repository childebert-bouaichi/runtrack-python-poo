class Livre:

    def __init__(self,__titre,__auteur,__nombrePage):
        self.__titre = __titre
        self.__auteur = __auteur
        self.__nombrePage = __nombrePage

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
                return "Vous ne pouvez choisir que des nombres."
                
libre = Livre("spaceHulk","GW",10)
print(libre.get_livre())
print(libre.set_livre("teste","lol",70))