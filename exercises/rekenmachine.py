principal = 0
rate = 0
time = 0

while True:
    principal = float(input('Enter principal amount: '))
    if principal <= 0:
        print('Principal mag niet lager zijn dan of gelijk aan 0.')
    else:
        break

while True:
    rate = float(input('Enter de rentepercentage: '))
    if rate <= 0:
        print('Rente mag niet 0 of lager zijn.')
    else:
        break

while True:
    time = int(input('Enter tijd in jaren: '))
    if time <= 0:
        print('Tijd mag niet 0 of lager zijn.')
    else:
        break

total = principal * pow((1 + rate / 100), time)
print(f'Saldo na {time} jaar: ${total:.2f}')
