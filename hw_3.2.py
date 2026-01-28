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