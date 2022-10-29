# 1. Створіть клас Vehicle з атрибутами екземпляра max_speed і mileage та методами increase_speed, break_speed,
# mileage_info
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def increase_speed(self, num):
        print(f"Speed increased to {num}")

    def break_speed(self, num):
        print(f"Speed decreased to {num}")

    def mileage_info(self):
        print("Mileage:", self.mileage)


# 2. Створіть дочірній клас Bus, який успадкує всі змінні та методи класу Vehicle і матиме власний метод
# seating_capacity
class Bus(Vehicle):
    def __init__(self, max_speed, mileage):
        super().__init__(max_speed, mileage)

    def seating_capacity(self, num):
        print(f"Seating capacity: {num}")


# 3. Визначте, від якого класу успадковується клас Bus (перевірте issubclass)
print(issubclass(Bus, Vehicle))

# 4. Створіть екземпляр Bus під назвою school_bus і визначте, чи є school_bus об'єктом класу Vehicle/Bus
school_bus = Bus(100, 2000)
school_bus.mileage_info()
school_bus.seating_capacity(30)
school_bus.increase_speed(5)
school_bus.break_speed(7)

print(isinstance(school_bus, Vehicle))
print(isinstance(school_bus, Bus))


# 5. Створіть новий клас School з атрибутами екземпляра get_school_id і number_of_students та методами
# school_address, main_subject
class School():
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students

    def school_address(self, address):
        print(f"Address is {address}")

    def main_subject(self, subject):
        print(f"Main subject is {subject}")


# 6*. Створіть новий клас SchoolBus, який успадкує всі методи від School і Bus і матиме власний - bus_school_color
class SchoolBus(School, Bus):
    def __init__(self, get_school_id, number_of_students, max_speed, mileage):
        super().__init__(get_school_id, number_of_students)
        super(Bus, self).__init__(max_speed, mileage)

    def bus_school_color(self, color):
        print(f"Bus school color is {color}")


new_school_bus = SchoolBus(112, 30, 150, 5000)
print(new_school_bus.get_school_id)
print(new_school_bus.number_of_students)
print(new_school_bus.max_speed)
print(new_school_bus.mileage)
new_school_bus.school_address('Zhytomyr, Vitruka 132')
new_school_bus.main_subject('Math')
new_school_bus.seating_capacity(50)
new_school_bus.bus_school_color('orange')


# 7. Поліморфізм: Створіть два класи: Bear, Wolf. Обидва вони повинні мати метод eat. Створіть два екземпляри: від
# Ведмідь і від Вовк, створіть із нього кортеж і використовуючи спільну змінну, викличте метод eat.
class Animal:
    def __init__(self, name, food):
        self.name = name
        self.food = food

    def info(self):
        print(f"This animal is {self.name}")

    def eat(self):
        print(f"I eat {self.food}")


class Bear(Animal):
    pass


class Wolf(Animal):
    pass


bear = Bear('bear', 'fish')
wolf = Wolf('wolf', 'rabbits')

animals = (bear, wolf)

for animal in animals:
    animal.info()
    animal.eat()


# Магічні методи: Додатково: 8*. Створіть клас City з атрибутами екземпляра name i population, сторіть новий
# екземпляр цього класу, лише коли population > 1500, інакше повертається повідомлення: "Your city is too small".
# Підказка: використовуєте для цього завдання магічні методи

class City:
    def __init__(self, name, population):
        if population > 1500:
            self.name = name
            self.population = population
        else:
            print("Your city is too small")


berezivka = City('Berezivka', 500)
zhytomyr = City('Zhytomyr', 200000)

print(zhytomyr.name)
print(zhytomyr.population)