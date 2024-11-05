# Kelas dasar (Parent Class)
class Book:
    def __init__(self, title, author):
        self._title = title  # Protected attribute
        self._author = author  # Protected attribute

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        self._title = new_title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        self._author = new_author

    def info(self):
        return f"'{self.title}' by {self.author}"

# Kelas turunan (Child Class)
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self._file_size = file_size  # Protected attribute

    @property
    def file_size(self):
        return self._file_size

    @file_size.setter
    def file_size(self, new_file_size):
        self._file_size = new_file_size

    def info(self):
        return f"{super().info()} - File size: {self.file_size}MB"

# Contoh penggunaan
if __name__ == "__main__":
    # Membuat objek Book dan EBook
    book = Book("The Great Gatsby", "F. Scott Fitzgerald")
    ebook = EBook("1984", "George Orwell", 1.5)

    # Menggunakan metode info
    print(book.info())  # Output: 'The Great Gatsby' by F. Scott Fitzgerald
    print(ebook.info())  # Output: '1984' by George Orwell - File size: 1.5MB

    # Menggunakan setter dan getter
    book.title = "The Great Gatsby (Updated)"
    print(book.info())  # Output: 'The Great Gatsby (Updated)' by F. Scott Fitzgerald

    ebook.file_size = 2.0
    print(ebook.info())  # Output: '1984' by George Orwell - File size: 2.0MB