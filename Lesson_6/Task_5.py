class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"Запуск отрисовки {self.title}"


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"Вы взяли {self.title}. Запуск отрисовки ручкой"


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"Вы взяли {self.title}. Запуск отрисовки карандашом"


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"Вы взяли {self.title}. Запуск отрисовки маркером"


pen = Pen("Классную ручку")
pencil = Pencil("Волшебный карандаш")
handle = Handle("Нестираемый маркер")
print(pen.draw())
print(pencil.draw())
print(handle.draw())