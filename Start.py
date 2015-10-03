import os
import json

def save(data, file_name):
    file = open(os.path.join(DIR, file_name), 'w', encoding="UTF-8")
    file.write(json.dumps(data, ensure_ascii=False))
    file.close()

__author__ = 'azis'

# h = input("Введите желаемое данных видение: У, Пр, У кл 'number', Сп шк")

teach = open('Students.json')
stud = open('Teachers.json')

Students = json.load(teach)
Teachers = json.load(stud)

z = {}
surnames = []
lstt = []

print("*"*20,1,"*"*20)

for Stud in Students:
    print(Stud['name'])

print("*"*20,2,"*"*20)

for Teach in Teachers:
    print(Teach['name'])

print("*"*20,3,"*"*20)

for Stud in Students:
    clas = "5 А"
    i = 0
    i = i + 1
    print(Students[i]['name'], Students[i]['surname'])
    if i > len(Stud):
        break

print("*"*20,4,"*"*20)

for Teach in Teachers:
    print(Teach['school'])

print("*"*20,5,"*"*20)

for Stud in Students:
    surnames.append(Stud["surname"])

namesakes = [surname for surname in surnames if surnames.count(surname) > 1]
print(namesakes)

print("*"*20,0,"*"*20)

print("*"*18 , "Блок 3" , "*"*17)

print("*"*20,0,"*"*20)

DIR = "data"

students_data = json.load(open(os.path.join(DIR, 'Students.json'), 'r'))  # os.path.join - Вставляет нужный \ (Для исскуственного поддержания кросс-платформенности)
teachers_data = json.load(open(os.path.join(DIR, 'Teachers.json'), 'r'))  # константа - переменная которая не должна изменятся

student = {
    "name": "Петр",
    "middle_name": "Алексеевич",
    "surname": "Первый",
    "school": "67 школа",
    "class": "7 В",
    "birth_day": "06.06.1997"
}

students_data.append(student)

save(students_data, 'Students.json')
