class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Autobus(Transport):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)  # Вызов конструктора родительского класса

    def display_info(self):
        print(f"Название автомобиля: {self.name} Скорость: {self.max_speed} Пробег: {self.mileage}")

# Создаем объект Autobus
autobus = Autobus("Renault Logan", 180, 12)

# Выводим информацию об объекте
autobus.display_info()
