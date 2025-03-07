import json
import sys


#Store available recipes
recipes = {
  "Chicken Mole": ["chicken, mole, mexican rice, refried beans, pinto beans"],
  "Carne Asada Tortas": ["skirt steak, refried beans, crema, guacamole"],
  "Tostadas with Chorizo": ["chicharron, refried beans, guacamole, tostada, queso fresco"]
}


# Get ingredients from JavaScript
user_ingredients = json.loads(sys.argv[1]


# Find matching recipes
matching_recipes = []
for recipe, ingredients in recipes.items():
  if all(ingredient in user_ingredients for ingredient in ingredients):
      matching_recipes.append(recipe)


if matching_recipes:
    print(json.dumps({"recipes": matching_recipes}))
else:
    print(json.dumps({"error": "No exact matches found. Try adding more ingredients!"}))
