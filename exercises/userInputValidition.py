username = input('TYPE YOUR USERNAME: ')


if len(username) > 12:
    print('Mag niet he')
elif not username.find(' ') == -1:
    print('your username cant contain spaces')
elif not username.isalpha():
    print('your username cant be digit')

else:
    print(f'welcome {username}')

