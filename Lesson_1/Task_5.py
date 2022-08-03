money_plus = float(input("Введите значение Вашей выручки: "))
money_minus = float(input("Введите значение Ваших издержек: "))
result = money_plus - money_minus
if result > 0:
    print(f"Вы заработали {result} рублей, ура!")
    print(f"Рентабельность составляет {(result / money_minus) * 100:.2f}%")
    people = int(input("Сколько же сотрудников в Вашей компании? Введите цифру:"))
    print(f"Если поделить прибыль между сотрудниками, каждый получит по {result / people:.2f} рублей!")

elif result < 0:
    print(f"К сожалению, пока Ваша компания сработала с убытком {-result} рублей :(")





