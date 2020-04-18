"""
В этом фалйше описываетсявизуальный интерфейс примерно как тут
https://habr.com/ru/post/326268/
более подробно тут
https://build-system.fman.io/pyqt5-tutorial
обработка нажатия клавиш
https://stackoverflow.com/questions/38507011/implementing-keypressevent-in-qwidget
"""
# Класс QUrl предоставляет удобный интерфейс для работы с Urls
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget
# Класс QQuickView предоставляет возможность отображать QML файлы.
from PyQt5.QtQuick import QQuickView
from PyQt5 import QtCore

from match import Match

#menu states:
MENU_STATE_START = 0
MENU_STATE_GAME = 1
#.. etc


# Класс основного меню
class Menu:
    def __init__(self):
        # TODO создать окно как здесть https://habr.com/ru/post/326268/

        self.state = MENU_STATE_START

        # создаем новую игру и передаем функцию обновления интерфейса как параметр
        self.game = Match(ui_update_callback=self.update)

# Обработка нажатий клавишь
    def key_press_event(self, event):
        if event.key() == QtCore.Qt.Key_W:
            self.geme.key_event("W")
        elif event.key() == QtCore.Qt.Key_S:
            self.geme.key_event("S")
        # TODO Сделать обработку остальных клавишь
        event.accept()

# Эта фугнкция обновляет положения объекты в интерфейсе
# upd_object - представляет собой словарь в котором сожержатся параметры объекта
    def update(self, upd_object):
        try:
            obj_name = upd_object["name"]
            # TODO Сделать обновлние положения объект в зависимости от его имени
        except KeyError as e:
            # TODO добавить логирование ошибок
            pass

# "Этот метод начинает игру
    def play(self):
        self.game.start() # запускае игру в отдельном потоке
        self.game.join() # ждем пока поток игры не закончится



