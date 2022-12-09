from Item import *

#------------------------------------------------------------------

class Person():
    def __init__(self, namn, nivå, kön, roll, huset, styrka):
        self.namn = namn
        self.nivå = nivå
        self.xp = 0
        self.kön = kön 
        self.roll = roll
        self.HP = 100
        self.hus = huset
        self.styrka = styrka
        self.ryggsäck = []

    def print_items(Huvudperson, Item_konsumerbart, Item_vapen):
        items = ""
        for sak in Huvudperson.ryggsäck:
            items = items + sak + " ," + str(Item_konsumerbart) + " ,"
        
        return items
        # for sak in Huvudperson.ryggsäck:
        #     print(sak)



#Håller alla stats för personen som spelar

    def __str__(self):
        return f"Du är {self.namn} nivå [{self.nivå}] av huset {self.hus} och har styrkan [{self.styrka}]"
#Gör så att man ser ett string när man printar Huvudperson istället för ett konstigt medelande


