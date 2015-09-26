__author__ = 'azis'
import json

teach = open('Students.json')
Students = json.load(teach)

lst = []

for Stud in Students:
    clas = "5 А"
    lst.append(Stud['class'])
    if 'class' == clas:
        break
    St = Stud
    print(St)

print(lst)
