def div(s_1, s_2):
    try:
        s_1, s_2 = int(s_1), int(s_2)
        div_num = s_1 / s_2
    except ValueError:
        return 'Value Error!'
    except ZeroDivisionError:
        return "Делить на ноль нельзя, введите другое число"
    return round(div_num, 2)

print(div(input ("Введите первое число: "), input("Введите второе число:")))

