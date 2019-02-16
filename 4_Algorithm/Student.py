class Student:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

    def __str__(self):
        return "{}번 {}".format(self.id, self.name)

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.id < other.id
        else:
            return self.id < other


    def __eq__(self, other):
        if isinstance(other, Student):
            return self.id == other.id
        else:
            return self.id == other