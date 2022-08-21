from sys import argv

def salary():
    try:
        time, rate, bonus = map(float, argv[1:])
        print(f"Заработная плата сотрудника = {time * rate + bonus}")
    except ValueError:
        print("Нужно ввести 3 числа")

salary()
