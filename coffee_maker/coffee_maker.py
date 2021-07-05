from menu import Menu


class CoffeeIngredients:
    def __init__(self, water=0, coffee=0, milk=0):
        self.water = water
        self.coffee = coffee
        self.milk = milk

    def manage_water(self, water):
        self.water = water

    def manage_coffee(self, coffee):
        self.coffee = coffee

    def manage_milk(self, milk):
        self.milk = milk

    def deduct_resource(self, water, coffee, milk):
        self.manage_water(water)
        self.manage_coffee(coffee)
        self.manage_milk(milk)


class CoffeeMaker:
    def __init__(self, state="on", order=None):
        self.state = state
        self.menu = Menu()
        self.order = order

    def display_info(self):
        self.menu.coffee_catalog()

    def get_user_order(self):
        self.order = int(input("Choose your coffee."))
        return self.menu.get_coffee_recipe(self.order)


if __name__ == "__main__":
    coffee_machine = CoffeeMaker()
    coffee_machine.display_info()
    user_coffee = coffee_machine.get_user_order()
    print(user_coffee.name)
