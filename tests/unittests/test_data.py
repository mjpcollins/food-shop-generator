from unittest import TestCase
from tests.unittests_utils.misc import *
from utils import Data, Recipe


class TestData(TestCase):

    def setUp(self):
        self.starting_recipes = get_starting_recipes()
        self.starting_recipes_plus_one = get_starting_recipes_plus_one(self.starting_recipes)
        self._filepath = "./tests/test_data/recipes.json"
        create_recipe_file(self._filepath)
        self.r = Recipe(name="peanut_butter_toast",
                        meal="breakfast",
                        servings=1,
                        category="veggie",
                        speed="very_fast",
                        ingredients=[{"item":  "bread", "qty":  1, "unit":  "slice"},
                                     {"item":  "peanut_butter", "qty":  1, "unit":  "tablespoon"},
                                     {"item":  "banana", "qty":  1, "unit":  "amount"}])
        self.d = Data(filepath=self._filepath)

    def tearDown(self):
        remove_recipe_file(self._filepath)

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

