# format specifiers = {value:Flags} format a value on what 
#                                           flags are inserted

price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f'price 1 is ${price1:+}')
print(f'price 2 is ${price2:+}')
print(f'price 3 is ${price3:+}')