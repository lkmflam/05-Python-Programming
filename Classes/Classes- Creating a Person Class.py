class Person:
    #Stage 1 of Person Class

    #We will expand on this.

    firstName = "James"
    lastName = "Bond"
    birthday = "08/21/1800"
    age = "200"
    email = "someEmail@email.com"

    def f(self):
        return "This is the Person class"

# This is the instantiation of class Person as object x
x = Person()

# This is using object x
print(x.f())
print("This person's name is: {} {}".format(x.firstName, x.lastName))

# We can also do this...
print(Person.firstName)

#Stage 2 of Person Class

#We will expand on this.

'''def __init__(self, firstName, lastName, birthday, age, email):
    self.firstName = firstName
    self.lastName = lastName
    self.birthday = birthday
    self.age = age
    self.email = email

def printDetails(self):
    print("First Name: {}".format(self.firstName))
    print("First Name: {}".format(self.lastName))
    print("First Name: {}".format(self.birthday))
    print("First Name: {}".format(self.age))
    print("First Name: {}".format(self.email))

# This is the instantiation of class Person as object x
x = Person("James", "Bond", "08/21/1800", 200, "someEmail@email.com")
x.printDetails()'''