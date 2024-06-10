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
