# keyword arguments = a default value for certrain parameters
#                     default is uded when that argument is omitted
#                 make your function more flexible, reduces # of arguments
#                 !. positional, 2. DEFAULT, 3. Keyword, 4. Arbitrary

# def hello(greeting, titel, first, last):
#     print(f'{greeting} {titel} {first} {last}')

# hello("Hello", titel="Mr", last="jan", first="james")

def get_phone(country, area, first, last):
    return(f"{country}-{area}-{first}-{last}")
phone_num = get_phone(country=1, area=123, first=456, last=7890)
print(phone_num)