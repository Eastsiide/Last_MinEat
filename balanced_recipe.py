# Step 1: Ask the user for three values
prep_time = int(input("Enter preparation time in minutes: "))
ingredient_count = int(input("Enter number of ingredients: "))
calories = int(input("Enter calorie count: "))

# Step 2: Determine the middle value correctly using if/elif/else
if (prep_time > ingredient_count and prep_time < calories) or (prep_time < ingredient_count and prep_time > calories):
    middle = prep_time
    category = "minutes of prep time"
elif (ingredient_count > prep_time and ingredient_count < calories) or (ingredient_count < prep_time and ingredient_count > calories):
    middle = ingredient_count
    category = "ingredients"
else:
    middle = calories
    category = "calories"

# Step 3: Display the correct middle value
print(f"\nThe middle value was {middle} ({category}).")
