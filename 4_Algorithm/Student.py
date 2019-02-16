class Student:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

    def __str__(self):
        return "{}번 {}".format(self.id, self.name)

    def __lt__(self, other):
        return self.id < other.id


    def __eq__(self, other):
        return self.id == other.id
