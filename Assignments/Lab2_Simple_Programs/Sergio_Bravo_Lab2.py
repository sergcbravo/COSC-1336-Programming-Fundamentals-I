# Sergio_Bravo_Lab2_.py
# This program calculates the ingredients needed for a desired number of spaghetti servings.

# Constants for the original recipe
RECIPE_SERVINGS = 4
TOMATO_SAUCE = 2  # cups
TOMATO_PASTE = 0.333  # cups
GARLIC = 2  # cloves
OREGANO = 1  # tablespoon

# Input: Number of servings desired
servings = float(input("Enter the number of servings of spaghetti sauce you want to make: "))

# Processing: Calculate ingredient amounts per serving
tomato_sauce_needed = (TOMATO_SAUCE / RECIPE_SERVINGS) * servings
tomato_paste_needed = (TOMATO_PASTE / RECIPE_SERVINGS) * servings
garlic_needed = (GARLIC / RECIPE_SERVINGS) * servings
oregano_needed = (OREGANO / RECIPE_SERVINGS) * servings

# Output: Display the required amounts of each ingredient
print(f"To make {servings:.1f} servings of spaghetti sauce, you will need:")
print(f"{tomato_sauce_needed:.2f} cups of tomato sauce")
print(f"{tomato_paste_needed:.2f} cups of tomato paste")
print(f"{garlic_needed:.2f} cloves of garlic")
print(f"{oregano_needed:.2f} tablespoons of oregano")
