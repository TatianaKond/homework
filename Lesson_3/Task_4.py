def my_pow_fun(x, y):
    try:
        res = x**y
    except TypeError:
        return "Введите действительное положительное число и целое отрицательное число"
    return res

print(my_pow_fun(1.4, -7))


