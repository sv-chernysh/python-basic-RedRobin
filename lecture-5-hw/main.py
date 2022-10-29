# 1.
# class Laptop:
#     """
#     Make the class with composition.
#     """
# class Battery:
#     """
#     Make the class with composition.
#     """
class Laptop:
    def __init__(self):
        battery_1 = Battery('Battery_1 - 2000 mAh')
        battery_2 = Battery('Battery_2 - 2500 mAh')
        self.laptop = [battery_1.capacity, battery_2.capacity]


class Battery:
    def __init__(self, capacity):
        self.capacity = capacity


hp = Laptop()
print(hp.laptop)


# 2.
# class Guitar:
#     """
#     Make the class with aggregation
#     """
# class GuitarString:
#     """
#     Make the class with aggregation
#     """
class Guitar:
    def __init__(self, string):
        self.string = string


class GuitarString:
    def __init__(self, string_type):
        self.string_type = string_type


classical_string = GuitarString('classical')
cort = Guitar(classical_string)


# 3
# class Calc:
#     """
#     Створіть клас з одним методом "add_nums" та 3 атрибутами, який повертає суму цих атрибутів.
#     """
class Calc:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def add_nums(self):
        print(f'{self.a + self.b + self.c}')


Calc(5, 4, 3).add_nums()


# 4*.
# class Pasta:
#     """
#     Створіть клас, який приймає 1 атрибут при ініціалізації - ingredients і визначає інгридієнти атрибута екземпляра.
#     Він повинен мати 2 методи:
#     carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
#     which should create Pasta instances with predefined list of ingredients.
#     Example:
#         pasta_1 = Pasta(["tomato", "cucumber"])
#         pasta_1.ingredients will equal to ["tomato", "cucumber"]
#         pasta_2 = Pasta.bolognaise()
#         pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
#     """
class Pasta:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def carbonara(cls):
        return cls(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise(cls):
        return cls(['bacon', 'parmesan', 'eggs'])


print(Pasta(["tomato", "cucumber"]).ingredients)
print(Pasta.carbonara().ingredients)
print(Pasta.bolognaise().ingredients)
