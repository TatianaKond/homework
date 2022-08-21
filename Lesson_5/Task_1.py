print("Введите данные для записи\n Пустая строка закончит ввод текста")
with open("task_1.txt", "w", encoding="utf-8") as my_file:
    while (line := input()) != "":
        my_file.write(f"{line}\n")

