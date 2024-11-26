# Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Пустые списки для простых и не простых чисел
primes = []
not_primes = []

for num in numbers:
    if num == 1:
        continue
    is_prime = True
    for remainder in range(2, num):
        if num % remainder == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)
print("Primes:", primes)
print("Not Primes:", not_primes)
