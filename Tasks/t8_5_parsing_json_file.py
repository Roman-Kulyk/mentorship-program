import json


def print_students_list():
    """This is a function that prints list of all students in the class."""
    f = open('class.json')
    data = json.load(f)
    names = []
    for i in data['students']:
        if i['name'] not in names:
            names.append(i['name'])
    print(names)
    print()
    f.close()


def print_teachers_list():
    """This is a function that prints list of all teachers in the school."""
    f = open('class.json')
    data = json.load(f)
    names = []
    for i in data['teachers']:
        if i['name'] not in names:
            names.append(i['name'])
    print(names)
    print()
    f.close()


def print_teachers_subjects_list():
    """This is a function that prints list of all students for certain
    teacher in the school.
    """
    f = open('class.json')
    data = json.load(f)
    students = data['students']
    teachers = data['teachers']

    for teacher in teachers:
        teacher_name = teacher['name']
        teacher_subject = teacher['subject']
        teacher_students = []

        for student in students:
            student_name = student['name']
            student_subjects = student['subjects']

            if teacher_subject in student_subjects:
                teacher_students.append(student_name)

        print(f"{teacher_name} => {teacher_students}")

    f.close()


def print_students_subject_list():
    """This is a function that prints list of all teachers for certain
    student.
    """
    f = open('class.json')
    data = json.load(f)
    teachers = data['teachers']
    students = data['students']

    for student in students:
        student_name = student['name']
        student_subject = student['subjects']
        student_teachers = []

        for teacher in teachers:
            teacher_name = teacher['name']
            teacher_subject = teacher['subject']

            if teacher_subject in student_subject:
                student_teachers.append(teacher_name)

        print(f"{student_name} => {student_teachers}")


def print_school_teachers_list():
    """This is a function that prints list of all teachers for certain
    school.
    """
    f = open('class.json')
    data = json.load(f)
    teachers = data['teachers']
    schools = data['schools']

    for school in schools:
        school_name = school['name']
        school_postal_code = school['postal_code']
        teacher_school = []

        for teacher in teachers:
            teacher_name = teacher['name']
            teacher_postal_code = teacher['postal_code']

            if teacher_postal_code == school_postal_code:
                teacher_school.append(teacher_name)
        print(f'{school_name} => {teacher_school}')


def print_school_students_list():
    """This is a function that prints list of all students for certain
    school.
    """
    f = open('class.json')
    data = json.load(f)
    students = data['students']
    schools = data['schools']

    for school in schools:
        school_name = school['name']
        school_postal_code = school['postal_code']
        student_school = []

        for student in students:
            student_name = student['name']
            student_postal_code = student['school']

            if student_postal_code == school_postal_code:
                student_school.append(student_name)
        print(f'{school_name} => {student_school}')


print_students_list()
print_teachers_list()
print()
print_teachers_subjects_list()
print()


print_students_subject_list()
print()
print_school_teachers_list()
print()
print_school_students_list()
