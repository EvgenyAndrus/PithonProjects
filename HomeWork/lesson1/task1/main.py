from task1 import Book


def main():
    book1 = Book('J. K. Rowling', 'Fantasy', 'Harry Potter and the Sorcerer\'s Stone', 2019, 'super')
    book2 = Book('Jane Austen', 'romance', 'Pride and Prejudice', 1995)
    book3 = Book('author', 'genre', 'title', 1980)
    book4 = Book('J. K. Rowling', 'Fantasy', 'Harry Potter and the Sorcerer\'s Stone', 2019, 2)

    for i in range(10):
        book1.get_book_reviews().set_review('{} good book'.format(i))

    for i in range(3):
        book3.get_book_reviews().set_review('{} good book'.format(i))

    print(book1)
    print(repr(book1))

    book3.get_book_reviews().set_review(20)
    print(book2)
    print(book3)
    print(book4)
    print(book1 != book3)  # True
    print(book1 == book2)  # False
    print(book3 == book2)  # False
    print(book1 == book4)  # True
    print(book1 != book4)  # False


if __name__ == '__main__':
    main()
