class Operation:
    def __init__(self,nombre1,nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
    def show_number(self):
        print(f"Le nombre1 est: {self.nombre1}.\n le nombre2 est: {self.nombre2}.\n")  
    def addition(self):
        return f"Le résultat vaut: {self.nombre1 + self.nombre2}"      
test = Operation(10,20)
test.show_number()
print(test.addition())