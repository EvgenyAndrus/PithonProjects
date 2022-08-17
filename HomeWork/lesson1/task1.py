"""
Задание 1
Создайте класс, описывающий книгу. Он должен содержать информацию об авторе, названии, годе издания и жанре.
Создайте несколько разных книг. Определите для него операции проверки на равенство и неравенство,
методы __repr__ и __str__.

Задание 2
Создайте класс, описывающий отзыв к книге. Добавьте в класс книги поле – список отзывов.
Сделайте так, что при выводе книги на экран при помощи функции print также будут выводиться отзывы к ней.
"""


class BookReviews:
    _reviews = list

    def __init__(self, review):
        if type(review) is str:
            self._reviews = [review]
        else:
            self._reviews = []

    def __repr__(self):
        return self._reviews

    def get_reviews(self):
        text = ''
        for i in self._reviews:
            text += '\n\t' + i
        return text + '\n'

    def set_review(self, text):
        if type(text) is str:
            self._reviews.append(text)
        else:
            pass

    @property
    def reviews(self):
        return self._reviews

    @reviews.setter
    def reviews(self):
        pass


class Book:
    _author = str
    _genre = str
    _title = str
    _year_of_publishing = int
    _BookReviews = None

    def __init__(self, author=None, genre=None, title=None, year_of_publishing=0, review=None):
        self._author = author
        self._genre = genre
        self._title = title
        self._year_of_publishing = year_of_publishing
        self._BookReviews = BookReviews(review)

    def __repr__(self):
        return '{} {} {} {} {}' \
            .format(self._author, self._title,
                    self._genre, self._year_of_publishing, self._BookReviews.reviews)

    def __str__(self):
        return 'Author: {}\n' \
               'Title: {}\n' \
               'Genre: {}\n' \
               'Year of publishing: {}\n' \
               'reviews: {}' \
            .format(self._author, self._title,
                    self._genre, self._year_of_publishing, self._BookReviews.get_reviews())

    def __eq__(self, other):
        return self._author == other._author \
               and self._genre == other._genre \
               and self._title == other._title \
               and self._year_of_publishing == other._year_of_publishing

    def __ne__(self, other):
        if self._author != other._author \
                and self._genre != other._genre \
                and self._title != other._title \
                and self._year_of_publishing != other._year_of_publishing:
            return True
        else:
            return False

    def get_book_reviews(self):
        return self._BookReviews

    def get_author(self):
        return self._author

    def get_genre(self):
        return self._genre

    def get_title(self):
        return self._title

    def get_year_of_publishing(self):
        return self._year_of_publishing

    def set_author(self, value):
        self._author = value

    def set_genre(self, value):
        self._genre = value

    def set_title(self, value):
        self._title = value

    def set_year_of_publishing(self, value):
        self._year_of_publishing = value



