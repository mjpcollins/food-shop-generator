import os
import json
from copy import deepcopy


def create_recipe_file(filepath):
    remove_recipe_file(filepath)
    with open(filepath, 'w') as F:
        F.write(json.dumps(get_starting_recipes(), indent=1))


def remove_recipe_file(filepath):
    try:
        os.remove(filepath)
    except FileNotFoundError:
        pass


def get_starting_recipes():
    starting_recipes = {
        "meal": {
            "breakfast": {
                "overnight_oats": {
                    "category": "veggie",
                    "speed": "very_fast",
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
                    "category": "veggie",
                    "speed": "very_fast",
                    "ingredients": [
                        {
                            "item": "salad",
                            "qty": 1,
                            "unit": "handful"
                        },
                        {
                            "item": "tomatoes",
                            "qty": 1,
                            "unit": "amount"
                        },
                        {
                            "item": "bread",
                            "qty": 2,
                            "unit": "slice"
                        },
                        {
                            "item": "cheese",
                            "qty": 125,
                            "unit": "g"
                        }
                    ]
                }
            },
            "dinner": {
                "roast_pork": {
                    "servings": 2,
                    "category": "meat",
                    "speed": "slow",
                    "ingredients": [
                        {
                            "item": "pork_loin",
                            "qty": 1,
                            "unit": "amount"
                        },
                        {
                            "item": "potatoes",
                            "qty": 500,
                            "unit": "g"
                        },
                        {
                            "item": "carrots",
                            "qty": 300,
                            "unit": "g"
                        },
                        {
                            "item": "broccoli",
                            "qty": 300,
                            "unit": "g"
                        }
                    ]
                },
                "tomato_and_marsc_risotto": {
                    "servings": 2,
                    "category": "veggie",
                    "speed": "fast",
                    "ingredients": [
                        {
                            "item": "risotto",
                            "qty": 200,
                            "unit": "g"
                        },
                        {
                            "item": "tomatoes",
                            "qty": 6,
                            "unit": "amount"
                        },
                        {
                            "item": "garlic_paste",
                            "qty": 1,
                            "unit": "teaspoon"
                        },
                        {
                            "item": "marscarpone",
                            "qty": 125,
                            "unit": "g"
                        },
                        {
                            "item": "chicken_stock_cubes",
                            "qty": 2,
                            "unit": "amount"
                        },
                        {
                            "item": "white_wine_vinegar",
                            "qty": 25,
                            "unit": "ml"
                        },
                        {
                            "item": "salad",
                            "qty": 2,
                            "unit": "handful"
                        }
                    ]
                }}
        }
    }

    return starting_recipes


def get_starting_recipes_plus_one(starting_recipes):
    starting_recipes_plus_one = deepcopy(starting_recipes)
    starting_recipes_plus_one['meal']['breakfast']["peanut_butter_toast"] = {
        "servings": 1,
        "category": "veggie",
        "speed": "very_fast",
        "ingredients": [
            {
                "item": "bread",
                "qty": 1,
                "unit": "slice"
            },
            {
                "item": "peanut_butter",
                "qty": 1,
                "unit": "tablespoon"
            },
            {
                "item": "banana",
                "qty": 1,
                "unit": "amount"
            }
        ]
    }
    return starting_recipes_plus_one
