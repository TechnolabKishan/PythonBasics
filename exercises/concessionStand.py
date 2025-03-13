menu = {
    "popcorn": 4.50,
    "pizza": 2.50,
    "soda": 3.00,
    "lemonade": 1.50,
    "rucola": 6.00,
    "nachos": 3.50
}

cart = []
total = 0

print("---------- MENU ----------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("--------------------------")

while True:
    food = input('Kies uit wat je wilt (n om te stoppen): ').lower()
    if food == "n":  
        break
    if menu[food] is not None:
        cart.append(food)

print("----------- YOUR ORDER ---------------")
for food in cart:
    total += menu[food]
    print(food, end=' ')
print()

while True:
    itemVerwijderen = input('wil je je eten verwijderen? (Ja Of Nee): ').lower()
    
    if itemVerwijderen == "nee":
        break  
    
    if itemVerwijderen == "ja":
        itemVerwijderen = input("Welke eten wil je verwijderen ").lower()
        
        if itemVerwijderen in cart:
            cart.remove(itemVerwijderen)  
            total -= menu.get(itemVerwijderen)  
            print(f"{itemVerwijderen} je bestelling is verwijdered")
        else:
            print(f"{itemVerwijderen} bestaat niet")

    elif itemVerwijderen != "yes":
        print("typ normaal")

print("----------- FINAL ORDER ---------------")
for food in cart:
    print(food, end=' ')
print()

print(f"Totaal te betalen: ${total:.2f}")
