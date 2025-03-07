# Store available recipes (Dictionary with lists)
recipes = {
    "Chicken Mole": ["chicken", "mole", "mexican rice", "rice", "refried beans", "beans", "pinto beans"],
    "Carne Asada Tortas": ["skirt steak", "refried beans", "crema", "guacamole"],
    "Tostadas with Chicharron": ["chicharron", "refried beans", "guacamole", "tostada", "queso fresco"]
}

# Ask the user to enter ingredients
user_input = input("Enter your ingredients (comma-separated): ").lower()

# Create a list of ingredients
user_ingredients = user_input.split(",")  # Create a list from input
for i in range(len(user_ingredients)):  # Loop through each ingredient
    user_ingredients[i] = user_ingredients[i].strip()  # Remove spaces

# Find matching recipes (Checking if any ingredient is in a recipe)
matching_recipes = []  # Empty list for matches

for recipe in recipes:  # Loop through recipe names
    ingredient_list = recipes[recipe]  # Get the list of ingredients
    match_count = 0  # Counter for matching ingredients

    for ingredient in ingredient_list:  # Loop through each recipe's ingredients
        if ingredient in user_ingredients:  # Check if user has this ingredient
            match_count += 1  # Increase match count

    if match_count > 0:  # If at least one ingredient matches, add the recipe
        matching_recipes.append((recipe, match_count))  # Store recipe with match count

# Sort the recipes by the highest match count (Beginner sorting)
for i in range(len(matching_recipes) - 1):  
    for j in range(len(matching_recipes) - 1 - i):
        if matching_recipes[j][1] < matching_recipes[j + 1][1]:
            matching_recipes[j], matching_recipes[j + 1] = matching_recipes[j + 1], matching_recipes[j]

# Display results
print("\nSearching for recipes...\n")

if len(matching_recipes) > 0:
    print("You can make the following Last MinEat recipe(s) (Most Matches First):")
    for recipe in matching_recipes:
        print("- " + recipe[0] + f" ({recipe[1]} matching ingredient{'s' if recipe[1] > 1 else ''})")
else:
    print("No exact matches found. Try adding more ingredients!")

print("\nEnjoy your Last MinEat meal!")
