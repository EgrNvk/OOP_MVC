class NoteController:
    def __init__(self):
        self.__notes=[]

    def add(self, note):
        self.__notes.append(note)
    def delete(self, note):
        self.__notes.remove(note)

    def getAll(self):
        return self.__notes

# 1) Добавить метод поиска заметки по заголовку
    def find_by_title(self, title):
        for element in self.__notes:
            if element.title == title:
                return element
        return None