from human import Human


class Student(Human):
    """ Клас Student описує стать, вік, ім'я, прізвище та номер залікової книжки студента"""

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.record_book}"

    def compare_student(self, student):
        return str(student) == f"{self.first_name} {self.last_name}, {self.record_book}"
