class Human:
    """ Клас описує стать, вік, ім'я, прізвище людини"""

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} y.o."


class Student(Human):
    """ Клас Student описує стать, вік, ім'я, прізвище та номер залікової книжки студента"""

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.record_book}"


class Group:
    """Клас Group додає, видаляє студента, здійснює пошук студента за прізвищем.
    У випадку, якщо кількість студентів у групі перевищує 10, то виводиться помилка"""

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        try:
            if len(self.group) == 10:
                raise ValueError("Кількість студентів у групі не може бути більше 10!")
            else:
                self.group.add(student)
        except ValueError as e:
            print(e)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        self.group.discard(student)

    def find_student(self, last_name):
        for student in self.group:
            if last_name == student.last_name:
                return student
        return None

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += str(student) + "\n"
        return f'Number:{self.number}\n{all_students}'


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Female', 25, 'Ziza', 'Taylor', 'AN146')
st4 = Student('Female', 25, 'Piza', 'Taylor', 'AN147')
st5 = Student('Female', 25, 'Miza', 'Taylor', 'AN148')
st6 = Student('Female', 25, 'Niza', 'Taylor', 'AN149')
st7 = Student('Female', 25, 'Hiza', 'Taylor', 'AN150')
st8 = Student('Female', 25, 'Riza', 'Taylor', 'AN151')
st9 = Student('Female', 25, 'Giza', 'Taylor', 'AN152')
st10 = Student('Female', 25, 'Fiza', 'Taylor', 'AN153')
st11 = Student('Female', 25, 'Diza', 'Taylor', 'AN154')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)
gr.add_student(st11)

# print(gr)
# print(st1)
# print(st2)
#
# assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
# assert gr.find_student('Jobs2') is None, 'Test2'
# assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'
#
# gr.delete_student('Taylor')
# print(gr)  # Only one student
#
# gr.delete_student('Taylor')  # No error!
