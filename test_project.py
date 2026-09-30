import unittest

from cooking_app.recipes import RECIPES
from cooking_app.search import search_recipes
from cooking_app.validation import recipe_exists, clean_search


class RecipeAppTests(unittest.TestCase):

    def test_recipes_exist(self):
        self.assertGreaterEqual(len(RECIPES), 8)

    def test_recipe_exists(self):
        self.assertTrue(recipe_exists("Masala Pasta", RECIPES))
        self.assertFalse(recipe_exists("Pizza From Mars", RECIPES))

    def test_search_by_name(self):
        results = search_recipes(RECIPES, "pasta")
        self.assertIn("Masala Pasta", results)
        self.assertIn("Tomato Pasta", results)

    def test_search_by_ingredient(self):
        results = search_recipes(RECIPES, "paneer")
        self.assertIn("Paneer Butter Masala", results)

    def test_clean_search(self):
        self.assertEqual(clean_search("  pasta  "), "pasta")


if __name__ == "__main__":
    unittest.main()
