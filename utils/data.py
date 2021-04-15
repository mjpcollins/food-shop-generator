import json


class Data:

    def __init__(self, filepath):
        self.filepath = filepath
        self._data = {}
        self._load()

    def _load(self):
        with open(self.filepath, 'r') as F:
            self._data = json.load(F)
        return self._data

    def add_recipe(self, recipe):
        self._data["meal"][recipe.meal][recipe.name] = {
            "servings": recipe.servings,
            "category": recipe.category,
            "speed": recipe.speed,
            "ingredients": recipe.get_ingredients()
        }

    def get_recipes(self):
        return self._data

    def write(self):
        with open(self.filepath, 'w') as F:
            F.write(json.dumps(self._data, indent=1))
