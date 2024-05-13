from DecoratorDesignPattern.Burger.french_burger import FrenchBurger
from DecoratorDesignPattern.Burger.ginger_burger import GingerBurger
from DecoratorDesignPattern.BurgerDecorator.burger_with_extra_meyo import ExtraMeyoBurger
from DecoratorDesignPattern.BurgerDecorator.burger_with_extra_cheese import ExtraCheeseBurger


ginger_burger = GingerBurger()
print(f"Burger: {ginger_burger.get_description()}")
print(f"Base Price: {ginger_burger.get_cost()}")

french_burger = FrenchBurger()
print(f"Burger: {french_burger.get_description()}")
print(f"Base Price: {french_burger.get_cost()}")

ginger_burger = ExtraMeyoBurger(ginger_burger)
print(ginger_burger.get_description())
print(ginger_burger.get_cost())

french_burger = ExtraCheeseBurger(french_burger)
print(french_burger.get_description())
print(french_burger.get_cost())

french_burger = ExtraMeyoBurger(french_burger)
print(french_burger.get_description())
print(french_burger.get_cost())

french_burger = ExtraCheeseBurger(french_burger)
print(french_burger.get_description())
print(french_burger.get_cost())

french_burger = ExtraMeyoBurger(french_burger)
print(french_burger.get_description())
print(french_burger.get_cost())
