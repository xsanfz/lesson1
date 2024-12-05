#Самостоятельная работа по уроку "Распаковка позиционных параметров"

def print_params(a = 1, b = 'строка', c = True):
    print(a , b , c)

print_params()
print_params(10)
print_params('привет', False)
print_params(b=13)
print_params(c=[1, 2, 3])

values_list = [98, 'пока', False]
values_dict = {'a': 132, 'b': 'параметр', 'c': None}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [12.324, 'Строка']
print_params(*values_list_2, 788)


def append_to_list(item, list_my=None):
    if list_my is None:
        list_my = []
    list_my.append(item)
    return list_my
result = append_to_list(1)
print(result)
another_result = append_to_list(2)
print(another_result)
