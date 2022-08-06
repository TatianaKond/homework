my_list = [54, -77.2, 'False', [1, 10], (3, 5), True, None, {1: 'Hello', 2: 'World'}, frozenset()]
def my_type(el):
    for el in range(len(my_list)):
        print(type(my_list[el]))
    return
my_type(my_list)
