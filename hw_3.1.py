# 1

class Animal:
    mame: str
    view: str
    age: int
    weight: int
    is_vaccine: bool


    def __init__(self, name: str, view: str, age: int, weight: int, is_vaccinate: bool):
        self.name = name
        self.view = view
        self.age = age
        self.weight = weight
        self.is_vaccinate = is_vaccinate


animal1 = Animal('Burenka', 'cow', 10, 150, True )
animal2 = Animal('Bobik', 'dog', 5, 30, False )


# 2 ---------------------------------------------------------------------------------------

class Artifacts:
    material: str
    historical_values: str
    power: int

    def __init__(self, material: str, historical_values: str, power: int):
        self.material = material
        self.historical_values = historical_values
        self.power = power


class DateRitual:
    day: int
    month: int
    year: int

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year


class SocietyMember:
    role: str
    clothes: str
    experience: int

    def __init__(self, role: str, clothes: str, experience: int):
        self.role = role
        self.clothes = clothes
        self.experience = experience


""" Во время проведения церемоний, класс Члены Общества, выбирает в классе Дата Ритуала 
точную дату проведения и используют в этот день определенные артефакты, выбирая их
в классе Артефакты.  
"""

# 3 -------------------------------------------------------------------------------------------

class UrbanFermersMarket:

    def __init__(self):
        pass

class FermersShop:
    name: str
    age: int
    products: list

    def __init__(self, name: str, age: int, products: list):
        self.name = name
        self.age = age
        self.products = products


class Product:
    name: str
    availability_piece: int

    def __init__(self, name: str, availability_piece: int):
        self.name = name
        self.availability_piece = availability_piece


class DateManufactureProduct:
    day: int
    month: int
    year: int

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year


class Buyer:
    name: str
    age: int
    demographic_characteristic: str
    product_preferences: list
    cash: float

    def __init__(self, name: str, age: int, demographic_characteristic: str, product_preferences: list, cash: float):
        self.name = name
        self.age = age
        self.demographic_characteristic = demographic_characteristic
        self.product_preferences = product_preferences
        self.cash = cash



""" Класс Городской Фермерский рынок место, где происходит торговля между классом Фермерские Лавки
и классом Покупатель, в лавках фермеров набор продуктов, которые хранятся в классе Продукты,
а создаются в классе Дата Производства Продукции.
"""