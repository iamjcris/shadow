#Class methods = Allow operations related to the class itself
# Take (cls) as first parameter, which represents class itself

#instance method = best operations on instance of the class (objects)
#class methods = Best for class-level data or require access to the class itself
#static methods = best for utility functions that do not need access to class data

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    def get_info(self):
        return f'{self.name} {self.gpa}'

    @classmethod
    def get_count(cls):
        return f'\nTotal Number of Students: {cls.count}'

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f'Average GPA: {cls.total_gpa / cls.count:.2f}'

student1 = Student('Hen', 2.5)
student2 = Student('Zyr', 2.0)
student3 = Student('Joseph', 1.0)

print(Student.get_count())
print(Student.get_average_gpa())




