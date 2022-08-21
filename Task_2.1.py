from random import randint

my_list = [randint(0, 100) for _ in range (0, randint(2, 20))]
second_list = [num for i, num in enumerate(my_list[1:]) if num > my_list[i]]

print(my_list)
print(second_list)
