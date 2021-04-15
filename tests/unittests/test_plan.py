import random
import datetime
from unittest import TestCase
from tests.unittests_utils.misc import *
from utils import Data, Plan


class TestPlan(TestCase):

    def setUp(self):
        random.seed(1)
        self.rules = {
            "monday": {
                "breakfast_categories": ["veggie", "vegan", "fish"],
                "brunch_categories": [],
                "lunch_categories": ["veggie", "vegan", "fish"],
                "dinner_categories": ["veggie", "vegan", "fish"],
                "breakfast_speed": ["very_fast"],
                "brunch_speed": [],
                "lunch_speed": ["very_fast"],
                "dinner_speed": ["very_fast", "fast", "medium"]
            },
            "sunday": {
                "breakfast_categories": ["veggie", "vegan", "fish", "meat"],
                "brunch_categories": [],
                "lunch_categories": ["veggie", "vegan", "fish", "meat"],
                "dinner_categories": ["meat"],
                "breakfast_speed": ["very_fast"],
                "brunch_speed": [],
                "lunch_speed": ["very_fast"],
                "dinner_speed": ["very_fast", "fast", "medium", "slow", "very_slow"]
            }
        }
        self._filepath = "./tests/test_data/recipes.json"
        create_recipe_file(self._filepath)
        self.d = Data(self._filepath)
        self.p = Plan(self.d, self.rules, "2021-04-17", people=2)
        self.maxDiff = None

    def test_init(self):
        self.assertEqual(self.d.get_recipes()['meal'], self.p._recipes)
        self.assertEqual(self.rules, self.p._rules)
        self.assertEqual(datetime.datetime(year=2021, month=4, day=17),
                         self.p._start_date)
        self.assertEqual(2, self.p._people)
        self.assertEqual(['breakfast', 'brunch', 'lunch', 'dinner'], self.p._meals)

    def test_two_day_plan(self):
        expected_meal_plan = {
            "2021-04-18": {
                "day": "sunday",
                "meals": {
                    "breakfast": {"overnight_oats": {"speed": "very_fast", "category": "veggie", "servings": 2.0, "ingredients": [{"item": "oats", "qty": 200.0, "unit": "g"}, {"item": "milk", "qty": 175.0, "unit": "ml"}]}},
                    "brunch": {},
                    "lunch": {"basic": {"servings": 2.0,"category": "veggie","speed": "very_fast","ingredients": [{"item": "salad","qty": 2.0,"unit": "handful"},{"item": "tomatoes","qty": 2.0,"unit": "amount"},{"item": "bread","qty": 4.0,"unit": "slice"},{"item": "cheese","qty": 250.0,"unit": "g"}]}},
                    "dinner": {"roast_pork": {"speed": "slow", "servings": 2.0,"category": "meat","ingredients": [{"item": "pork_loin","qty": 1.0,"unit": "amount"},{"item": "potatoes","qty": 500.0,"unit": "g"},{"item": "carrots","qty": 300.0,"unit": "g"},{"item": "broccoli","qty": 300.0,"unit": "g"}]}}
                }
            },
            "2021-04-19": {
                "day": "monday",
                "meals": {
                    "breakfast": {"overnight_oats": {"speed": "very_fast", "category": "veggie", "servings": 2.0, "ingredients": [{"item": "oats", "qty": 200.0, "unit": "g"}, {"item": "milk", "qty": 175.0, "unit": "ml"}]}},
                    "brunch": {},
                    "lunch": {"basic": {"servings": 2.0,"category": "veggie","speed": "very_fast","ingredients": [{"item": "salad","qty": 2.0,"unit": "handful"},{"item": "tomatoes","qty": 2.0,"unit": "amount"},{"item": "bread","qty": 4.0,"unit": "slice"},{"item": "cheese","qty": 250.0,"unit": "g"}]}},
                    "dinner": {"tomato_and_marsc_risotto": {"speed": "fast", "servings": 2.0,"category": "veggie","ingredients": [{"item": "risotto","qty": 200.0,"unit": "g"},{"item": "tomatoes","qty": 6.0,"unit": "amount"},{"item": "garlic_paste","qty": 1.0,"unit": "teaspoon"},{"item": "marscarpone","qty": 125.0,"unit": "g"},{"item": "chicken_stock_cubes","qty": 2.0,"unit": "amount"},{"item": "white_wine_vinegar","qty": 25.0,"unit": "ml"},{"item": "salad","qty": 2.0,"unit": "handful"}]}}
                }
            }
        }
        actual_meal_plan = self.p.get_meal_plan(days=2)
        self.assertEqual(expected_meal_plan, actual_meal_plan)

    def test_pick_recipe(self):
        expected_recipe = {"roast_pork": {"speed": "slow", "servings": 2.0,"category": "meat","ingredients": [{"item": "pork_loin","qty": 1.0,"unit": "amount"},{"item": "potatoes","qty": 500.0,"unit": "g"},{"item": "carrots","qty": 300.0,"unit": "g"},{"item": "broccoli","qty": 300.0,"unit": "g"}]}}
        actual_recipe = self.p.pick_recipe('sunday', 'dinner')
        self.assertEqual(expected_recipe, actual_recipe)

    def test_align_servings(self):
        input_recipe = {"speed": "very_fast", "category": "veggie", "servings": 8, "ingredients": [{"item": "oats", "qty": 800, "unit": "g"}, {"item": "milk", "qty": 700, "unit": "ml"}]}
        expected_recipe = {"speed": "very_fast", "category": "veggie", "servings": 2.0, "ingredients": [{"item": "oats", "qty": 200.0, "unit": "g"}, {"item": "milk", "qty": 175.0, "unit": "ml"}]}
        actual_recipe = self.p.align_servings(input_recipe)
        self.assertEqual(expected_recipe, actual_recipe)

