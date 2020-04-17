import pyQt5

#menu states:
MENU_STATE_START = 0
MENU_STATE_GAME = 1
#.. etc


# Класс основного меню
class Menu:
    def __init__(self):
        self.state = MENU_STATE_START

    def update(self, upt_object):
        pass

    def play(self):
        pass

