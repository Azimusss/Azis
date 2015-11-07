import json
import os

DIR = 'data'
def save(data, file_name):
    file = open(os.path.join(DIR, file_name), 'w', encoding="UTF-8")
    file.write(json.dumps(data, ensure_ascii=False))
    file.close()

stud = open(os.path.join('data', 'Students.json'))
teach = open(os.path.join('data', 'Teachers.json'))
stud_new = open(os.path.join('data', 'Students_new.json'))
teach_new = open(os.path.join('data', 'Teachers_new.json'))

students = json.load(stud)
teachers = json.load(teach)
students_new = json.load(stud_new)
teachers_new = json.load(teach_new)

lst = []
clas = '5 А'
for Teach in teachers_new:
    if clas in Teach["class"]:
        Teach["class"].remove(clas)
save(lst, "Teachers_new.json")
