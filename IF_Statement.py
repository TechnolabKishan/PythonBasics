# age = int(input("enter your age: "))
# has_ticket = True;
# price = 10.00

# if age >= 65:
#     print('je bent oud')
#     print(f"jouw ticket omdat je oud bent is ${price * 0.75}")
# elif age >= 18:
#     print("je bent 18")
#     print(f'the ticket price is for an adult is ${price}')
# elif age < 0:
#     print('noob')
# else:
#     print("You are an Baby")
#     print(f"the ticket price for an child is ${price * 0.5}")

# if has_ticket:
#     print('nice noobio')
# else:
#     print("koop ticket noob")

# --------------------------------------------------------------------------------------

    # conditional expression = shortcut for if-else statement

num = 6
a = 6 
b = 7
age = 17
temp = 20
user_role = 'admin'

acces_level = "goodadmin" if user_role == 'admin' else 'not admin'

print(user_role)

Weather = 'HOT' if temp >= 25 else "poop"
print(Weather)

max_num = a if a > b else b
min_num = a if a < b else b

status = "adult" if age >= 18 else 'baby'

print(status)

print(max_num)
print(min_num)

# print('positive' if num < 5 else "negative")