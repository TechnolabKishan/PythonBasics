import random

def spin_row():
    symbols = ["❤️ ",  "🍉 ", "🍒 ", "📞 ", "⭐ "]
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print('--------------')
    print(" | ".join(row))
    print('--------------')

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '❤️ ':
            return bet * 3
        elif row[0] == '🍉 ':
            return bet * 4
        elif row[0] == '🍒 ':
            return bet * 2
        elif row[0] == '📞 ':
            return bet * 30
        elif row[0] == '⭐ ':
            return bet * 100
    return 0
        
def main():
    while True:  
        balance = 100
        print('-----------------------')
        print('Welcome to Python Slots')
        print('Symbols: ❤️  🍉 🍒 📞 ⭐')
        print('-----------------------')

        while balance > 0:
            print(f'Current balance: ${balance}')
            
            
            action = input('Place your bet amount (or type "quit" to exit): ')
            
            if action.lower() == 'quit':  
                print(f'You left the game with ${balance}. Thanks for playing!')

                return  
            
            if not action.isdigit():  
                print('Please enter a valid number.')
                continue
            
            bet = int(action)
            
            if bet > balance:
                print('Not enough money!')
                continue
            if bet <= 0:
                print('Bet must be greater than 0.')
                continue
            
            balance -= bet

            print("Spinning...\n")
            row = spin_row()
            print_row(row)

            payout = get_payout(row, bet)
            if payout > 0:
                print(f'You won ${payout}! 🎉')
            else:
                print('You lost. Better luck next time!')
            
            balance += payout

        play_again = input('Do you want to play again? (y/n): ').lower()
        if play_again != 'y':
            print('\nYou lost all your money. Broke ahhhhhhhh!')
            break  

if __name__ == '__main__':
    main()