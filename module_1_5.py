#Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи"

immutable_var = (1, 2, 'time', 16.0, [1, 2, 3, 4, 5, 6], True)
print(immutable_var)

#immutable_var[1] = 7
#TypeError: 'tuple' object does not support item assignment
#Главное свойство кортежа - это невозможность изменить содержимое кортежа после его создания


mutable_list = [1, 2, 3, 'one', 4.0, [1, 2, 3, 4, 5], False]
mutable_list[0] = 'track'
mutable_list[3] = 13
mutable_list[5] = 2.0
mutable_list[6] = True
print(mutable_list)