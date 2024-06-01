# ÖRNEK 1
# Metin Editöründe Karakterler

class CharacterFlyweight:
    def __init__(self, font, size, color):
        self.font = font
        self.size = size
        self.color = color

    def display(self, position):
        print(f'Character with font={self.font}, size={self.size}, color={self.color} at position={position}')


class CharacterFactory:
    _characters = {}

    @staticmethod
    def get_character(font, size, color):
        key = (font, size, color)
        if key not in CharacterFactory._characters:
            CharacterFactory._characters[key] = CharacterFlyweight(font, size, color)
        return CharacterFactory._characters[key]


class Document:
    def __init__(self):
        self.characters = []

    def add_character(self, char, font, size, color, position):
        character_flyweight = CharacterFactory.get_character(font, size, color)
        self.characters.append((char, character_flyweight, position))

    def display(self):
        for char, flyweight, position in self.characters:
            flyweight.display(position)
            print(f'Displaying character "{char}" at {position}')

# Kullanım
document = Document()
document.add_character('H', 'Arial', 12, 'Black', (0, 0))
document.add_character('e', 'Arial', 12, 'Black', (1, 0))
document.add_character('l', 'Arial', 12, 'Black', (2, 0))
document.add_character('l', 'Arial', 12, 'Black', (3, 0))
document.add_character('o', 'Arial', 12, 'Black', (4, 0))
document.add_character('!', 'Arial', 12, 'Black', (5, 0))

document.display()


