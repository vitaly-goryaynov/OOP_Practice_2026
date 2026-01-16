class Animal:

    def __init__(self, name: str, view: str, age: int, weight: int, vaccinate: bool):
        self.name = name
        self.view = view
        self.age = age
        self.weight = weight
        self.vaccinate = vaccinate


animal1 = Animal('Burenka', 'cow', 10, 150, True )
animal2 = Animal('Bobik', 'dog', 5, 30, False )

