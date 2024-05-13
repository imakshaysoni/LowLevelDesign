from DecoratorDesignPattern.Burger.burger import Burger


class GingerBurger(Burger):

    def get_description(self):
        return "Ginger Burger"

    def get_cost(self):
        return 200
