


class Circle:
    pi = 3.14
    def __init__(self, r):
        self.r = r

    def area(self, *args):
       r = args[0] if args else self.r
       return self.pi * r * r