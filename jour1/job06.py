class  Animal:

    def __init__(self,age,prenom):
        self.age = age
        self.prenom = prenom
        age = 0
        prenom = ""
    
    def viellir(self):
        
        print(f"l'âge de l'animal: {self.age} ans")
        self.age = self.age + 1
    
    def nommer(self):
        self.prenom = "Leman Russ !"
        return f"l'animal se nomme {self.prenom}"
        
        #return f"l'âge de l'animal: {self.age}"
        
animal = Animal(0,"")
animal.viellir()
animal.viellir()
print(animal.nommer())

