class Book:

    def __init__ (self, name, exemplar, cost):
        self.name = name
        self.exemplar = exemplar
        self.cost = cost

    def __repr__(self):
        return "This author very famous, his name is {name}, his book published by {exemplar} books aroud the world and it's {cost}". format(name=self.name, exemplar=self.exemplar, cost=self.cost)

    @staticmethod
    def viva():
        return "Super book !!!"

Conan_Doil = Book("Arthur Conan Doil", "100 mln", "25$")
#ronaldo = Football("Ronaldo", "40", "have a lot of money")

print(Conan_Doil)

print(Conan_Doil.viva())

#print(ronaldo)

#print(ronaldo.goll())
