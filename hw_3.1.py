# 1

class Animal:
    mame: str
    view: str
    age: int
    weight: int
    vaccine: bool


    def __init__(self, name: str, view: str, age: int, weight: int, vaccinate: bool):
        self.name = name
        self.view = view
        self.age = age
        self.weight = weight
        self.vaccinate = vaccinate


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


class Date_Ritual:
    day: int
    month: int
    year: int

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year


class Society_member:
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


