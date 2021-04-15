import os
import json
from copy import deepcopy
from unittest import TestCase
from utils import Data, Recipe


class TestData(TestCase):

    def setUp(self):
        self._expected_recipes()
        self._filepath = "./tests/test_data/recipes.json"
        self._create_recipe_file()
        self.r = Recipe(name="peanut_butter_toast",
                        meal="breakfast",
                        servings=1,
                        ingredients=[{"item":  "bread", "qty":  1, "unit":  "slice"},
                                     {"item":  "peanut_butter", "qty":  1, "unit":  "tablespoon"},
                                     {"item":  "banana", "qty":  1, "unit":  "amount"}])
        self.d = Data(filepath=self._filepath)

    def tearDown(self):
        self._remove_recipe_file()

    def test_init(self):
        self.assertEqual("./tests/test_data/recipes.json", self.d.filepath)
        self.assertEqual(self.starting_recipes, self.d._data)

    def test_load(self):
        self.d._data = {}
        self.assertEqual({}, self.d._data)
        self.assertEqual(self.starting_recipes, self.d._load())
        self.assertEqual(self.starting_recipes, self.d._data)

    def test_add_recipe(self):
        self.assertEqual(self.starting_recipes, self.d._data)
        self.d.add_recipe(self.r)
        self.assertEqual(self.starting_recipes_plus_one, self.d._data)

    def test_get_recipes(self):
        self.d._data = {}
        self.assertEqual({}, self.d.get_recipes())
        self.d._data = self.starting_recipes
        self.assertEqual(self.starting_recipes, self.d.get_recipes())

    def _create_recipe_file(self):
        self._remove_recipe_file()
        with open(self._filepath, 'w') as F:
            F.write(json.dumps(self.starting_recipes, indent=1))

    def _remove_recipe_file(self):
        try:
            os.remove(self._filepath)
        except FileNotFoundError:
            pass

    def _expected_recipes(self):
        self.starting_recipes = {
            "meal": {
                "breakfast": {
                    "overnight_oats": {
                        "servings": 8,
                        "ingredients": [
                            {
                                "item": "oats",
                                "qty": 800,
                                "unit": "g"
                            },
                            {
                                "item": "milk",
                                "qty": 700,
                                "unit": "ml"
                            }
                        ]
                    }
                },
                "lunch": {
                    "basic": {
                        "servings": 1,
                        "ingredients": [
                            {
                                "item":  "salad",
                                "qty":  1,
                                "unit":  "handful"
                            },
                            {
                                "item":  "tomatoes",
                                "qty":  1,
                                "unit":  "amount"
                            },
                            {
                                "item":  "bread",
                                "qty":  2,
                                "unit":  "slice"
                            },
                            {
                                "item":  "cheese",
                                "qty":  125,
                                "unit":  "g"
                            }
                        ]
                    }
                }
            }
        }
        self.starting_recipes_plus_one = deepcopy(self.starting_recipes)
        self.starting_recipes_plus_one['meal']['breakfast']["peanut_butter_toast"] = {
            "servings": 1,
            "ingredients": [
                {
                    "item":  "bread",
                    "qty":  1,
                    "unit":  "slice"
                },
                {
                    "item":  "peanut_butter",
                    "qty":  1,
                    "unit":  "tablespoon"
                },
                {
                    "item":  "banana",
                    "qty":  1,
                    "unit":  "amount"
                }
            ]
        }
