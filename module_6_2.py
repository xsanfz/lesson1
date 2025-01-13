#Задача "Изменять нельзя получать"


class Vehicle:

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, model, engine_power, color, owner=None):
        self.__owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def get_owner(self):
        return self.__owner

    def set_owner(self, value):
        self.__owner = value

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.get_owner()}")

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, model, color, engine_power):
        super().__init__(model, engine_power, color, owner)


# Пример использования
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Исходные свойства
vehicle1.print_info()

# Меняем свойства
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.set_owner('Vasyok')

# Проверяем изменения
vehicle1.print_info()
