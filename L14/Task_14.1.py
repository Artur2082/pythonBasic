class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, gender {self.gender}, age {self.age} yrs"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, record_book {self.record_book}"


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


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr, '\n')
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr, '\n')  # Only one student
gr.delete_student('Taylor')  # No error!
gr.add_student(st2)
st3 = Student('F', 26, 'St3', 'A', '01')
st4 = Student('M', 27, 'St4', 'B', '02')
st5 = Student('F', 28, 'St5', 'C', '03')
st6 = Student('M', 29, 'St6', 'D', '04')
st7 = Student('F', 30, 'St7', 'E', '05')
st8 = Student('M', 31, 'St8', 'F', '06')
st9 = Student('F', 25, 'St9', 'G', '07')
st10 = Student('M', 29, 'St10', 'H', '08')
st11 = Student('F', 28, 'St11', 'I', '09')
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)
print(gr, '\n')
try:
    gr.add_student(st11)
except TooManyStudents as ex:
    print(ex.message)
