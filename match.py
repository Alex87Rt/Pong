from threading import Thread #вычисления в матче должны проходить в отдельном потоке
from game_phy import GamePhy


# класс матча
# отвечает за игровую логику
class Match(Thread):
    def __init__(self, ui_update_callback=None):
        Thread.__init__(self)
        self.ui_update_callback = ui_update_callback

        self.phy = GamePhy()
        # начальные координаты
        # TODO: инициализировать начальные координаты объектов

# этот метод будет работать в отдельном потоке после вызова match.start()
    def run(self):
        # производим расчеты новых координат
        self.phy.tick()

        # обновляем позиции объектов на фронт энде
        self._update(self.phy.l_player.get_pos())
        self._update(self.phy.r_player.get_pos())
        self._update(self.phy.ball)

        # проверяем столкновения
        # TODO

    def key_event(self, key):
        # TODO сделать обработку нажатия клавиш
        pass

    # Эту функцию надо вызывать чтобы обновить объект на интерфейсе
    def _update(self, ui_object):
        if self.ui_update_callback and ui_object:
            self.ui_update_callback(ui_object)
