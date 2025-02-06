#Maken van een student klasse

class Student:
    def __init__ (self, naam, nummer, leeftijd):
        self.name = naam
        self.nmr = nummer
        self.age = leeftijd
    
    def verjaardag(self):
        self.age += 1
    def __str__(self):
        return f"Naam student: {self.name}, Studentennummer: {self.nmr}, Leeftijd: {self.age}"

student1 = Student("Daan", 1213186, 21)
print(student1)
