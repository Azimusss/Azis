import os
import json
from utilities import search, get_full_name, location, clear

school_data = {}
students_data = []
DIR = 'data'
cls = ''


def save(data, file_name):
    file = open(os.path.join(DIR, file_name), 'w', encoding="UTF-8")
    file.write(json.dumps(data, ensure_ascii=False))
    file.close()


def load_data():
    global school_data
    global students_data

    with open(location('data/school.json')) as f:
        school_data = json.load(f)

    with open(location('data/Students.json')) as f:
        students_data = json.load(f)


def menu_do(menu, **kwargs):
    while True:
        clear()
        print("*" * 24)
        print("* Welcome to %s %s *" % (school_data['number'], school_data['type']))
        print("*" * 24)
        print("MENU > ", kwargs.get("sub_menu", ''))
        for num, el in enumerate(menu):
            print("%s. %s" % (num, el["text"]))
        choice = int(input(": "))
        if menu[choice].get("do"):
            if menu[choice]["do"]():
                break
        else:
            menu_do(menu[choice]["sub_menu"], sub_menu=menu[choice]['text'])
            # return True


def about_students():
    for class_room in school_data["classes"]:
        print("Ученики '%s' класса: " % class_room)
        for num, student in enumerate(search(students_data, class_room=class_room), start=1):
            # FIXME: учесть(во всей программе), в файле могут быть ученики из других школ
            print("     ", str(num) + ')', get_full_name(student))  # TODO: Добавить нумерацию учеников для каждого класса
        print("-" * 24)
    input("Нажмите Enter для возврата в предыдущее меню")


def about_classes():
    print("Все классы нашей школы")
    print("||", " || ".join(school_data['classes']), "||")
    print()
    input("Нажмите Enter для возврата в предыдущее меню")


def edit():
    clear()
    print("*" * 24)
    print("* Welcome to %s %s *" % (school_data['number'], school_data['type']))
    print("*" * 24)
    print("Menu > Edit")
    input("Нажмите Enter для возврата в предыдущее меню")
    pass


def end():
    global run
    print("Goodbye")
    run = False
    return True


def del_class():
    global cls
    cls = input('Введите класс который желаете удалить:')

    for Stud in school_data:
        Stud['classes'].remove(cls)
    for Stud in students_data[:]:
        if Stud['class'] == cls:
            students_data.remove(Stud)
            print(Stud)
    save(school_data, 'data/Students.json')
    return True


def add_class():
    cls = input('Введите номер класса который желаете добавить:')
    for Stud in students_data:
        Stud['classes'].append(cls)
    save(students_data, 'data/Students.json')
    return True


def re_class_st():
    global run
    print("Goodbye")
    run = False
    return True


def re__st():
    global run
    print("Goodbye")
    run = False
    return True


def re__st():
    global run
    print("Goodbye")
    run = False
    return True

load_data()

menu = [
    {
        "text": "Информация",
        "sub_menu": [
            {
                "text": "О классах",
                "do": about_classes
            },
            {
                "text": "Об учениках",
                "do": about_students
            },
            {
                "text": "Назад",
                "do": lambda: True
            }
        ]
    },
    {
        "text": "Редактировать",
        "sub_menu": [
            {
                "text": "Редактировать классы",
                        "sub_menu": [
                            {
                                "text": "Удалить класс: с удалением всех учившихся в нём учеников",
                                "do": del_class
                            },
                            {
                                "text": "Добавить класс",
                                "do": add_class
                            },
                            {
                                "text": "Назад",
                                "do": lambda: True
                            },
                        ]
            },
            {
                "text": "Редактировать ученика",
                "do": [
            {
                "text": "Назад",
                "do": re_class
            },
            {
                "text": "Назад",
                "do": lambda: True
            }
                ]
            },
            {
                "text": "Редактировать учителя",
            },
            {
                "text": "Назад",
                "do": lambda: True
            }
        ]
    },
    {
        "text": "Выход",
        "do": end
    }
]

run = True

while run:
    menu_do(menu)
