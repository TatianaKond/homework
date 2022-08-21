with open("text_2.txt", encoding="utf-8") as f:
    my_line = f.readlines()
    for index, value in enumerate(my_line, 1):
        words_number = len(value.split())
        print(f"В строке {index} содержится {words_number} слов")

