def my_sum ():
    sum_res = 0
    exit = False
    while exit == False:
        number = input("Введите числа либо, если хотите завершить, введите q : ").split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'q':
                exit = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f"Текущая сумма =  {sum_res}")
    print(f"Итоговая сумма = {sum_res}")


my_sum()