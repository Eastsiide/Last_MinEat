#Store available recipes
recipes = {
  "Chicken Mole": ["chicken, mole, mexican rice, refried beans, pinto beans"],
  "Carne Asada Tortas": ["skirt steak, refried beans, crema, guacamole"],
  "Tostadas with Chorizo": ["chicharron, refried beans, guacamole, tostada, queso fresco"]
}


# Ask user to input ingredients available at home
user_input = input("Enter your ingredients (comma-separated): ").lower()
user_ingredients = [ingredient.strip() for ingredient in user_input.split(",")]


# Find matching recipes
matching_recipes = []
for recipe, ingredients in recipes.items()
    if all(ingredient in user_ingredients for ingredient in ingredients):
        matching_recipes.append(recipe)


print("\n Searching for recipes...\n")


if matching recipes:
    print("You can make the following Last MinEat recipe(s):")
    for recipe in matching_recipes:
        print(f"- {recipe]")
else:
    print("No exact matches found. Try adding more ingredients!")


print("\n Enjoy your Last MinEat meal!")
