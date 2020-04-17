# !/usr/bin/python3
from ui_menu import Menu


# Функция начинает игру двух играков на 1 компьютере
def start_standalone():
    menu = Menu()
    menu.play()


# TODO: добавить парсинг аргументов
if __name__ == "__main__":
    start_standalone()

