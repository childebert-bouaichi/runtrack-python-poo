class Rectangle:

    def __init__(self,__longueur,__largeur):
        self.__longueur = __longueur
        self.__largeur = __largeur
    
    def get_rectangle(self):
        return f"Longueur: {self.__longueur} Largeur: {self.__largeur}"
    
    def set_rectangle(self,longueur,largeur):
        self.__longueur = longueur
        self.__largeur = largeur
        
        return f"Nouvelle longueur: {self.__longueur} Nouvelle largeur: {self.__largeur}"

rectangle = Rectangle(10,5)
print(rectangle.get_rectangle())
print(rectangle.set_rectangle(20,10))