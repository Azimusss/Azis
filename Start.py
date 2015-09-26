import json

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



# dsijbccbcdkjkkcbkjc

