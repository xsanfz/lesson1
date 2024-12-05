#Самостоятельная работа по уроку "Распаковка позиционных параметров"

def print_params(a = 1, b = 'строка', c = True):
    print(a , b , c)

print_params()
print_params(10)
print_params('привет', False)
print_params(b=13)
print_params(c=[1, 2, 3])

values_list = [98, 'пока', False]
values_dict = {'a': 132, 'b': 'параметр', 'c': True}
print_params(*values_list)
print_params(**values_dict)
