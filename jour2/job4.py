class Student:

    def __init__(self,__nom,__prenom,__numeroEtudiant,__credit,__level):
        self.__nom = __nom
        self.__prenom = __prenom
        self.__numeroEtudiant = __numeroEtudiant
        self.__credit = __credit
        __credit = 0
        __level = self.__student_eval()
        self.__level = __level
        
        

    def set_add_credits(self):


        try:

            if self.__credit > 0:
                return f"Le nombre de crédit de {self.__prenom} {self.__nom} est de {self.__credit} numéro etudiant {self.__numeroEtudiant}"
            else:
                return "Le montant doit être supérieur à 0"
        except:
            return "Vous devez choisir un nombre."
    
    def __student_eval(self):
        

        if self.__credit >= 90:
            return "Excellent !"
        elif self.__credit >= 80 and self.__credit < 90:
            return "Très bien."
        elif self.__credit >= 70 and self.__credit < 80:
            return "Bien."
        elif self.__credit >= 60 and self.__credit < 70:
            return "Passable."
        else:
            return "Tes nul à chier ! "
    def student_info(self):
        return f"Nom = {self.__nom}\n Prénom = {self.__prenom}\n Id = {self.__numeroEtudiant}\n Credit = {self.__credit}\n Niveau = {self.__level}"
        

student = Student("Bouaichi","Childebert",145,80,90)
print(student.set_add_credits())
print(student.student_info())
