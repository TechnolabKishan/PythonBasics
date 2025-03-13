questions = (
    "How tall is Elmo?", 
    "How old is Elmo?", 
    "What is Elmo's favorite club?", 
    "Who is smarter, Decayy or Elmo?",
    "Is Fairy Tail winning vs Fear?"
)

options = (
    ("A. 170cm", "B. 165cm", "C. 190cm", "D. 167cm"),
    ("A. 12 years old", "B. 15 years old", "C. 17 years old", "D. 18 years old"),
    ("A. FC Barcelona", "B. Ajax", "C. Liverpool", "D. FC Ajaccio"),
    ("A. Decayy", "B. Elmo"),
    ("A. YES", "B. NO")
)

answers = ("B", "D", "A", "B", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------------")
    print(question)

    for option in options[question_num]: 
        print(option)
    guess= input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print('CORRECT')
    else:
        print('INCORRECT!')
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1  

print("-------------------------")
print("        RESULTS          ")
print("-------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for gues in guesses:
    print(gues, end=' ')
print()

score = int(score / len(questions) * 100)
print(f'your score is: {score}%')