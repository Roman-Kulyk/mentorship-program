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
    """This is a function that prints list of all teachers in the school."""
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

# print_students_list()
# print_teachers_list()
print_teachers_subjects_list()