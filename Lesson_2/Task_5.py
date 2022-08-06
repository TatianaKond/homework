my_numbers = [9, 8, 6, 5, 5, 4, 3, 1]

while True:
    new_number = input("Введите натуральное число:\n")
    if new_number.isdigit():
        my_numbers.append(float(new_number))
        my_numbers.sort(reverse=True)
        print(my_numbers)
    elif new_number == "a":
        break



