class Students:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello {}".format(self.name))


a = Students("My name is Himal Acharya", 19)
b = Students("My name is ...", 20)
c  = Students("My name is ____", 25)


a.greet()
b.greet()
c.greet()


