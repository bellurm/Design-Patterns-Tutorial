# Used Flyweight Pattern
import tkinter as tk

class CharacterFlyweight:
    def __init__(self, font, size, color):
        self.font = font
        self.size = size
        self.color = color

    def display(self, text_widget, char):
        text_widget.config(font=(self.font, self.size), fg=self.color)
        text_widget.insert(tk.END, char)

class CharacterFactory:
    _characters = {}

    @staticmethod
    def get_character(font, size, color):
        key = (font, size, color)
        if key not in CharacterFactory._characters:
            CharacterFactory._characters[key] = CharacterFlyweight(font, size, color)
        return CharacterFactory._characters[key]

class TextEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor")
        self.root.geometry("1000x700")

        self.text_input = tk.Text(self.root, wrap=tk.WORD, font=("Arial", 12), fg="black")
        self.text_input.pack(expand=True, fill='both')

        self.font_family = "Arial"
        self.font_size = 12
        self.font_color = "black"

        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        self.font_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="Font", menu=self.font_menu)

        self.font_menu.add_command(label="Arial", command=lambda: self.set_font("Arial"))
        self.font_menu.add_command(label="Times New Roman", command=lambda: self.set_font("Times New Roman"))
        self.font_menu.add_command(label="Courier New", command=lambda: self.set_font("Courier New"))

        self.size_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="Size", menu=self.size_menu)

        for size in range(8, 21):
            self.size_menu.add_command(label=str(size), command=lambda s=size: self.set_size(s))

        self.color_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="Color", menu=self.color_menu)

        self.color_menu.add_command(label="Black", command=lambda: self.set_color("black"))
        self.color_menu.add_command(label="Red", command=lambda: self.set_color("red"))
        self.color_menu.add_command(label="Blue", command=lambda: self.set_color("blue"))

    def set_font(self, font_family):
        self.font_family = font_family
        self.update_text()

    def set_size(self, font_size):
        self.font_size = font_size
        self.update_text()

    def set_color(self, font_color):
        self.font_color = font_color
        self.update_text()

    def update_text(self):
        text_content = self.text_input.get("1.0", "end-1c")
        self.text_input.delete("1.0", tk.END)
        for char in text_content:
            character_flyweight = CharacterFactory.get_character(self.font_family, self.font_size, self.font_color)
            character_flyweight.display(self.text_input, char)

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditorApp(root)
    root.mainloop()
