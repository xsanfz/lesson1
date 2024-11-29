#Дополнительное практическое задание по модулю: "Основные операторы"

result = []
n = int(input('Введите число: '))
numbers = range(0, 21)

# Создаем пустой список для хранения сумм пар
sums_of_pairs = []

# Внешний цикл проходит по каждому элементу списка
for i in range(len(numbers)):
    # Внутренний цикл начинается со следующего элемента после текущего
    for j in range(i + 1, len(numbers)):
        # Сложение текущей пары и добавление результата в список
        sums_of_pairs.append(numbers[i] + numbers[j])


# Цикл для проверки деления без остатка
for n in range(numbers):
    if n % numbers == 0:
        result.append(i)
print(result)
