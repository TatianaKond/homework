original_number = int(input("Введите целое число больше нуля: "))
max_integer = 0
num = original_number

while num > 0:
    integer = num % 10
    if integer > max_integer:
        max_integer = integer
    num = num // 10

print(f"Самая большая цифра в числе {original_number} это {max_integer}")


