def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = "Dmitriy", 29, False
values_dict = {'a': True, 'b': "Viktor", 'c': 100}
print_params(*values_list)
print_params(**values_dict)

value_list_2 = [1, 5], "Python"
print_params(*value_list_2, 42)