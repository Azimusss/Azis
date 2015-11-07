import os
import json

def save(data, file_name):
    file = open(os.path.join(DIR, file_name), 'w', encoding="UTF-8")
    file.write(json.dumps(data, ensure_ascii=False))
    file.close()

# h = input("Введите желаемое данных видение: У, Пр, У кл 'number', Сп шк")

stud = open(os.path.join('data', 'Students.json'))
teach = open(os.path.join('data', 'Teachers.json'))
stud_new = open(os.path.join('data', 'Students_new.json'))
teach_new = open(os.path.join('data', 'Teachers_new.json'))

students = json.load(stud)
teachers = json.load(teach)
students_new = json.load(stud_new)
teachers_new = json.load(teach_new)

ls = []
z = {}
surnames = []
lstt = []

print("*"*20, 1, "*"*20)##########################################################################

for Stud_new in students_new:
    print(Stud_new['name'])

print("*"*20, 2, "*"*20)##########################################################################

for Teach in teachers_new:
    print(Teach['name'])

print("*"*20, 3, "*"*20)##########################################################################

for Stud_new in students:
    clss = "5 А"
    i = 0
    i = i + 1
    print(students[i]['name'], students[i]['surname'])
    if i > len(Stud_new):
        break

print("*"*20, 4, "*"*20)##########################################################################

for Teach in teachers:
    print(Teach['school'])

print("*"*20, 5, "*"*20)##########################################################################

for Stud_new in students:
    surnames.append(Stud_new["surname"])

namesakes = [surname for surname in surnames if surnames.count(surname) > 1]
print(namesakes)

print("*"*20, 0, "*"*20)##########################################################################

print("*"*18, "Блок 3", "*"*17)

print("*"*20, 1, "*"*20)##########################################################################
print("*"*18, "Готов", "*"*18)

DIR = "data"

students_data = json.load(open(os.path.join(DIR, 'Students.json'), 'r'))  # os.path.join - Вставляет нужный \ (Для исскуственного поддержания кросс-платформенности)
teachers_data = json.load(open(os.path.join(DIR, 'Teachers.json'), 'r'))  # константа - переменная которая не должна изменятся

student = {
    "name": "Петр",
    "middle_name": "Алексеевич",
    "surname": "Первый",
    "school": "67 школа",
    "class": "7 Д",
    "birth_day": "06.06.1997"
}

students_data.append(student)

save(students_data, 'Students_new.json')

print("*"*20, 2, "*"*20)##########################################################################
print("*"*18, "Готов", "*"*18)

teacher = {
    "name": "Юрий",
    "middle_name": "Алексеевич",
    "surname": "Васин",
    "school": "67 школа",
    "class": [
      "5 Д",
      "6 Б",
      "7 В"
    ]
}

teachers_data.append(teacher)

save(teachers_data, 'Teachers_new.json')

print("*"*20, 3, "*"*20)##########################################################################
print("*"*18, "Готов", "*"*18)

teach = 'Александр'
clss1 = "666 Б"

for Teach_new in teachers_new:
    if Teach_new['name'] == teach:
        Teach_new['class'].append(clss1)
        break


print("*"*20, 4, "*"*20)##########################################################################
print("*"*18, "Готов", "*"*18)

studi_name = 'Александр'
studi_suname = 'Красный'

for Stud_new in students_new[:]:
    if Stud_new['name'] == studi_name and Stud_new['surname'] == studi_suname:
        students_new.remove(Stud_new)

print("*"*20, 5, "*"*20)##########################################################################
print("*"*18, "Готов", "*"*18)

clss2 = '7 Б'

for Stud_new in students_new[:]:
    if Stud_new['class'] == clss2:
        students_new.remove(Stud_new)

print("*"*20, 6, "*"*20)##########################################################################
print("*"*18, "Готов", "*"*18)

teach_name = 'Владимир'
teach_surname = 'Вышкин'
teach_middle_name = 'Сергеевич'

for Teach_new in teachers_new:
    if Teach_new['name'] == teach and Teach_new['surname'] == teach_surname and Teach_new['middle_name'] == teach_middle_name:
        students_new.remove(Stud_new)

print("*"*20, 7, "*"*20)##########################################################################

school = "67 школа"

for Teach_new in teachers_new[:]:
    if Teach_new['class'] == school:
        teachers_new.remove(Teach_new)

print("*"*20, 8, "*"*20)##########################################################################
print("*"*18, "Готов", "*"*18)

clss3 = '6 А'

for Teach_new in teachers_new:
    if Teach_new['name'] == teach_name and Teach_new['surname'] == teach and Teach_new['middle_name'] == teach:
        Teach_new.remowe(clss3)

print("*"*18, "4 блок", "*"*18)##########################################################################
print("*"*20, 1, "*"*20)

ii = 0
for Stud_new in students_new:
    ii = ii + 1
    Stud_new['id'] = ii
    save(students_new, "Students_new.json")

iii = 0
for Teach_new in teachers_new:
    iii = iii + 1
    Teach_new['id'] = iii
    save(teachers_new, "Students_new.json")

print("*"*20, 2, "*"*20)

su = "Черный"
for Stud_new in students_new:
    if Stud_new["surname"] == su:
        print(Stud_new['surname'], Stud_new['name'],  Stud_new['middle_name'])




















