from DecoratorDesignPattern.Burger.burger import Burger
from DecoratorDesignPattern.BurgerDecorator.burger_decorator import BurgerDecorator


class ExtraCheeseBurger(BurgerDecorator):
    def __init__(self, burger_obj: Burger):
        self.burger = burger_obj

    def get_description(self):
        return self.burger.get_description() + "With Extra Cheese"

    def get_cost(self):
        return self.burger.get_cost() + 10

