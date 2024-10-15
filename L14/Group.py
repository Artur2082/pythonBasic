class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) < 10:
            self.group.add(student)
        else:
            raise TooManyStudents('Чисельність студентів у групі не може бути більше 10')

    def delete_student(self, last_name):
        stud = self.find_student(last_name)
        self.group.discard(stud)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student

    def __str__(self):
        all_students = "\n".join(str(student) for student in self.group)
        return f'Number:{self.number}\nStudents:\n{all_students} '


class TooManyStudents(Exception):

    def __init__(self, message):
        super().__init__()
        self.message = message

    def get_exception_message(self):
        return self.message
