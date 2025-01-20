employees = {
            "Emily Williams": "Trainee Devops",
            "Grace Carter": "Senior HR Specialist",
            "Ella Patel": "Senior Developer",
            "Amella Kim": "Senior QA Manual",
            "David Chang": "Senior QA Automation",
            "Mia Torres": "Devops",
            "Sophia Hernandez": "Junior Devops",
            "Matthew Rodriguez": "Junior Developer",
            "Joseph Liu": "Senior Manager",
            "Charlotte Adams": "QA Automation",
            "Olivia Garcia": "Trainee Manager",
            "John Doe": "Trainee QA Manual",
            "Ava Gonzalea": "Junior Manager",
            "Roman Kulyk": "QA Automation",
            "Isabella Flores": "HR Specialist",
            "James Lee": "Junior QA Manual",
            "Alexander Nguyen": "Manager",
            "William Lopez": "Junior HR Specialist",
            "Michael Johnson": "Trainee Developer",
            "Benjamin Perez": "QA Manual",
            "Alice Smith": "Trainee QA Automation",
            "Logan Mitchell": "Senior Devops",
            "Emma Martinez": "Junior QA Automation",
            "Daniel Brown": "Trainee HR Specialist",
            "Ethan Wilson": "Developer"
            }

hr_specialists = {"trainee": [],"junior": [],"middle": [],"senior": []}
devops = {"trainee": [],"junior": [],"middle": [],"senior": []}
developers = {"trainee": [],"junior": [],"middle": [],"senior": []}
qa_manual = {"trainee": [],"junior": [],"middle": [],"senior": []}
qa_automation = {"trainee": [],"junior": [],"middle": [],"senior": []}
managers = {"trainee": [],"junior": [],"middle": [],"senior": []}

for employee, position in employees.items():
    grade = ''
    if "Trainee" in position:
        grade = "trainee"
    elif "Junior" in position:
        grade = "junior"
    elif "Senior" in position:
        grade = "senior"
    else:
        grade = "middle"

    if 'HR' in position:
        hr_specialists[grade].append(employee)
    elif 'Devops' in position:
        devops[grade].append(employee)
    elif 'Developer' in position:
        developers[grade].append(employee)
    elif 'QA Manual' in position:
        qa_manual[grade].append(employee)
    elif 'QA Automation' in position:
        qa_automation[grade].append(employee)
    elif 'Manager' in position:
        managers[grade].append(employee)

print('HR = ', hr_specialists)
print('Devops = ', devops)
print('Developer = ', developers)
print('QA Manual = ', qa_manual)
print('QA Automation = ', qa_automation)
print('Manager = ', managers)
