from care import Auto 

car1 = Auto('bmw', '2008', 'red', False)  
car2 = Auto('audi', '2010', 'blue', True)

print(car2.model)    
print(car2.year)    
print(car2.color)    
print(car2.for_Sale) 

car2.drive()
car2.stop()

car2.describe()