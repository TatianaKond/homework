from random import randint

with open("Text_5.txt", "w", encoding="utf-8") as my_file:
    my_list = [randint(1, 40) for _ in range(100)]
    my_file.write(" ".join(map(str, my_list)))

    print(f"Сумма элементов = {sum(my_list)}")
