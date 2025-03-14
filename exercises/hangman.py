import random

words = ('Blaaster', 'Nd', 'Elmo', 'Daffyd', 'golmon', 'Ocean', 'Haxball', 'math')

hangmanArt = {
    0: (
        "   _______",
        "  |       |",
        "  |",
        "  |",
        "  |",
        "  |",
        "__|__"
    ),
    1: (
        "   _______",
        "  |       |",
        "  |       O",
        "  |",
        "  |",
        "  |",
        "__|__"
    ),
    2: (
        "   _______",
        "  |       |",
        "  |       O",
        "  |       |",
        "  |",
        "  |",
        "__|__"
    ),
    3: (
        "   _______",
        "  |       |",
        "  |       O",
        "  |      /|",
        "  |",
        "  |",
        "__|__"
    ),
    4: (
        "   _______",
        "  |       |",
        "  |       O",
        "  |      /|\\",
        "  |",
        "  |",
        "__|__"
    ),
    5: (
        "   _______",
        "  |       |",
        "  |       O",
        "  |      /|\\",
        "  |      /",
        "  |",
        "__|__"
    ),
    6: (
        "   _______",
        "  |       |",
        "  |       O",
        "  |      /|\\",
        "  |      / \\",
        "  |",
        "__|__"
    )
}

def display_man(wrong_Guesses):
    print('-----------------------------')
    for line in hangmanArt[wrong_Guesses]:
        print(line)
    print('-----------------------------')


def display_hint(hint):
    print(' '.join(hint))

def display_answer(answer):
    print(' '.join(answer))


def main():
    answer = random.choice(words).lower()
    hint = ["_"] * len(answer)
    wrong_Guesses = 0
    guessed_letters = set()
    is_running = True
    
    while is_running:
        display_man(wrong_Guesses)
        display_hint(hint)
        guess = input('enter a letter: ').lower()

        if guess in guessed_letters:
            print(f'{guess} You already guess it')
            continue
        guessed_letters.add(guess)

        if len(guess) != 1 or not guess.isalpha():
            print('invalid input')
            continue
        
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_Guesses += 1

        if "_" not in hint:
            display_man(wrong_Guesses)
            display_answer(answer)
            print("You have won")
            is_running = False
        elif wrong_Guesses >= len(hangmanArt) - 1:
            display_man(wrong_Guesses)
            display_answer(answer)
            print('You lose')
            is_running = False


if __name__ == '__main__':
    main()