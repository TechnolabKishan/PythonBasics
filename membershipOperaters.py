# membership operaters = used to test whether a value or variable 
# is found in a sequence
#(string, list = [], tuple (), set {}, or dictionary)
#                1. in
#                2. not in

# word = 'Apple'

# letter = input('guess a letter in the secret word: ')

# if letter in word: 
#     print(f'there is a {letter}')
# else:
#     print(f'{letter} was not found')


# if letter not in word: # not in check je eerst iets niet in is bij de andere andersom
#     print(f'{letter} was not found')
# else:
#     print(f'there is a {letter}')

# students = {'Elmo', "Nd", 'Blaaster'}

# student = input('Enter a name of a student: ')

# if student in students:
#     print(f'We have found {student}')
# else:
#     print(f'{student} was not found')

# grades = {'Elmo': 10, "Blaaster": 8.5, 'Nd': 5}

# student = input('Enter the name of a Student: ')

# if student in grades:
#     print(f'{student}`s grade is {grades[student]}')
#     if grades[student] < 6:
#         print(f"{student} is very bad in Math")
# else:
#     print(f'{student} was not found')


email = input('Type your Email: ')

if "@" in email and "." in email:
    print('valid email')
else:
    print('invalid email')