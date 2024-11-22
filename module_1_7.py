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
    sum(grades[4]) / len(grades[4])] #вычисляем среднее значение
students_name = tuple(sorted_students) #преобразуем список в кортеж

result[students_name[0]] = avg_grades[0]
result[students_name[1]] = avg_grades[1]
result[students_name[2]] = avg_grades[2]
result[students_name[3]] = avg_grades[3]
result[students_name[4]] = avg_grades[4] #добавляем значения  и ключи в словарь
print(result) # Выводим результат