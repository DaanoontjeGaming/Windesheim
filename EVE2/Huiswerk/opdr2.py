class Boek:
    def __init__(self, titel, auteur, jaar):
        self.titel = titel
        self.auteur = auteur
        self.jaar = jaar
        self.uitgeleend = False

    def leen_uit(self):
        self.uitgeleend = True
    
    def __str__(self):
        return f"Titel: {self.titel}, auteur: {self.auteur}, jaar: {self.jaar}, uitgeleend: {self.uitgeleend}."

boek1 = Boek("Boek", "onbekend", "onbekend")

print(boek1)
boek1.leen_uit()
print(boek1)