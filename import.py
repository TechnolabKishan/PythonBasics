import random

low = 1
high = 100
options = ('rock', 'paper', 'scizssors')
cards = ['2','3','4','5','6','7','8','9','q','j','10','f',]

# number = random.randint(low, high)
# number = random.random()
random.shuffle(cards)

option = random.choice(options)

print(cards)