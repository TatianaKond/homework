class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} is started'

    def stop(self):
        return f'{self.name} is stopped'

    def turn_right(self):
        return f'{self.name} is turned right'

    def turn_left(self):
        return f'{self.name} is turned left'

    def show_speed(self):
        return f'Current speed {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} is higher than allow for town car'
        else:
            return f'Speed of {self.name} is normal for town car'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is higher than allow for work car'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'

Mustang = SportCar(100, "Blue", "Mustang", False)
Toyota = TownCar(30, "White", "Toyota", False)
Niva = WorkCar(70, "Yellow", "Niva", False)
Lada = PoliceCar(110, "Green", "Lada", True)
print(Lada.turn_left())
print(f"If {Toyota.turn_right()}, so {Mustang.stop()}")
print(f"{Lada.go()} with speed exactly {Lada.show_speed()}")
print(f"{Niva.name} is {Niva.color}")
print(f"Is {Lada.name} a police car? {Lada.is_police}")
print(f"Is {Niva.name}  a police car? {Niva.is_police}")
print(Niva.show_speed())
print(Mustang.show_speed())
print(Lada.show_speed())



