import random

option = ('rock', 'paper', 'scissors')
running = True

while running:

    computer = random.choice(option)
    player = None

    while player not in option:
        player = input("Enter your choice (rock, paper, scissors): ").lower()

    print(f'Player: {player}')
    print(f'Computer: {computer}')

    if player == computer:
        print("It's a tie!")
    elif player == 'rock' and computer == 'scissors':
        print('You win!')
    elif player == 'paper' and computer == 'rock':
        print('You win!')
    elif player == 'scissors' and computer == 'paper':
        print('You win!')
    else:
        print("You lost!")

    if not input("Play again? (y/n): ").lower() == 'y':
        break

print("Thanks for playing!")
