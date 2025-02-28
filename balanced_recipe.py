# Step 1: Ask the user to enter prep time, ingredient count, and calories for a recipe
prep_time = int(input("Enter preparation time in minutes: "))
ingredient_count = int(input("Enter number of ingredients: "))
calories = int(input("Enter calorie count: "))

# Step 2: Determine the middle-balanced recipe
if (prep_time < ingredient_count < calories) or (calories < ingredient_count < prep_time):
    middle = ingredient_count
    category = "ingredients"
elif (ingredient_count < prep_time < calories) or (calories < prep_time < ingredient_count):
    middle = prep_time
    category = "minutes of prep time"
else:
    middle = calories
    category = "calories"

# Step 3: Display the result
print(f"\nThe most balanced recipe has {middle} {category}.")
