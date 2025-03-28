# inheritance = allows a class to inherit attributes and methodes from
#               another classs helps with code resuability and
#               extensibility class sub(classes)

class Animal:
    def __init__ (self, name):
        self.name = name
        self.is_alive = True

    def eating(self):
        print(f'{self.name} is eating')

    def sleep(self):
        print(f'{self.name} is sleeping!')


class Dog(Animal):
    def speak(self):
        print('WOOF')

class Cat(Animal):
    def speak(self):
        print('MEOW')

class Mouse(Animal):
    def speak(self):
        print('SQUEEK')

dog = Dog('Lukus')
cat = Cat('Garfield')
mouse = Mouse('Micky')

# print(mouse.name)
# print(mouse.is_alive)
# mouse.eating()
# mouse.sleep()

mouse.speak()