import json
import os

teach = open(os.path.join('data', 'Students.json'))
stud = open(os.path.join('data', 'Teachers.json'))
stud_new = open(os.path.join('data', 'Students_new.json'))
teach_new = open(os.path.join('data', 'Teachers_new.json'))

students = json.load(teach)
teachers = json.load(stud)
students_new = json.load(stud_new)
teachers_new = json.load(teach_new)

lst = []
studi_name = 'Александр'
studi_suname = 'Красный'
clss = '666 Б'

# for Teach_new in teachers_new:
#     lst.append(Teach_new['class'])  # помогает в сортировке переменных
#     ln = len(lst)
#     print(lst[ln - 1])

print("*"*20, 3, "*"*20)

for Stud_new in students_new[:]:
    if Stud_new['name'] == studi_name and Stud_new['suname'] == studi_suname:
        students_new.remove(Stud_new)

print("*"*20, 4, "*"*20)