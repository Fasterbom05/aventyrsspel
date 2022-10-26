import random

#En liten kommentar :)

Huset = ["Barathoen", "Stark", "Lannister", "Tyrell", "Martell", "Tully", "Arryn", "Targaryen"]     #Vilken familj (kungarike) du föds in i väljs här!

Huset = random.choice(Huset)  
#Väljer hus av listan Huset

def välj_styrka(Huset):
    if Huset == "Barathoen" or "Stark":
        styrka = 10
    elif Huset == "Lannister" or "Tyrell" or "Martell":
        styrka = 7
    elif Huset == "Tully" or "Arryn":
        styrka = 4
    else:
        styrka = 11
    return styrka
    #Väljer din styrka beroende på ditt hus

class Person():
    def __init__(self, namn, nivå, kön, roll):
        self.namn = namn
        self.nivå = nivå
        self.kön = kön 
        self.roll = roll
        self.HP = 100
        self.hus = Huset
        self.styrka = välj_styrka(self.hus)
        
    def __str__(self):
        return f"Du är {self.namn} av huset {self.hus} och har styrkan {self.styrka}"


Huvudperson = Person("Andreas", 1, "Man", "Kungavakt")
 
print(Huvudperson)