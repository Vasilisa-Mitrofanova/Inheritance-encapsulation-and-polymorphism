class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def grade_to_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and grade <= 10 and (course in self.courses_in_progress or course in self.finished_courses):
            if course in lecturer.grades.keys():
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            print('Ошибка. Проверьте введенные данные.')

    def __str__(self):
        print(f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {average_score_calculation(self)}")
        print("Курсы в процессе изучения: ", end="")
        for course in self.courses_in_progress:
            print(f"{course},", end=" ")
        print("\nЗавершенные курсы: ", end="")
        for course in self.finished_courses:
            print(f"{course},", end=" ")
        res = "\n"
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Ошибка. Попытка сравнить студента с не-студентом.")
            return
        else:
            return average_score_calculation(self) < average_score_calculation(other)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        mean = 0
        count = 0
        for grade_s in self.grades.values():
            for grade in grade_s:
                mean += grade
            count += len(grade_s)
        mean //= count
        print(f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {mean}")
        return ""

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Ошибка. Попытка сравнить лектора с не-лектором.")
            return
        else:
            return average_score_calculation(self) < average_score_calculation(other)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        print(f"Имя: {self.name} \nФамилия: {self.surname}")
        return ""


def average_score_calculation(student):
    mean = 0
    count = 0
    for grade_s in student.grades.values():
        for grade in grade_s:
            mean += grade
        count += len(grade_s)
    mean //= count
    return mean


def mean_grade_for_students(students, name_of_course):
    amount = 0
    count = 0
    for student in students:
        if name_of_course in student.grades.keys():
            for grade in student.grades[name_of_course]:
                amount += grade
                count += 1
    res = amount/grade
    print(f'Cредняя оценка за домашние задания всех студентов в рамках курса "{name_of_course}": {res}')


def mean_grade_for_lecturer(lecturers, name_of_course):
    amount = 0
    count = 0
    for lecturer in lecturers:
        if name_of_course in lecturer.grades.keys():
            for grade in lecturer.grades[name_of_course]:
                amount += grade
                count += 1
    res = amount / grade
    print(f'Cредняя оценка за лекции всех лекторов в рамках курса "{name_of_course}": {res}')


# создаю экземпляры класса Student

student1 = Student("Николай", "Николаев", "random_gender")
student2 = Student("Макар", "Макаров", "random_gender")
student3 = Student("Алексей", "Алексеев", "random_gender")

student1.finished_courses += ["Python", "Git"]
student2.finished_courses += ["Git"]
student3.finished_courses += ["Python"]

student2.courses_in_progress += ["Python"]
student3.courses_in_progress += ["Git"]

student1.grades["Python"] = [3, 2, 4, 5, 2, 1, 3]
student1.grades["Git"] = [1, 3, 5, 8, 10, 3, 2]
student2.grades["Git"] = [10, 10, 9, 10, 9, 10, 9]
student3.grades["Python"] = [10, 10, 10, 10, 10, 10, 10]

students = [student1, student2, student3]

# создаю экземпляры класса Lecturer

lecturer1 = Lecturer("Иван", "Иванович")
lecturer2 = Lecturer("Петр", "Петрович")
lecturer3 = Lecturer("Артем", "Артемович")

lecturer1.courses_attached = ["Python", "Git"]
lecturer2.courses_attached = ["Python", "Git"]
lecturer3.courses_attached = ["Python", "Git"]

lecturers = [lecturer1, lecturer2, lecturer3]

# Reviewer

reviewer1 = Reviewer("Максим", "Максимович")
reviewer2 = Reviewer("Андрей", "Андреевич")
reviewer3 = Reviewer("Дмитрий", "Дмитриевич")

# проверка, как работает метод выставления оценок лекторам

student1.grade_to_lecturer(lecturer1, "Python", 10)
student1.grade_to_lecturer(lecturer1, "Git", 10)
student1.grade_to_lecturer(lecturer2, "Python", 5)
student1.grade_to_lecturer(lecturer2, "Git", 5)
student1.grade_to_lecturer(lecturer3, "Python", 10)
student1.grade_to_lecturer(lecturer3, "Git", 10)

student2.grade_to_lecturer(lecturer1, "Git", 5)
student2.grade_to_lecturer(lecturer2, "Git", 3)
student2.grade_to_lecturer(lecturer3, "Git", 10)

student3.grade_to_lecturer(lecturer1, "Python", 7)
student3.grade_to_lecturer(lecturer2, "Python", 1)
student3.grade_to_lecturer(lecturer3, "Python", 10)

print(lecturer1.grades)
print(lecturer2.grades)
print(lecturer3.grades)

# проверка, как работают измененные методы __str__

print(student1)
print(student2)
print(student3)

print(lecturer1)
print(lecturer2)
print(lecturer3)

print(reviewer1)
print(reviewer2)
print(reviewer3)

# проверка, как работает функция выводы средней оценки студентов

mean_grade_for_students(students, "Git")
mean_grade_for_students(students, "Python")

# проверка, как работает функция выводы средней оценки лекторов

mean_grade_for_lecturer(lecturers, "Git")
mean_grade_for_lecturer(lecturers, "Python")

# проверка, как работает метод сравнения студентов и метод сравнения лекторов

print()

print(student1 < student2)
print(student3 > student1)

print(lecturer1 < lecturer2)
print(lecturer3 > lecturer1)