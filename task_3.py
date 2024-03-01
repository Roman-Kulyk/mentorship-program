"""You have a dict with students with their grades for various subjects:
1 - Create a function to add a new student to the dictionary. The function
should take the student's name and their grades for subject as input and
then add them to dictionary.
2 - Create a function to calculate a student's average grade. The function should take
student's name as input and return the average grade for all subjects.
3 - Create a function to remove a student from the dictionary. The function
should take the student's name as input and remove them from dictionary."""
students = {"Alice":[85, 90, 92],
            "Bob":[70, 80, 75],
            "Charlie":[60, 65, 70]}

def func_to_add(name,*args):
    """This is a function to add student to dictionary."""
    students[name] = list(args)
    print(name, "was added to the students dictionary.")
    

def func_to_calculate(name):
    """This is a function to calculate student's average grade."""
    x = students[name]
    average = sum(x)/len(x)
    print(f"The average {name}'s grade for all subjects is {average}")


def func_to_remove(name):
    """This is a function to remove student from dictionary."""
    students.pop(name)
    print(name, "was removed from students dictionary.")


print(students) 
func_to_add("Piotr", 40,50,60)
func_to_add("Pawel",58,58,49)
func_to_remove("Bob")

print(students)
func_to_calculate("Alice")