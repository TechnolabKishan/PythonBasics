# with wraps a block. open function return file object first parameter is file_path 
# w = write x = also write if the document doesnt exists a = append a file r = to read a file
#

import json
import csv

# employees = ['Saroj', 'Parwesh', 'Kishan', 'Rajnish']

# employee = {
#     'name': 'kishan',
#     'age': 18,
#     'job': 'haxball pro'
# }

employee = [['name', 'age', 'job'],
            ['Elmo', 18, 'IT Developer'],
            ['Nd', 28, 'Noob'],
            ['Blaaster', '24', 'Pro gk']]

file_path = 'C:/Users/Kisha/gibberish.csv'

try:
    with open(file=file_path, mode='w', newline='') as file:
        # json.dump(employee, file, indent=4)
        writer = csv.writer(file)
        for employees in employee:
            writer.writerow(employees)
        print(f'csv file `{file_path}` was created')
except FileExistsError:
    print('file already exists')
