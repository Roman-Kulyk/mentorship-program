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
    
    if "Trainee" in position:
        hr_specialists["trainee"].append(employee)
    elif "Junior" in position:
        hr_specialists["junior"].append(employee)
    elif "Senior" in position:
        hr_specialists["senior"].append(employee)
    else:
        hr_specialists["middle"].append(employee)
print("HR Spesialists = ",hr_specialists)
