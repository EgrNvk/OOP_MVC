from Controller.oop_note_controller import NoteController
from Model.oop_note import Note


class ConsoleView:
    def __init__(self):
        self.__noteController = NoteController()

    def showAll(self):
        for elem in self.__noteController.getAll():
            print(f"${elem.title()}\n${elem.text()}\n\n")
    def add(self):
        print("Enter title ")
        title = input()
        print("Enter text ")
        text = input()

        newNote = Note(title, text)

        self.__noteController.add(newNote)

        # self.__noteController.add(Note(input("Enter Title"),input("Enter Text")))

# 1) Добавить метод поиска заметки по заголовку
    def find_by_title(self):
        title = input("Введіть шаблон пошуку ")
        note=self.__noteController.find_by_title(title)

