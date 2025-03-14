# List comprehsension = A concise way to create lists in python
#                       compact and easier to read then traditional loops
#                       [expression for value in iterable if condition]


# doubles = []

# for x in range(1, 11):
#     doubles.append(x * 2)


# print(doubles)
# tradition loop

# doubles = [x * 2 for x in range(1, 11)]
# triples = [y * 3 for y in range(1, 11)]
# square = [z * z for z in range(1, 11)]

# print(square)

# fruits = ['áppel', 'banaan', "annas", 'sinsa']

# fruit_chars = [fruit[1] for fruit in fruits]

# print(fruit_chars)

# string

# numbers = [1, -2, 3, -4, 5, -6, 8, -7]

# postive_nums = [num for num in numbers if num >= 0]
# negative_nums = [num for num in numbers if num < 0]
# even_nums = [num for num in numbers if num % 2 == 0]
# odd_nums = [num for num in numbers if num % 2 == 1]



# print(postive_nums)
# print()
# print(negative_nums)
# print()
# print(even_nums)
# print()
# print(odd_nums)


# grades = [85, 42, 79, 90, 56, 61, 30]
# passing_Grads = [grade for grade in grades if grade >= 60 ]

# print(passing_Grads)


userGrade = {"Elmo": 70, 'Nd': 80, 'Blaaster': 75, "Chama": 40}

grade_name = input('What is your name? for your grade!: ')

if grade_name in userGrade:
    grade = userGrade[grade_name]
    if grade >= 60:
        print(f'{grade_name} Is a pro student with grade of {grade}')
    else:
        print(f'{grade_name} sucks ass with grade of {grade}')
else:
    print(f"{grade_name} was not found")

proStudent = {name: grade for name, grade in userGrade.items() if grade >= 60}

print(proStudent)