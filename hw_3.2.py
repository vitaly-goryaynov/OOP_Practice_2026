# 1

class Animal:
    name: str
    view: str
    age: int

    def __init__(self, name, view, age):
        self.name = name
        self.view = view
        self.age = age


    def __str__(self):
        return f'Имя животного {self.name}, вид животного {self.view}, возраст животного {self.age}'

    def sound_animal(self, sound):
        return f'{sound} издал(-а) звук {self.name}'

cow1 = Animal('корова', 'пятнистая', 4)

print(cow1.sound_animal("мууу"))
print(cow1)


# 2

