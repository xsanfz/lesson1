#Практическое задание по теме: "Словари и множества"
from os import remove

my_dict = {"Sergey" : 1980, "Dmitriy" : 2010, "Alex" : 1994, "Elena" :1979}
print('Dict: ',my_dict)
print('Existing value: ',my_dict.get("Alex"))
print('Not existing value:', my_dict.get("Roman"))
my_dict.update({"Anastasia" : 2004, "Piter" : 2001})
removed_ = my_dict.pop("Piter")
print('Deleted value: ',removed_)
print('Modified dictionary: ',my_dict)

print()

my_set = {2, 4, 2, 7,"Енот", 1.34 , 3.14, "Енот"}
print(my_set)
my_set.add("Кот")
my_set.add(True)
my_set.remove(3.14)
print(my_set)



