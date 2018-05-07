class House:

    def __init__ (self, floor, entrance, cost):
        self.floor = floor
        self.entrance = entrance
        self.cost = cost

    def __repr__(self):
        return "It's looking good house, it has {floor} floors and {entrance} entrances, but it {cost}". format(floor=self.floor, entrance=self.entrance, cost=self.cost)

    @staticmethod
    def shock():
        return "It's too expencive !!!"

New_House = House("12", "5", "150 000$")

print(New_House)

print(New_House.shock())
