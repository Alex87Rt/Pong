# набор классов для рассчета физики


class PlayerPhy:
    def __init__(self, init_pos, name):
        self.pos_x = init_pos["x"]
        self.pos_y = init_pos["y"]
        self.name = name

    def get_pos(self):
        return {"name": self.name, "x": self.pos_x, "y": self.pos_y}

# класс длля расчета физики
class GamePhy:
    def __init__(self):
        self.l_player = PlayerPhy({"x": 50.0, "y": 200.0}, "left_player")
        self.r_player = PlayerPhy({"x": 950.0, "y": 200.0}, "right_player")
        self.ball = {"name": "ball", "x": 500.0, "y": 200.0}

        #по умолчанию координаты пересчитываются 64 раза в секунду
    def tick(self, time=1.0/64):
        pass
