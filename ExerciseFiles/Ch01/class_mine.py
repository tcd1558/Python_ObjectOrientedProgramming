# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPES=("HARDCOVER", "PAPERBACK", "EBOOK")

    # TODO: double-underscore properties are hidden from other classes
    __booklist = None

    # TODO: create a class method
    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES 

    # TODO: create a static method
    @staticmethod
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def setTitle(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if booktype in Book.BOOK_TYPES:
            self.booktype = booktype 
        else:
            print("ERROR: unknown Booktype")
            raise ValueError(f"{booktype} is not a valid book type")


# TODO: access the class attribute
print("Get the book types")
print(Book.getbooktypes())
print()


# TODO: Create some book instances
print("Create an instance b1 from class Book")
b1 = Book("Title 1", "HARDCOVER")
print(b1)
print()
print("Create an instance b2 from class Book with an illegal book type")
#b2 = Book("Title 2", "HARDBACK")
b2 = Book("Title 2", "PAPERBACK")
print(b2)
print()

# TODO: Use the static method to access a singleton object
thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
print("thebooks variable: ", thebooks)
print("Call Book.getbooklist(): ", Book.getbooklist())
