# return = statement used to end a function
    # and send a result back to the caller

# def add(x, y):
#     z = x + y
#     return z

# def subtraction(x, y):
#     z = x - y
#     return z

# def multiply(x, y):
#     z = x * y
#     return z

# def divide(x, y):
#     z = x / y
#     return z

# print(add(1, 2))
# print(subtraction(1, 2))
# print(multiply(1, 2))
# print(divide(1, 4))

def createName(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = createName('blaaster', 'Vigniley')

print(full_name)