class Pet:
    def _init_(self, name, animaltype, age):
        self.name = name
        self.animaltype = animaltype
        self.age = age
    def setname(self):
        return "{} is {} years old".format(self.name, self.age)