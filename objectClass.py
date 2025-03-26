# class variables = shared among all instances of a class'
#                   defined outside the constructor
#                   Allow you to share data among all objects created from that class

class Student:

    class_year = 2026
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student('kishan', 18)
student2 = Student('patrick', 35)
student3 = Student('squidward', 55)
student3 = Student('rotonde', 25)


print(f"{student1.name} is {student1.age} and will be gradueting in {Student.class_year} and his class is also big with like {Student.num_students} in it")