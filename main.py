# 9-m
class Teacher:
    def __init__(self, name, subject, salary):
        self.name = name
        self._subject = subject
        self.__salary = salary

    def teach(self, hours):
        print(f"Teaching {hours} hours")

    def increase_salary(self, x):
        self.__salary += x

    def info(self):
        print(f"Salary:{self.__salary}")

teacher = Teacher("Ali", "Math", 1000)
teacher.teach(2)
teacher.increase_salary(200)
teacher.info()
