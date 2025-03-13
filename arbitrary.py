# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#           * unpacking operator
#           1. Positional 2. default 3. keyword 4. arbitrary


# def add(*nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total
    
# print(add(1, 2, 3, 4))

# def display_name(*args):
#     for arg in args:
#         print(arg, end=' ')

# display_name("poop", "spongebob", "harold", "squarpants")

# def print_Adress(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")


# print_Adress(street= "123 fake st.", apt= 100, city="detroit", state="MI", zip= 54321)

def shipping_label(*args, **Kwargs):
    for arg in args:
        print(arg, end=' ')
    print()
    for key, value in Kwargs.items():
        print(f"{key}: {value}")

shipping_label('dr', 'spongebob', 'squarpants', 'III',
                street= "123 Fake St.", apt="100", city='detroit',
                state='MI', zip= '54321')