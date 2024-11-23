# Запись данных о студентах в файл
students = [
    {'name': 'John', 'age': 23},
    {'name': 'Jane', 'age': 22},
    {'name': 'Mike', 'age': 24},
]

with open('students.txt', 'w') as file:
    for student in students:
        file.write(f"Name: {student['name']}, Age: {student['age']}\n")
