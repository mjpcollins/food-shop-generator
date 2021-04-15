from unittest import TestCase
from utils import Recipe


class TestRecipe(TestCase):

    def setUp(self):
        self.r = Recipe(name="peanut_butter_toast",
                        meal="breakfast",
                        servings=1)
        self.r_with_ingredients = Recipe(name="peanut_butter_toast",
                                         meal="breakfast",
                                         servings=1,
                                         ingredients=[{"item":  "bread", "qty":  1, "unit":  "slice"},
                                                      {"item":  "peanut_butter", "qty":  1, "unit":  "tablespoon"},
                                                      {"item":  "banana", "qty":  1, "unit":  "amount"}])

    def test_init(self):
        self.assertEqual("peanut_butter_toast", self.r.name)
        self.assertEqual("breakfast", self.r.meal)
        self.assertEqual(1, self.r.servings)
        self.assertEqual([], self.r._ingredients)
        self.assertEqual("peanut_butter_toast", self.r_with_ingredients.name)
        self.assertEqual("breakfast", self.r_with_ingredients.meal)
        self.assertEqual(1, self.r_with_ingredients.servings)
        self.assertEqual([{"item":  "bread", "qty":  1, "unit":  "slice"},
                          {"item":  "peanut_butter", "qty":  1, "unit":  "tablespoon"},
                          {"item":  "banana", "qty":  1, "unit":  "amount"}],
                         self.r_with_ingredients._ingredients)

    def test_add_ingredient(self):
        expected_ingredients = [
          {
            "item":  "bread",
            "qty":  1,
            "unit":  "slice"
          }
        ]
        self.assertEqual([], self.r._ingredients)
        self.r.add_ingredient(item="bread",
                              qty=1,
                              unit="slice")
        self.assertEqual(expected_ingredients, self.r._ingredients)

    def test_get_ingredients(self):
        expected_ingredients = [{"item": "bread", "qty": 1, "unit": "slice"},
                                {"item": "peanut_butter", "qty": 1, "unit": "tablespoon"},
                                {"item": "banana", "qty": 1, "unit": "amount"}]
        actual_ingredients = self.r_with_ingredients.get_ingredients()
        self.assert_ingredients(expected_ingredients, actual_ingredients)

    def test_get_ingredients_4_servings(self):
        expected_ingredients = [{"item":  "bread", "qty":  4.0, "unit":  "slice"},
                                {"item":  "peanut_butter", "qty":  4.0, "unit":  "tablespoon"},
                                {"item":  "banana", "qty":  4.0, "unit":  "amount"}]
        actual_ingredients = self.r_with_ingredients.get_ingredients(servings=4)
        self.assert_ingredients(expected_ingredients, actual_ingredients)

    def assert_ingredients(self, expected_ingredients, actual_ingredients):
        self.assertEqual(expected_ingredients, actual_ingredients)
        self.assertEqual([{"item":  "bread", "qty":  1, "unit":  "slice"},
                          {"item":  "peanut_butter", "qty":  1, "unit":  "tablespoon"},
                          {"item":  "banana", "qty":  1, "unit":  "amount"}],
                         self.r_with_ingredients._ingredients)
