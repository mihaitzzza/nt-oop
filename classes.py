from abc import abstractmethod


class Ingredient:
    def __init__(self, name, price, cook_time):
        self._name = name
        self._price = price
        self.cook_time = cook_time

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    def __str__(self):
        return self._name

    def __repr__(self):
        return self.__str__()


class PizzaIngredient(Ingredient):
    def __init__(self, name, price, cook_time, quantity):
        super().__init__(name, price, cook_time)
        self._quantity = quantity

    @property
    def quantity(self):
        return self._quantity


class Dish:
    @abstractmethod
    def bake(self):
        pass

    @abstractmethod
    def deliver(self):
        pass


class Pizza(Dish):
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = [
            PizzaIngredient(
                ingredient[0].name,
                ingredient[0].price,
                ingredient[0].cook_time,
                ingredient[1]
            )
            for ingredient in ingredients
        ]

    @property
    def price(self):
        price = 0

        for ingredient in self.ingredients:
            price += ingredient.quantity * ingredient.price

        return price + 10 + 5

    @property
    def cook_time(self):
        cook_time = 0

        for ingredient in self.ingredients:
            cook_time += ingredient.quantity * ingredient.cook_time

        return cook_time

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def bake(self):
        print('This will be ready in %s. Come back later!' % self.cook_time)

    def deliver(self):
        pass


class Salad(Dish):
    def bake(self):
        pass

    def deliver(self):
        pass
