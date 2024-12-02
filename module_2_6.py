#Дополнительное практическое задание по модулю: "Основные операторы"


print("Введите число от 3 до 20: ")
n = int(input())

for first in range(1, n):
    for second in range(first + 1, n):
        if n % (first + second) == 0:
            print(first, second, sep="", end="")
