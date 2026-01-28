# 1

class Animal:
    name: str
    view: str
    age: int

    def __init__(self, name:str, view:str, age:int):
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

class Book:
    name: str
    author: str
    number_pages: int

    def __init__(self, name:str, author:str, number_pages:int):
        self.name = name
        self.author = author
        self.number_pages = number_pages


    def __str__(self):
        return f"Название книги {self.name}, автор {self.author}, количество страниц {self.number_pages}. "


    def open_pages(self, other):

        if other > self.number_pages: return f"Книга не может быть открыта! Нет столько страниц."

        return f"Страница {other} открыта"


book1 = Book('Кошки', "Куклачёв", 76)

print(book1)
print(book1.open_pages(77))
print(book1.open_pages(27))


# 3

class PassengerPlane:
    maker: str
    model: str
    passenger_capacity: int
    current_height: int
    current_speed: int

    def __init__(self, maker:str, model:str, passenger_capacity:int, current_height:int, current_speed:int):
        self.maker = maker
        self.model = model
        self.passenger_capacity = passenger_capacity
        self.current_height = current_height
        self.current_speed = current_speed


    def __str__(self):
        return (f'Производитель самолёта {self.maker}, модель {self.model}, вместимость пассажиров {self.passenger_capacity}, '
                f'\nтекущая высота {self.current_height}, текущая скорость {self.current_speed}')


    def takeoff(self):
        return f'Самолёт взлетел!'


    def landing(self):
        return f'Самолёт приземлился!'


    def change_height(self, height:int) -> int:
        self.current_height = height
        return self.current_height


    def change_sped(self, speed:int) -> int:
        self.current_speed = speed
        return self.current_speed


plane1 = PassengerPlane("Россия", "Ту - 777", 333, 0, 0)

print(plane1)
plane1.change_sped(400)
print(plane1.takeoff())
plane1.change_height(234)
print(plane1)
print(plane1.landing())
