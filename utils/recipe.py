from copy import deepcopy


class Recipe:

    def __init__(self, name, meal, servings, category, speed, ingredients=None):
        self.name = name
        self.meal = meal
        self.servings = servings
        self.category = category
        self.speed = speed
        if ingredients:
            self._ingredients = ingredients
        else:
            self._ingredients = []

    def add_ingredient(self, item, qty, unit):
        self._ingredients.append({"item": item, "qty": qty, "unit": unit})

    def get_ingredients(self, servings=None):
        if servings:
            multiplier = servings / self.servings
        else:
            return self._ingredients
        ingredients = deepcopy(self._ingredients)
        for ing in ingredients:
            ing['qty'] *= multiplier
        return ingredients
