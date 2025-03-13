fruits = ["apple", "kiwi", "banana"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "pig"]

boodschappen = [fruits, vegetables, meats]

# print(boodschappen) # dit is 1d

# print(boodschappen[1][1])  # twee omdat het 2d list is moet je ook twee kolomen aanwijzen

for category in boodschappen:
    for food in category:
        print(food, end=' ')
    print(category) # kijkt welke categorie het is 