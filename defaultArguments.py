# default arguments = a default value for certrain parameters
#                     default is uded when that argument is omitted
#                 make your function more flexible, reduces # of arguments
#                 !. positional, 2. DEFAULT, 3. Keyword, 4. Arbitrary

import time

# def net_price(list_price, discount=0, tax=0.05):
#     return list_price * (1 - discount) * (1 + tax)

# print(net_price(200))
# print(net_price(500, 0.1))
# print(net_price(500, 0.1, 0))


def count(end, start=10):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print('DONE!')

count(40)
                   