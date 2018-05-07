class Football:

    def __init__ (self, name, age, money):
        self.name = name
        self.age = age
        self.money = money

    def __repr__(self):
        return "I know about you, your name is {name}, your age is {age} and you {money}". format(name=self.name, age=self.age, money=self.money)

    @staticmethod
    def goll():
        return "GOOOL !!!"

messi = Football("Messi", "30", "are F.. rich")
ronaldo = Football("Ronaldo", "40", "have a lot of money")

print(messi)

print(messi.goll())

print(ronaldo)

print(ronaldo.goll())
