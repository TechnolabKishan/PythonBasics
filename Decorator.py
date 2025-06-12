# Decorator = a function that extends the behavior of another function
# w/o modifying the base function
# pass the base function as an argument to the decorator
# @add_sprinkles
# get_ice_cream('vanilla')

def add_ants(func):
    def wrapper(*args, **kwargs):
        print('*You add nd to the team*')
        func(*args, **kwargs)
    return wrapper

def add_blaaster(func):
    def wrapper(*args, **kwargs):
        print('*you add luciano to the team*')
        func(*args, **kwargs)
    return wrapper


@add_ants
@add_blaaster
def haxball_player(player):
    print(f'here is {player}')

haxball_player('My_rulez')