from functools import reduce

def my_list(el_1, el_2):
    return el_1 * el_2

new_list = [el for el in range(100, 1001, 2)]
print(f"List\n{new_list}\nРезультат умножения чисел\n{reduce(my_list, new_list)}")
