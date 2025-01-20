"""
Given the names and grades for each student in a class of N students, store them
in a nested list and print the name(s) of any student(s) having the second lowest
grade.
Note: If there are multiple students with the second lowest grade, order their
names alphabetically and print each name on a new line.
"""

if __name__ == '__main__':

    python_students = []

    n = (int(input()))
    if 2 <= n <= 5:
        for _ in range(n):
            name = input()
            scope = float(input())
            python_students.append([name, scope])

        second = max(python_students, key=lambda x: x[1])[1]
        first = min(python_students, key=lambda x: x[1])[1]

        for i in range(len(python_students)):
            if python_students[i][1] <= second and python_students[i][1] != first:
                second = python_students[i][1]

        list_second_results = []
        for i in range(len(python_students)):
            if second == python_students[i][1]:
                
                list_second_results.append(python_students[i][0])
        sorted_name_list = (sorted(list_second_results))
        for i in sorted_name_list:
            print(i)
            
