# object_file.py
from care import Auto 

# Create objects of the Auto class
car1 = Auto('bmw', '2008', 'red', False)  
car2 = Auto('audi', '2010', 'blue', True)

print(car2.model)    
print(car2.year)    
print(car2.color)    
print(car2.for_Sale) 

car2.stop()