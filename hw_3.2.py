# 1

class Animal:
    name: str
    view: str
    age: int

    def __init__(self, name:str, view:str, age:int):
        self.name = name
        self.view = view
        self.age = age


    def __str__(self) -> str:
        return f'Имя животного {self.name}, вид животного {self.view}, возраст животного {self.age}'

    def sound_animal(self, sound:str) -> str:
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


    def __str__(self) -> str:
        return f"Название книги {self.name}, автор {self.author}, количество страниц {self.number_pages}. "


    def open_pages(self, other: int) -> str:

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


    def __str__(self) -> str:
        return (f'Производитель самолёта {self.maker}, модель {self.model}, вместимость пассажиров {self.passenger_capacity}, '
                f'\nтекущая высота {self.current_height}, текущая скорость {self.current_speed}')


    def takeoff(self) -> str:
        return f'Самолёт взлетел!'


    def landing(self) -> str:
        return f'Самолёт приземлился!'


    def change_height(self, height:int) -> int:
        if height > 0:
            self.current_height = height
        return self.current_height


    def change_sped(self, speed:int) -> int:
        if speed > 0:
            self.current_speed = speed
        return self.current_speed


plane1 = PassengerPlane("Россия", "Ту - 777", 333, 0, 0)

print(plane1)
plane1.change_sped(400)
print(plane1.takeoff())
plane1.change_height(234)
print(plane1)
print(plane1.landing())


# 4

class MusicAlbum:
    author: str
    album: str
    genre: str
    list_track : list

    def __init__(self, author: str, album_name: str, genre: str, list_track=None):
        self.author = author
        self.album = album_name
        self.genre = genre
        self.list_track = []


    def __str__(self) -> str:
        return (f"Исполнитель {self.author}, название альбома {self.album}, жанр {self.genre},"
                f"список треков {self.list_track} ")


    def add_track(self, track: str) -> None:
        if track not in self.list_track:
            self.list_track.append(track)


    def del_track(self, track) -> None:
        self.list_track.remove(track)


    def play_track(self, track: str) -> str:
        return f"Трек {track} воспроизведён."


album1 = MusicAlbum('SnoopDog','Bang','Rap')
print(album1)

album1.add_track('yo')
album1.add_track('gav')
print(album1)
album1.del_track('yo')
print(album1)
print(album1.play_track('gAV'))





