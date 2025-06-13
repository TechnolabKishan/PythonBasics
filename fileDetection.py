import os

file_path = 'C:\laragon\www\Dagco-randomizer'

if os.path.exists(file_path):
    print(f'The location {file_path} exists')\

    if os.path.isfile(file_path):
        print('thats a file')
    elif os.path.isdir(file_path):
        print('thats a dir')

else:
    print('that location doesnt exists')