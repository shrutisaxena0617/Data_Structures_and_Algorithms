class Resume:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def fullname(self):
        name = self.name + ' ' + self.surname
        return name

    def address(self):
        pass

def isEmpty(lis):
    return lis.size > 0



