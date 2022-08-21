def sal():
    try:
        time = float(input("Выработка сотрудника в часах = "))
        salary = int(input("Ставка сотрудника = "))
        bonus = int(input("Премия сотрудника = "))
        res = time * salary + bonus
        print(f"Заработная плата сотрудника = {res}")
    except ValueError:
        return print("Нужно ввести число!")
sal()
