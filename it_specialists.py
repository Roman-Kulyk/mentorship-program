employees = {
            "Emily Williams":"Trainee Devops",
            "Grace Carter":"Senior HR Specialist",
            "Ella Patel":"Senior Developer",
            "Amella Kim":"Senior QA Manual",
            "David Chang":"Senior QA Automation",
            "Mia Torres":"Devops",
            "Sophia Hernandez":"Junior Devops",
            "Matthew Rodriguez":"Junior Developer",
            "Joseph Liu":"Senior Manager",
            "Charlotte Adams":"QA Automation",
            "Olivia Garcia":"Trainee Manager",
            "John Doe":"Trainee QA Manual",
            "Ava Gonzalea":"Junior Manager",
            "Isabella Flores":"HR Specialist",
            "James Lee":"Junior QA Manual",
            "Alexander Nguyen":"Manager",
            "William Lopez":"Junior HR Specialist",
            "Michael Johnson":"Trainee Developer",
            "Benjamin Perez":"QA Manual",
            "Alice Smith":"Trainee QA Automation",
            "Logan Mitchell":"Senior Devops",
            "Emma Martinez":"Junior QA Automation",
            "Daniel Brown":"Trainee HR Specialist",
            "Ethan Wilson":"Developer"
            }


hr_specialists = {"trainee":[],"junior":[],"middle":[],"senior":[]}
for employee, position in employees.items():
    if "HR" in position:
        if "Trainee" in position:
            hr_specialists["trainee"].append(employee)
        elif "Junior" in position:
            hr_specialists["junior"].append(employee)
        elif "Senior" in position:
            hr_specialists["senior"].append(employee)
        else:
            hr_specialists["middle"].append(employee)
print("HR Spesialists = ", hr_specialists)

devops = {"trainee":[],"junior":[],"middle":[],"senior":[]}
for employee, position in employees.items():
    if "Devops" in position:
        if "Trainee" in position:
            devops["trainee"].append(employee)
        elif "Junior" in position:
            devops["junior"].append(employee)
        elif "Senior" in position:
            devops["senior"].append(employee)
        else:
            devops["middle"].append(employee)
print("Devops =", devops)

developers = {"trainee":[],"junior":[],"middle":[],"senior":[]}
for employee, position in employees.items():
    if "Developer" in position:
        if "Trainee" in position:
            developers["trainee"].append(employee)
        elif "Junior" in position:
            developers["junior"].append(employee)
        elif "Senior" in position:
            developers["senior"].append(employee)
        else:
            developers["middle"].append(employee)
print("Developer =", developers)

qa_manual = {"trainee":[],"junior":[],"middle":[],"senior":[]}
for employee, position in employees.items():
    if "QA Manual" in position:
        if "Trainee" in position:
            qa_manual["trainee"].append(employee)
        elif "Junior" in position:
            qa_manual["junior"].append(employee)
        elif "Senior" in position:
            qa_manual["senior"].append(employee)
        else:
            qa_manual["middle"].append(employee)
print("QA Manual =", qa_manual)

qa_automation = {"trainee":[],"junior":[],"middle":[],"senior":[]}
for employee, position in employees.items():
    if "QA Automation" in position:
        if "Trainee" in position:
            qa_automation["trainee"].append(employee)
        elif "Junior" in position:
            qa_automation["junior"].append(employee)
        elif "Senior" in position:
            qa_automation["senior"].append(employee)
        else:
            qa_automation["middle"].append(employee)
print("QA Automation = ", qa_automation)

managers = {"trainee":[],"junior":[],"middle":[],"senior":[]}
for employee, position in employees.items():
    if "Manager" in position:
        if "Trainee" in position:
            managers["trainee"].append(employee)
        elif "Junior" in position:
            managers["junior"].append(employee)
        elif "Senior" in position:
            managers["senior"].append(employee)
        else:
            managers["middle"].append(employee)
print("Manager =", managers)
