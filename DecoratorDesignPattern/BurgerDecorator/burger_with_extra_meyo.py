from DecoratorDesignPattern.BurgerDecorator.burger_decorator import BurgerDecorator, Burger


class ExtraMeyoBurger(BurgerDecorator):

    def __init__(self, burger_obj: Burger):
        self.burger = burger_obj

    def get_description(self):
        return self.burger.get_description() + " with extra meyo"

    def get_cost(self):
        return self.burger.get_cost() + 40

