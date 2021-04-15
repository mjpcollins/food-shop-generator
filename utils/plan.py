import random
import datetime
from copy import deepcopy


class Plan:

    def __init__(self, data, rules, start_date, people):
        self._recipes = data.get_recipes()['meal']
        self._rules = rules
        self._people = people
        self._start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        self._meals = ['breakfast', 'brunch', 'lunch', 'dinner']

    def get_meal_plan(self, days):
        meal_plan = {}
        for datetime_date in (self._start_date + datetime.timedelta(n + 1) for n in range(days)):
            str_date = datetime_date.strftime("%Y-%m-%d")
            day = datetime_date.strftime("%A").lower()
            meal_plan[str_date] = {"day": day}
            meal_plan[str_date]['meals'] = {}
            for meal in self._meals:
                meal_plan[str_date]['meals'][meal] = self.pick_recipe(day=day, meal=meal)
        return meal_plan

    def pick_recipe(self, day, meal):
        category = f"{meal}_categories"
        speed = f"{meal}_speed"
        today_rules = self._rules[day]
        possible_recipes = []
        recipes = self._recipes.get(meal, [])
        for recipe_name in recipes:
            recipe_details = self._recipes[meal][recipe_name]
            in_cat = recipe_details["category"] in today_rules[category]
            in_speed = recipe_details["speed"] in today_rules[speed]
            if in_cat and in_speed:
                possible_recipes.append(recipe_name)
        if possible_recipes:
            chosen_recipe = random.choice(possible_recipes)
            return {chosen_recipe: self.align_servings(self._recipes[meal][chosen_recipe])}
        return {}

    def align_servings(self, recipe_data):
        recipe_data_copy = deepcopy(recipe_data)
        multiplier = self._people / recipe_data_copy['servings']
        recipe_data_copy['servings'] *= multiplier
        for ingredient in recipe_data_copy['ingredients']:
            ingredient['qty'] *= multiplier
        return recipe_data_copy
