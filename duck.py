# "Duck typing" = Another way to achieve polymorphism besides Inheritance
#    Object must have the minimum necessary attributes/methods
#    "If it looks like a duck and quacks like a duck, it must be a duck."

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print('WOof!')

class Cat(Animal):
    def speak(self):
        print('meow')

class Car(Animal):
    alive = False
    def speak(self):
        print('HONK')
        alive = False

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)  