# magic method = dudner methods (double underscore) __init__, __str__, __eq__
#   they are automatically called by so many of python built in operations
#   they allow developers to define or customize the behavior of objects

class Fortnite:


    def __init__(self, weapon, shields, healing):
        self.weapon = weapon
        self.shields = shields
        self.healing = healing

    def __str__(self):
        return f"{self.weapon} and {self.shields}"
    
    def __eq__(self, other):
        return self.weapon == other.weapon and self.shields == other.shields
    
    def __lt__(self, other):
        return self.healing < other.healing
    
    def __gt__(self, other):
        return self.healing > other.healing
    
    def __add__(self, other):
        return self.healing + other.healing
    
        
    def __contains__(self, keyword):
        return keyword in self.weapon or keyword in self.shields
    
    def __getitem__(self, key):
        if key == 'weapon':
            return self.weapon
        


loadout = Fortnite('AR', '50 POT', 100)
loadout2 = Fortnite('pump', '50 POT', 50)
loadout3 = Fortnite('burst', 'chugsplash', 50)

print(loadout)
print (loadout == loadout2)
print (loadout < loadout2)
print (loadout > loadout2)
print(loadout + loadout3)
print('AR' in loadout)
print(loadout['weapon'])