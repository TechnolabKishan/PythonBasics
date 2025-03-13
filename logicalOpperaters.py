# temp = 20
# is_Raining = False

# if temp > 35 or temp < 0 or is_Raining: //bij or moet tenminste condition true zijn//
#     print('the outdoor event is cancelled')
# else:
#     print('the outdoor is still going')

temp = 10 #and moet allebij antwoorden true zijn anders is het fout
is_Sunny = False

if temp >= 28 and is_Sunny:
    print('its hot outside😊😂')
    print('it is SUNNY ❤️❤️🙌')
elif temp <= 0 and is_Sunny:
    print('its cold outside')
    print('and its sunny')
elif 28 > temp > 0 and is_Sunny:
    print('oke het begint wat kouder te worden')
elif temp >= 28 and not is_Sunny:
    print('its hot outside😊😂1')
    print('it is SUNNY ❤️❤️🙌1')
elif temp <= 0 and not is_Sunny:
    print('its cold outside1')
    print('and its sunn1y')
elif 28 > temp > 0 and not is_Sunny: # bij not kijkt of het niet true of not false
    print('oke het begint wat kouder te worden1')

