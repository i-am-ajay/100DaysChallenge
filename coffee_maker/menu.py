class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cost = cost


class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name="Latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="Espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="Cappuccino", water=250, milk=50, coffee=24, cost=3)
        ]

    def coffee_catalog(self):
        count = 1
        for coffee in self.menu:
            print(f"{count}. {coffee.name}( {coffee.cost} )")
            count += 1

    def get_coffee_recipe(self, index):
        index = index-1
        return self.menu[index]
