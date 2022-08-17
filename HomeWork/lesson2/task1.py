# Задание 1
# Создайте класс Editor, который содержит методы view_document и edit_document.
# Пусть метод edit_document выводит на экран информацию о том,
# что редактирование документов недоступно для бесплатной версии.
# Создайте подкласс ProEditor, в котором данный метод будет переопределён.
# Введите с клавиатуры лицензионный ключ и, если он корректный,
# создайте экземпляр класса ProEditor, иначе Editor.
# Вызовите методы просмотра и редактирования документов.
import sys


class Editor:
    def view_document(self):
        print('view document')

    def edit_document(self):
        print('not available for free version')


class ProEditor(Editor):
    def edit_document(self):
        print('edit_document')


def main():
    print('menu:\n'
          '1 - view document\n'
          '2 - edit document\n'
          '0 - quit')

    response = int(input('Enter a num: '))
    if response == 1:
        editor = Editor()
        editor.view_document()
    elif response == 2:
        key = input('Enter a key: ')
        if key == '1111':
            editor = ProEditor()
            editor.edit_document()
        else:
            editor = Editor()
            editor.edit_document()
    elif response == 0:
        print("quit")
        sys.exit()
    else:
        print('error')


if __name__ == '__main__':
    main()
