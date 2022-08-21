my_list = [5, 14, 73, 234, 636, 6, 3]
new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f"Исходный список {my_list}")
print(f"Новый список {new_list}")



