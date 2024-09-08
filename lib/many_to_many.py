# lib/many_to_many.py

class Author:
    all = []

    def __init__(self, name):
        self.name = name
        self._contracts = []  # List to store contracts for the author
        self.__class__.all.append(self)

    def contracts(self):
        """Returns a list of contracts associated with the author."""
        return self._contracts

    def books(self):
        """Returns a list of books associated with the author."""
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        """Creates a new contract between the author and a book."""
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        """Calculates the total royalties earned by the author from all contracts."""
        return sum([contract.royalties for contract in self._contracts])


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        self._contracts = []  # List to store contracts for the book
        self.__class__.all.append(self)

    def contracts(self):
        """Returns a list of contracts associated with the book."""
        return self._contracts

    def authors(self):
        """Returns a list of authors associated with the book."""
        return [contract.author for contract in self._contracts]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be of type Author")
        if not isinstance(book, Book):
            raise Exception("book must be of type Book")
        if not isinstance(date, str):
            raise Exception("date must be of type str")
        if not isinstance(royalties, int):
            raise Exception("royalties must be of type int")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        # Add this contract to both the author's and book's contract lists
        author._contracts.append(self)
        book._contracts.append(self)
        self.__class__.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        """Returns a list of contracts that match the given date."""
        return [contract for contract in cls.all if contract.date == date]

