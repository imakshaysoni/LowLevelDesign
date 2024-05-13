from DecoratorDesignPattern.Burger.burger import Burger


class FrenchBurger(Burger):

    def get_description(self):
        return "French Burger"

    def get_cost(self):
        return 500
