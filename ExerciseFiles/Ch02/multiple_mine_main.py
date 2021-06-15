# Python Object Oriented Programming by Joe Marini course example
# Understanding multiple inheritance


class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.common = "A"


class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.common = "B"


class C(B, A):
    def __init__(self):
        super().__init__()

    def showprops(self):
        print(self.foo, self.bar)
        # Method resolution order (__mro__):
        # first in class C
        # then according to the parameters (A, B):
        # first class A, then class B
        # last from the superclass object
        # This is also defined in the variable __mro__
        print(self.common)


c = C()
c.showprops()
print(C.__mro__)
