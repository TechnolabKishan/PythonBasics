# List [] = most flexibale
# tuple () = mag niet meer veranderen/ faster
# set {} = mutable (add/remove), unorderd no 
#          duplicates for membership testing

# fruits = ["apple", 'orange', 'banana', 'coconut']

# fruits[3] = 'mango'
# fruits.append('mango')
# fruits.remove("banana")
# fruits.pop(0)
# fruits.clear()

# for i in fruits:
#     print(i, end=' ')

# fruits = ("apple", 'orange', 'banana', 'coconut') # kan niet meer veranderen

# for i in fruits:
#     print(i, end=' ')

fruits = {"apple", 'orange', 'banana', 'coconut'} # het is unodered

fruits.add('mango')
# fruits.remove('coconut')
# fruits.clear()

fruit = input('enter a fruit to search for: ')

if fruit in fruits:
    print(f'{fruit} was found')
else:
    print(f'{fruit} was not found')
