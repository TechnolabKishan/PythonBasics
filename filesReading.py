import csv
import json

files_path = 'C:/Users/Kisha/gibberish.csv'

try:
    with open(file=files_path, mode= 'r') as file:
        content = csv.reader(file)
        for line in content:
            print(line[0])
        print(content)
except FileNotFoundError:
    print(f'that {files_path} was not found')
except PermissionError:
    print('you dont have premission to read that file')
