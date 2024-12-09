#Самостоятельная работа по уроку "Рекурсия"

def get_multiplied_digits(number):

    str_number = str(number)

    if len(str_number) <= 1:
        return int(str_number)

    first = int(str_number[0])
    rest_of_digits = str_number[1:]
    if first == 0:
        return get_multiplied_digits(str_number[1:])

    last_digit = int(str_number[-1])

    if last_digit == 0:
        return get_multiplied_digits(str_number[:-1])

    return first * get_multiplied_digits(rest_of_digits)

result = get_multiplied_digits(40203)
print(result)

result2 = get_multiplied_digits(402030)
print(result2)
    