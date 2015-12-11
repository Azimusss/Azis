import os
import json
from utilities import search, location, clear, save


DIR = 'data'


def save(data, file_name):
    file = open(os.path.join(DIR, file_name), 'w', encoding="UTF-8")
    file.write(json.dumps(data, ensure_ascii=False))
    file.close()


def menu_do(menu, **kwargs):
    while True:
        clear()
        print("*" * 24)
        print("* Welcome to Shashki game")
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


def end():
    global run
    print("Goodbye")
    run = False
    return True


menu = [
    {
        "text": "Play",
        "sub_menu": [
            {
                "text": "Player vs Player",
            },
            {
                "text": "  Player vs PC  ",
            }
        ]
    },
    {
        "text": "Settings",
        "sub_menu": [
            {
                "text": "Colors",
            },
            {
                "text": "Sounds",
            },
            {
                "text": "Back to menu",
                "do": lambda: True
            }
        ]
    },
    {
        "text": "Exit",
        "do": end
    }
]

run = True

while run:
    menu_do(menu)