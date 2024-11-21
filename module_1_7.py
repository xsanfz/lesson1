#Дополнительное практическое задание по модулю: "Базовые структуры данных."

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

sorted_students = sorted(students) # Преобразуем множество в список по алфавитному порядку
result = {} # Создаем пустой словарь для хранения результатов
avg_grades = [
    sum(grades[0]) / len(grades[0]),
    sum(grades[1]) / len(grades[1]),
    sum(grades[2]) / len(grades[2]),
    sum(grades[3]) / len(grades[3]),
    sum(grades[4]) / len(grades[4])]

sorted_name = [sorted_students]

result[sorted_name] = avg_grades


print(result) # Выводим результат